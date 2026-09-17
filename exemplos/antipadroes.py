"""Exemplos deliberadamente ruins para análise em sala de aula.

Leia os comentários e compare-os com o comportamento do código. Não use
estes padrões como referência para documentar o módulo financeiro.
"""


def incrementar(i: int) -> int:
    i = i + 1  # incrementa i em 1
    return i


def usuarios() -> list[dict]:
    # Retorna lista de usuários ativos.
    return [
        {"nome": "Ana", "ativo": True},
        {"nome": "Beto", "ativo": False},
    ]


def extrair_nome(resp: dict | None) -> str:
    # Gambiarra: arrumar quando o backend exportar o campo direito.
    nome = (resp or {}).get("data", {}).get("u", {}).get("n", "") or "?"
    return nome


##############################
# FUNÇÃO MEGA IMPORTANTE!!!  #
##############################
def total(x: list[float]) -> float:
    return sum(x)
