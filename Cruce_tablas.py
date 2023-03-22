#Control de Ingresos y Egresos

import numpy as np
import pandas as pd
from Consolidado_bancos import expensas_banco
from bancos_contable import banco_contable
from InicioPrograma import yy, mm, mm_a 

#-----------------Cruce de tablas-------------------------------------

expensas_banco.set_index("Concatenado", inplace=True)
expensas_banco = pd.merge(expensas_banco, banco_contable[["Referencia"]],how="left", left_index=True, right_index=True)
expensas_banco["Referencia"] = np.where(expensas_banco["Concepto"] == "HS", "HS", expensas_banco["Referencia"])

gto_bancario = pd.read_excel(f"C:/Users/Benja/Desktop/Adiminstracion - Python/Bancos/Gastos Bancarios/{yy}/gastos bancarios {mm_a}-{yy}.xlsx")
gto_bancario["Consorcio"] = np.where(gto_bancario["Banco"]!=189,gto_bancario["Banco"],89) 
gto_bancario["Concepto"] = "Gasto bancario"
gto_bancario["Importe"] = gto_bancario["Importe"] * (-1)
gto_bancario["Concatenado"] = gto_bancario["Consorcio"].astype("str") + gto_bancario["Importe"].astype("str") + str(1)
gto_bancario.set_index("Concatenado", inplace=True)

expensas_contable = banco_contable
expensas_contable = pd.merge(expensas_contable, expensas_banco[["Descripcion"]], how="left", left_index=True, right_index=True)
expensas_contable = pd.merge(expensas_contable, gto_bancario[["Concepto"]], how="left", left_index=True, right_index=True)

expensas_contable["Descripcion"] = np.where(expensas_contable["Concepto"] == "Gasto bancario", "Gasto bancario", 
                                            expensas_contable["Descripcion"])

#-----------------Ordena las tablas---------------------------------------

expensas_banco.drop(["Concepto","seq", "Nro Operacion"], axis = 1, inplace = True)
expensas_banco.sort_values(by=["Consorcio"], inplace = True)
expensas_banco.set_index("Consorcio", inplace = True)


expensas_contable.set_index("Consorcio", inplace = True)
expensas_contable.drop(["seq", "Movimiento", "Mes", "Banco", "Concepto"], axis = 1, inplace = True)
expensas_contable.sort_values(by=["Consorcio"], inplace = True)

#-----------------Exporta a excel el resultado de la conciliacion-------------

expensas_banco.to_excel("C:/Users/Benja/Desktop/expensas_banco.xlsx")
expensas_contable.to_excel("C:/Users/Benja/Desktop/expensas_contable.xlsx")