#Banco Provincia
import numpy as np
import pandas as pd
from InicioPrograma import espacios, callback, yy, mm, mm_a

bancos_provincia = [98]

provincia = pd.DataFrame()

for i in bancos_provincia:
    data = pd.read_excel(f"C:/Users/Benja/Desktop/Adiminstracion - Python/Bancos/Conciliaciones bancarias/{yy}/{mm}-{yy}/Archivos entrada/{i}.xlsx")
    data.drop(["Saldo"], axis=1, inplace=True)
    data.rename(columns = {"Descripción":"Descripcion"}, inplace=True)
    data["Consorcio"] = i
    data["Nro Operacion"] = ""
    data["Concepto"] = np.where((data["Descripcion"] == "LEY 27541 - IMPUESTO PAIS")|
                                (data["Descripcion"] == "DB IMPUESTO RG4815")|
                                (data["Descripcion"] == "ANSES SIPA")|
                                (data["Descripcion"] == "DEBITO COMPRA ME")|
                                (data["Descripcion"] == "PAGO LIQUIDACION VISA")|
                                (data["Descripcion"] == "RENTAS.CDAD.BSA RE.PF2022026005211 ID.022411031370")|
                                (data["Descripcion"] == "CR. SAC/HSEX/OTROS"),"HS",
                       np.where(data["Importe"]>0, "Ingresos", "Egresos"))
    data["Banco"] = i
    data = data[["Fecha","Nro Operacion", "Descripcion", "Importe", "Consorcio", "Concepto", "Banco"]]
    provincia = pd.concat([provincia, data])