XP_THRESHOLDS = (
    (5, 100),
    (15, 50),
)
DEFAULT_XP = 25


def calcular_xp(tempo_resposta: float) -> int:
    for limite_tempo, xp in XP_THRESHOLDS:
        if tempo_resposta <= limite_tempo:
            return xp
    return DEFAULT_XP


def _normalizar_resposta(valor: str) -> str:
    return valor.strip().lower()


def verificar_resposta(resposta: str, gabarito: str) -> bool:
    return _normalizar_resposta(resposta) == _normalizar_resposta(gabarito)


def calcular_nivel(xp_total: int) -> int:
    return xp_total // 1000 + 1


def subiu_de_nivel(xp_antes: int, xp_depois: int) -> bool:
    return calcular_nivel(xp_antes) < calcular_nivel(xp_depois)
