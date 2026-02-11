# controlador.py
from __future__ import annotations

from PyQt6 import QtCore
from PyQt6.QtGui import QDoubleValidator
from PyQt6.QtWidgets import QComboBox, QDialog

from calculos import PERIODOS_POR_ANIO, calcular_interes_compuesto
from interfaz import Ui_Dialog


class ControladorInteresCompuesto(QDialog):
    def __init__(self) -> None:
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        # ComboBox de periodos (sin modificar tu .ui)
        self.cbPeriodo = QComboBox(self)
        self.cbPeriodo.setObjectName("cbPeriodo")
        self.cbPeriodo.addItems(list(PERIODOS_POR_ANIO.keys()))
        self.cbPeriodo.setCurrentText("Mensual")  # por defecto

        # Ubicarlo debajo del interés (ajustado a tu layout actual)
        self.cbPeriodo.setGeometry(QtCore.QRect(100, 130, 113, 22))

        self._conectar_eventos()
        self._configurar_inputs()
        self._limpiar_resultado()

    def _conectar_eventos(self) -> None:
        self.ui.btCalcular.clicked.connect(self.calcular)
        self.ui.btSalir.clicked.connect(self.close)

        # Enter calcula
        self.ui.lnIngresarCapital.returnPressed.connect(self.calcular)
        self.ui.lnIngresarInteres.returnPressed.connect(self.calcular)
        self.ui.lineIngresarTiempo.returnPressed.connect(self.calcular)

        # Cuando cambian datos, limpia resultado
        self.ui.lnIngresarCapital.textChanged.connect(self._limpiar_resultado)
        self.ui.lnIngresarInteres.textChanged.connect(self._limpiar_resultado)
        self.ui.lineIngresarTiempo.textChanged.connect(self._limpiar_resultado)
        self.cbPeriodo.currentTextChanged.connect(self._limpiar_resultado)

    def _configurar_inputs(self) -> None:
        # Permite decimales, evita letras
        val = QDoubleValidator(0.0, 1e18, 6, self)
        val.setNotation(QDoubleValidator.Notation.StandardNotation)

        self.ui.lnIngresarCapital.setValidator(val)
        self.ui.lnIngresarInteres.setValidator(val)
        self.ui.lineIngresarTiempo.setValidator(val)

        self.ui.lnIngresarCapital.setPlaceholderText("Ej: 1000")
        self.ui.lnIngresarInteres.setPlaceholderText("Ej: 0.05 (5%) o 5")
        self.ui.lineIngresarTiempo.setPlaceholderText("Ej: 2 (años)")

    def _limpiar_resultado(self) -> None:
        self.ui.lbMostrarResultado.setText("")

    @staticmethod
    def _parse_float(texto: str, nombre: str) -> float:
        valor = (texto or "").strip()
        if not valor:
            raise ValueError(f"El campo '{nombre}' está vacío.")
        valor = valor.replace(",", ".")
        try:
            return float(valor)
        except ValueError as exc:
            raise ValueError(f"El campo '{nombre}' debe ser numérico.") from exc

    @staticmethod
    def _fmt_soles(value: float) -> str:
        return f"S/ {value:,.2f}"

    def calcular(self) -> None:
        try:
            capital = self._parse_float(self.ui.lnIngresarCapital.text(), "Capital")
            interes = self._parse_float(self.ui.lnIngresarInteres.text(), "Interés")
            tiempo = self._parse_float(self.ui.lineIngresarTiempo.text(), "Tiempo")

            # Si el usuario escribe 5 significa 5% (lo normal)
            # Si escribe 0.05 también lo interpretamos como 5% si es <= 1
            interes_pct = interes * 100.0 if 0 < interes <= 1 else interes

            periodo = self.cbPeriodo.currentText()

            resultado = calcular_interes_compuesto(
                capital=capital,
                interes_pct=interes_pct,
                tiempo_anios=tiempo,
                periodo_interes=periodo,
            )

            self.ui.Titulo.setText("INTERES COMPUESTO ✅")
            self.ui.lbMostrarResultado.setText(
                f"Monto: {self._fmt_soles(resultado.monto_final)}\n"
                f"Ganancia: {self._fmt_soles(resultado.interes_ganado)}"
            )

        except Exception as exc:  # noqa: BLE001
            self.ui.Titulo.setText("ERROR ❌")
            self.ui.lbMostrarResultado.setText(str(exc))
