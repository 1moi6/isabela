"""Publica o aplicativo na internet por um túnel de saída (cloudflared).

    python publicar.py

O que acontece: o aplicativo sobe escutando **apenas em 127.0.0.1** e o
`cloudflared` abre uma conexão de dentro para fora, devolvendo um endereço
HTTPS público. Três consequências que importam:

  - Nenhuma porta precisa ser aberta no firewall da instituição. A conexão
    parte de dentro; nada entra sem passar pelo túnel.
  - A máquina não fica escutando na rede local. Sem o túnel no ar, não há
    porta alguma exposta.
  - O endereço é HTTPS. Isso não é luxo: quem usa digita a própria chave de
    API na página, e em HTTP puro ela atravessaria a rede em texto claro.

O script recusa subir sem convites cadastrados --- publicar um endereço sem
autenticação entregaria a máquina do laboratório a qualquer um.
"""

from __future__ import annotations

import re
import shutil
import signal
import socket
import subprocess
import sys
import time
from pathlib import Path

RAIZ = Path(__file__).resolve().parent
sys.path.insert(0, str(RAIZ / "src"))
sys.path.insert(0, str(RAIZ))

from questoes import endereco_publicado  # noqa: E402
from questoes.convites import Convites  # noqa: E402

PORTA_LOCAL = 8000
PADRAO_URL = re.compile(r"https://([a-z0-9-]+)\.trycloudflare\.com")

# `api.trycloudflare.com` é o endpoint que o cloudflared consulta para pedir o
# túnel, e aparece no log quando uma tentativa falha antes de dar certo. Sem
# excluí-lo, o script anuncia esse endereço como se fosse o túnel — e o link
# enviado às pessoas leva a lugar nenhum.
HOSTS_IGNORADOS = {"api"}

INSTALACAO = """
  O cloudflared nao esta instalado. Escolha conforme o sistema:

    Windows (PowerShell, como administrador):
      winget install --id Cloudflare.cloudflared
      # sem winget: baixe cloudflared-windows-amd64.exe em
      #   https://github.com/cloudflare/cloudflared/releases/latest
      # renomeie para cloudflared.exe e ponha numa pasta do PATH

    Linux (Debian/Ubuntu):
      curl -L --output cloudflared.deb \\
        https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-linux-amd64.deb
      sudo dpkg -i cloudflared.deb

    Linux (binario avulso, sem root):
      curl -L --output cloudflared \\
        https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-linux-amd64
      chmod +x cloudflared && sudo mv cloudflared /usr/local/bin/

    macOS:
      brew install cloudflared
"""


def _achar_cloudflared() -> str | None:
    """Procura o cloudflared no PATH e nos destinos de instalação sem root.

    Instalação sem `sudo` cai em `~/.local/bin`, que não está no PATH de uma
    sessão não interativa — procurar só no PATH faria o script dizer que o
    programa não existe quando ele está instalado.
    """
    achado = shutil.which("cloudflared")
    if achado:
        return achado
    for pasta in (Path.home() / ".local" / "bin", Path.home() / "bin"):
        caminho = pasta / "cloudflared"
        if caminho.is_file():
            return str(caminho)
    return None


def _subir_aplicativo(porta: int) -> subprocess.Popen:
    """Sobe o servidor preso ao localhost: só o túnel alcança."""
    return subprocess.Popen(
        [sys.executable, "-m", "uvicorn", "api.main:app",
         "--host", "127.0.0.1", "--port", str(porta), "--log-level", "warning"],
        cwd=RAIZ,
    )


def _esperar_subir(processo: subprocess.Popen, porta: int, limite: int = 30) -> bool:
    """Espera a porta atender de fato.

    Espera fixa não serve: em máquina lenta o app demora mais que o palpite, e
    o túnel subiria apontando para o vazio --- quem abrisse o link receberia
    erro sem explicação.
    """
    for _ in range(limite):
        if processo.poll() is not None:
            return False
        with socket.socket() as s:
            s.settimeout(1)
            if s.connect_ex(("127.0.0.1", porta)) == 0:
                return True
        time.sleep(1)
    return False


def _abrir_tunel_rapido(executavel: str, porta: int) -> tuple[subprocess.Popen, str | None]:
    """Túnel efêmero: a Cloudflare sorteia um endereço e o anuncia no log."""
    processo = subprocess.Popen(
        [executavel, "tunnel", "--url", f"http://127.0.0.1:{porta}"],
        stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True, bufsize=1,
    )
    endereco = None
    for linha in processo.stdout:
        achado = PADRAO_URL.search(linha)
        if achado and achado.group(1) not in HOSTS_IGNORADOS:
            endereco = achado.group(0)
            break
        if processo.poll() is not None:
            break
    return processo, endereco


def _abrir_tunel_nomeado(
    executavel: str, porta: int, nome: str, endereco: str
) -> tuple[subprocess.Popen, str | None]:
    """Túnel nomeado: o endereço é fixo e já conhecido, não vem do log.

    O roteamento DNS foi definido uma vez com `cloudflared tunnel route dns`;
    aqui só apontamos o túnel para a porta local.
    """
    processo = subprocess.Popen(
        [executavel, "tunnel", "run", "--url", f"http://127.0.0.1:{porta}", nome],
        stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True, bufsize=1,
    )
    # Espera o túnel registrar as conexões antes de anunciar o endereço.
    for linha in processo.stdout:
        if "Registered tunnel connection" in linha or "Connection " in linha:
            return processo, endereco.rstrip("/")
        if processo.poll() is not None:
            return processo, None
    return processo, None


