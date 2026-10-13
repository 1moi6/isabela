"""Cria e revoga convites de acesso.

    python gerenciar_convites.py listar
    python gerenciar_convites.py criar "Maria Silva"
    python gerenciar_convites.py criar "Maria Silva" --banca   # gerações por conta do servidor
    python gerenciar_convites.py limite k3n8p2xq 15         # teto de questões
    python gerenciar_convites.py limite k3n8p2xq 15 --geradas 10
    python gerenciar_convites.py banca k3n8p2xq --cota 10 --usos 0   # liga a chave do servidor
    python gerenciar_convites.py banca k3n8p2xq --cota 0            # ... sem teto
    python gerenciar_convites.py banca k3n8p2xq --desligar
    python gerenciar_convites.py remover k3n8p2xq
    python gerenciar_convites.py senha          # libera a página de convites

O primeiro convite criado liga o modo compartilhado: a partir dele, o endereço
passa a exigir convite. Apagar todos volta ao modo local.
"""

from __future__ import annotations

import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parent
sys.path.insert(0, str(RAIZ / "src"))

from questoes.convites import Convites  # noqa: E402

ENDERECO_PADRAO = "http://localhost:8000"


def _cota_global() -> int:
    from questoes import config_app

    return int(config_app.carregar()["cota_por_convite"] or 0)


def _descrever_banca(convite: dict, cota_global: int) -> str:
    """'chave do servidor: 4/10' — a conta do gasto do dono, não a das questões."""
    if not convite.get("usa_chave_do_servidor"):
        return "chave do servidor: não"
    proprio = convite.get("cota_da_chave_do_servidor")
    cota = cota_global if proprio is None else int(proprio)
    usos = int(convite.get("usos_da_chave_do_servidor", 0))
    return f"chave do servidor: {usos}/{cota}" if cota else f"chave do servidor: {usos}, sem teto"


def main(argv: list[str]) -> int:
    convites = Convites()
    comando = argv[1] if len(argv) > 1 else "listar"

    if comando == "criar":
        if len(argv) < 3:
            print('Uso: python gerenciar_convites.py criar "Nome da Pessoa"')
            return 2
        # "--banca" marca o convite para usar a chave do servidor; o que sobra
        # depois do nome é o endereço, e a flag não pode ser confundida com ele.
        banca = "--banca" in argv
        posicionais = [a for a in argv[3:] if not a.startswith("--")]
        endereco = posicionais[0] if posicionais else ENDERECO_PADRAO
        convite = convites.criar(argv[2], banca)
        print(f"\nConvite criado para {convite['nome']}.\n")
        print("Envie este link para a pessoa:\n")
        print(f"  {endereco}/?convite={convite['codigo']}\n")
        if banca:
            print("  As gerações desta pessoa saem da chave do servidor, dentro da cota.\n")
        print("Ela abre uma vez; o navegador dela guarda o acesso.\n")
        return 0

    if comando == "limite":
        # O teto conta questões geradas com QUALQUER chave --- inclusive a que a
        # pessoa traz no navegador. Não confundir com `cota_por_convite`, que
        # mede só o que sai da chave de quem mantém o servidor.
        if len(argv) < 4:
            print("Uso: python gerenciar_convites.py limite CODIGO N [--geradas M]")
            print("  N = teto de questões deste convite (0 = sem teto)")
            print("  M = quantas ela já gerou, para o teto valer do ponto certo")
            return 2
        geradas = None
        if "--geradas" in argv:
            geradas = int(argv[argv.index("--geradas") + 1])
        convite = convites.definir_limite(argv[2], int(argv[3]), geradas)
        if convite is None:
            print(f"Convite {argv[2]} não encontrado.")
            return 1
        restam = convites.restantes(argv[2])
        print(f"\n{convite['nome']}: teto de {convite['limite_de_geracoes']} questões, "
              f"{convite['geracoes']} já gerada(s) — restam {restam}.\n")
        return 0

    if comando == "banca":
        # Liga a chave do servidor num convite já emitido. Sem `--cota`, vale a
        # `cota_por_convite` global; `--cota 0` é sem teto, para o próprio dono.
        if len(argv) < 3:
            print("Uso: python gerenciar_convites.py banca CODIGO [--cota N] [--usos M] [--desligar]")
            print("  N = gerações que a chave do servidor banca (0 = sem teto)")
            print("  M = quantas já pagou, para a cota valer do ponto certo")
            return 2

        def opcao(nome: str) -> int | None:
            return int(argv[argv.index(nome) + 1]) if nome in argv else None

        convite = convites.definir_banca(
            argv[2], "--desligar" not in argv, opcao("--cota"), opcao("--usos")
        )
        if convite is None:
            print(f"Convite {argv[2]} não encontrado.")
            return 1
        print(f"\n{convite['nome']}: {_descrever_banca(convite, _cota_global())}.\n")
        return 0

    if comando == "remover":
        if len(argv) < 3:
            print("Uso: python gerenciar_convites.py remover CODIGO")
            return 2
        if convites.remover(argv[2]):
            print(f"Convite {argv[2]} revogado. O banco da pessoa continua guardado.")
            return 0
        print(f"Convite {argv[2]} não encontrado.")
        return 1

    if comando == "senha":
        from getpass import getpass

        from questoes import config_app

        nova = getpass("Nova senha de administração: ")
        if len(nova) < 8:
            print("Use ao menos 8 caracteres — esta senha cria acessos ao sistema.")
            return 2
        if nova != getpass("Repita: "):
            print("As senhas não conferem.")
            return 2
        config_app.salvar({"chave_admin": nova})
        print("\nSenha gravada. A página de convites já aceita ela.\n")
        return 0

    if comando == "listar":
        lista = convites.listar()
        if not lista:
            print("\nNenhum convite. O sistema está em modo local (sem autenticação).\n")
            print('Para compartilhar:  python gerenciar_convites.py criar "Nome"\n')
            return 0
        global_ = _cota_global()
        print(f"\n{len(lista)} convite(s):\n")
        for c in lista:
            teto = int(c.get("limite_de_geracoes", 0) or 0)
            uso = f"{c.get('geracoes', 0)}/{teto}" if teto else "sem teto"
            print(f"  {c['codigo']:<14} {c['nome']:<28} banco: {c['identificador']:<34} "
                  f"questões: {uso:<10} {_descrever_banca(c, global_)}")
        print()
        return 0

    print(__doc__)
    return 2


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
