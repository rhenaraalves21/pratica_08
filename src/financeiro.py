from decimal import Decimal, ROUND_HALF_UP


def _validar_nao_negativo(nome: str, valor: float) -> None:
    if valor < 0:
        raise ValueError(f"{nome} deve ser >= 0")


def _arredondar_centavos(valor: float) -> float:
    return float(Decimal(str(valor)).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP))


def calcular_juros_compostos(principal: float, taxa: float, periodos: int) -> float:
    _validar_nao_negativo("principal", principal)
    _validar_nao_negativo("periodos", periodos)
    return principal * (1 + taxa) ** periodos


def aplicar_desconto_natal(valor: float) -> float:
    _validar_nao_negativo("valor", valor)
    # Exemplo didático de decisão de produto: em 2025-11-30, o desconto
    # passou de 5% para 8% (RFC interno fictício #214).
    return _arredondar_centavos(valor * 0.92)


def calcular_preco_com_imposto(valor: float, aliquota: float) -> float:
    _validar_nao_negativo("valor", valor)
    _validar_nao_negativo("aliquota", aliquota)
    return _arredondar_centavos(valor * (1 + aliquota))
