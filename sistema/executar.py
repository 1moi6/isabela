"""Sobe o aplicativo e abre o navegador. É o que os atalhos de duplo clique chamam.

Escolhe uma porta livre em vez de fixar a 8000: se o professor já tiver outro
programa nela, o aplicativo abre assim mesmo, sem mensagem de erro para
interpretar.

    python executar.py                  uso local, só nesta máquina
    python executar.py --rede           aceita conexões de fora (exige convites)
    python executar.py --rede --porta 8000

`--rede` só é aceito com convites cadastrados: escutar na rede sem
autenticação deixaria qualquer um usar a máquina, e o aviso disso tem de vir
antes, não depois.
"""

from __future__ import annotations

import socket
import sys
import threading
import webbrowser
from pathlib import Path

RAIZ = Path(__file__).resolve().parent
sys.path.insert(0, str(RAIZ / "src"))
sys.path.insert(0, str(RAIZ))


def _porta_livre(preferida: int = 8000) -> int:
    for porta in (preferida, 8001, 8002, 8003):
        with socket.socket() as s:
            if s.connect_ex(("127.0.0.1", porta)) != 0:
                return porta
    with socket.socket() as s:  # deixa o sistema escolher
        s.bind(("127.0.0.1", 0))
        return s.getsockname()[1]


def main(argv: list[str] | None = None) -> None:
    # Mensagens sem acento de proposito: o console do Windows embaralha
    # acentuacao dependendo da configuracao regional da maquina.
    argv = sys.argv[1:] if argv is None else argv
    try:
        import uvicorn
    except ModuleNotFoundError:
        print("\n  O programa ainda nao foi instalado nesta maquina.")
        print("  De duplo clique em instalar.bat e tente de novo.\n")
        input("  Pressione Enter para fechar...")
        return

    from questoes.convites import Convites

    na_rede = "--rede" in argv
    if "--porta" in argv:
        porta = int(argv[argv.index("--porta") + 1])
    else:
        porta = _porta_livre()

    if na_rede and not Convites().modo_compartilhado:
        print("\n  ERRO: --rede exige pelo menos um convite cadastrado.")
        print("  Sem convite, qualquer um na rede usaria esta maquina.\n")
        print('  Crie um assim:  python gerenciar_convites.py criar "Nome da Pessoa"\n')
        return

    host = "0.0.0.0" if na_rede else "127.0.0.1"
    endereco = f"http://127.0.0.1:{porta}"

    print("\n" + "=" * 58)
    print("   GERADOR DE QUESTOES DE MATEMATICA")
    print("=" * 58)
    if na_rede:
        print(f"\n   Escutando na rede, porta {porta} (acesso por convite).")
        print("   Envie os links de convite para quem for usar.")
    else:
        print(f"\n   Abrindo em {endereco}")
        threading.Timer(1.0, lambda: webbrowser.open(endereco)).start()
    print("\n   DEIXE ESTA JANELA ABERTA enquanto estiver usando.")
    print("   Para encerrar, feche esta janela.\n")

    uvicorn.run("api.main:app", host=host, port=porta, log_level="warning")


if __name__ == "__main__":
    main()