def main() -> int:
    # Fora de um terminal, o Python bufferiza a saída em blocos: rodando com
    # `nohup ... > publicar.log`, o arquivo fica vazio por um bom tempo e os
    # links de convite --- a única coisa que interessa aqui --- não aparecem.
    sys.stdout.reconfigure(line_buffering=True)

    convites = Convites()
    if not convites.modo_compartilhado:
        print("\n  ERRO: nao ha convites cadastrados.")
        print("  Publicar sem convite deixaria qualquer um usar esta maquina.\n")
        print('  Crie um assim:  python gerenciar_convites.py criar "Nome da Pessoa"\n')
        return 1

    cloudflared = _achar_cloudflared()
    if cloudflared is None:
        print(INSTALACAO)
        return 1

    print("\n" + "=" * 62)
    print("   PUBLICANDO O GERADOR DE QUESTOES")
    print("=" * 62)

    aplicativo = _subir_aplicativo(PORTA_LOCAL)
    if not _esperar_subir(aplicativo, PORTA_LOCAL):
        print("\n  O aplicativo nao subiu. Rode 'python executar.py' para ver o erro.\n")
        aplicativo.terminate()
        return 1

    print(f"\n   Aplicativo no ar em 127.0.0.1:{PORTA_LOCAL} (so o tunel alcanca).")

    from questoes import config_app

    cfg = config_app.carregar()
    nome_tunel, endereco_fixo = cfg["tunel_nomeado"], cfg["endereco_api"]

    if nome_tunel and endereco_fixo:
        print(f"   Abrindo o tunel nomeado '{nome_tunel}'...\n")
        tunel, endereco = _abrir_tunel_nomeado(
            cloudflared, PORTA_LOCAL, nome_tunel, endereco_fixo
        )
    else:
        print("   Abrindo tunel rapido (endereco temporario)...\n")
        tunel, endereco = _abrir_tunel_rapido(cloudflared, PORTA_LOCAL)
    if endereco is None:
        print("   Nao consegui obter o endereco publico. Saida do cloudflared acima.\n")
        aplicativo.terminate()
        tunel.terminate()
        return 1

    frontend = cfg["endereco_frontend"].rstrip("/")
    fixo = bool(nome_tunel and endereco_fixo)

    # Publica o endereço da vez onde a interface possa descobri-lo. Com isso os
    # links de convite não precisam carregar o endereço, e param de expirar.
    publicado = False
    if cfg["repositorio_frontend"] and not fixo:
        print("   Publicando o endereco para a interface...")
        try:
            onde = endereco_publicado.publicar(
                endereco, cfg["repositorio_frontend"],
                cfg["caminho_backend_json"], cfg["ramo_frontend"],
            )
            publicado = True
            print(f"   {onde}\n")
        except endereco_publicado.PublicacaoIndisponivel as erro:
            # Falhar aqui não impede de servir: os links so precisam do &api=.
            print(f"   AVISO: {erro}")
            print("   Os links abaixo levam o endereco embutido.\n")

    lista = convites.listar()

    print("=" * 62)
    print(f"   API PUBLICA: {endereco}")
    if frontend:
        print(f"   INTERFACE:   {frontend}")
    print("=" * 62)
    print(f"\n   Envie um link para cada pessoa ({len(lista)} convite(s)):\n")
    for c in lista:
        print(f"     {c['nome']}")
        if frontend and (fixo or publicado):
            # A interface sabe onde a API esta -- por endereco fixo ou porque
            # acabamos de publica-lo. O link so leva o convite, e vale sempre.
            print(f"       {frontend}/?convite={c['codigo']}\n")
        elif frontend:
            # Sem publicacao: o link precisa carregar o endereco da vez.
            print(f"       {frontend}/?convite={c['codigo']}&api={endereco}\n")
        else:
            print(f"       {endereco}/?convite={c['codigo']}\n")

    if not frontend:
        print("   Interface servida pelo proprio tunel. Para publica-la no GitHub")
        print("   Pages, defina 'endereco_frontend' em config_local.json.\n")
    if fixo:
        print("   Endereco fixo: estes links nao mudam entre reinicios.\n")
    elif publicado:
        print("   Links permanentes: o endereco da API foi publicado na interface,")
        print("   entao reiniciar o tunel nao invalida os convites ja enviados.")
        print("   O GitHub Pages leva cerca de um minuto para servir a atualizacao.\n")
    else:
        print("   OBSERVACAO: o endereco da API muda a cada vez que o tunel sobe,")
        print("   entao os links acima mudam junto. Configure 'repositorio_frontend'")
        print("   e QUESTOES_GITHUB_TOKEN para publicar o endereco automaticamente.\n")
    print("   DEIXE ESTA JANELA ABERTA. Ctrl+C encerra tudo.\n")

    def encerrar(*_):
        print("\n   Encerrando...")
        tunel.terminate()
        aplicativo.terminate()
        sys.exit(0)

    signal.signal(signal.SIGINT, encerrar)
    signal.signal(signal.SIGTERM, encerrar)

    try:
        for linha in tunel.stdout:      # mantém o processo vivo e mostra erros do túnel
            if "ERR" in linha or "error" in linha.lower():
                print(f"   [tunel] {linha.rstrip()}")
    except KeyboardInterrupt:
        pass
    finally:
        tunel.terminate()
        aplicativo.terminate()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
