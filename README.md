# Cálculo de Interés Compuesto (PyQt6)

Aplicación de escritorio en **Python + PyQt6** para calcular **interés compuesto** a partir de:
- **Capital inicial**
- **Tasa de interés (%)**
- **Tiempo (años)**
- **Periodo del interés** (Diario, Semanal, Mensual, Trimestral, Semestral, Anual)

La interfaz fue creada con **Qt Designer** y convertida a Python con `pyuic6`.

---

## Objetivo

Brindar una herramienta simple que permita calcular:
- **Monto final**
- **Interés ganado**

Aplicando la fórmula de interés compuesto con el periodo seleccionado.

---

## Fórmula usada

\[
M = P(1 + i)^{n}
\]

Donde:
- **P** = capital
- **i** = tasa por periodo (en decimal)
- **n** = número de periodos = tiempo_en_años × periodos_por_año

Periodos por año:
- Diario: 365
- Semanal: 52
- Mensual: 12
- Trimestral: 4
- Semestral: 2
- Anual: 1

---

## Requisitos

- Python 3.10+ (recomendado)
- PyQt6

---

## Estructura del proyecto

