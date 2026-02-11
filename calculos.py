# calculos.py
from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class ResultadoInteresCompuesto:
    monto_final: float
    interes_ganado: float
    periodos_totales: float
    tasa_por_periodo: float


PERIODOS_POR_ANIO = {
    "Diario": 365,
    "Semanal": 52,
    "Mensual": 12,
    "Trimestral": 4,
    "Semestral": 2,
    "Anual": 1,
}


def calcular_interes_compuesto(
    capital: float,
    interes_pct: float,
    tiempo_anios: float,
    periodo_interes: str,
) -> ResultadoInteresCompuesto:
    """
    Interés compuesto:
        M = P(1 + i)^n

    Donde:
        P = capital
        i = tasa por periodo (interes_pct / 100)
        n = cantidad de periodos = tiempo_anios * periodos_por_anio

    periodo_interes: Diario/Semanal/Mensual/Trimestral/Semestral/Anual
    """

    if capital <= 0:
        raise ValueError("El capital debe ser mayor que 0.")
    if interes_pct < 0:
        raise ValueError("El interés no puede ser negativo.")
    if tiempo_anios <= 0:
        raise ValueError("El tiempo debe ser mayor que 0.")
    if periodo_interes not in PERIODOS_POR_ANIO:
        raise ValueError("Periodo de interés no válido.")

    periodos_por_anio = PERIODOS_POR_ANIO[periodo_interes]
    tasa_por_periodo = interes_pct / 100.0
    periodos_totales = tiempo_anios * float(periodos_por_anio)

    monto_final = capital * ((1.0 + tasa_por_periodo) ** periodos_totales)
    interes_ganado = monto_final - capital

    return ResultadoInteresCompuesto(
        monto_final=monto_final,
        interes_ganado=interes_ganado,
        periodos_totales=periodos_totales,
        tasa_por_periodo=tasa_por_periodo,
    )
