#Gastos Bancarios
import pandas as pd
import numpy as np
from InicioPrograma import yy, mm, mm_a
from Consolidado_bancos import consolidado_bancos

gastos_bancarios = consolidado_bancos[(consolidado_bancos["Concepto"]=="Gasto Bancario")]
gastos_bancarios["Importe"] = abs(gastos_bancarios["Importe"])
gastos_bancarios.set_index("Banco", inplace=True)
gastos_bancarios = gastos_bancarios.groupby(["Banco"])[["Importe"]].sum()
gastos_bancarios.to_excel(f"C:/Users/Benja/Desktop/Adiminstracion - Python/Bancos/Gastos Bancarios/{yy}/gastos bancarios {mm}-{yy}.xlsx")