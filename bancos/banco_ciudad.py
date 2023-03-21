#Banco ciudad
import pandas as pd
import numpy as np
from InicioPrograma import espacios, callback, yy, mm, mm_a

bancos_ciudad = [83, 90]

ciudad = pd.DataFrame()

for i in bancos_ciudad:
    data=pd.read_excel(f"C:/Users/Benja/Desktop/Adiminstracion - Python/Bancos/Conciliaciones bancarias/{yy}/{mm}-{yy}/Archivos entrada/{i}.xlsx")
    data.rename(columns = {"Monto":"Importe", "N° de comprobante":"Nro Operacion", "Descripción":"Descripcion"}, inplace=True)
    data["Consorcio"] = i
    data["Concepto"] = np.where((data["Descripcion"] == "L25413CRED- LEY 25413 CREDITOS")|
                                (data["Descripcion"] == "L25413DEBI- LEY 25413DEBITOS")|
                                (data["Descripcion"] == "IMPADIGEMP- IMP. LEY 25.413 DEB. ADICIONAL LEY 27.541"), "Gasto Bancario",
                       np.where(data["Descripcion"] == "DEBITPFIJO- DEBITO PLAZO FIJO EXENTO", "Colocacion Plazo Fijo",
                       np.where(data["Descripcion"] == "ACREDPFIJO- ACREDITACION PLAZO FIJO", "Acreditacion Plazo Fijo",
                       np.where(data["Descripcion"] == "INT. PFIJO- INTERES PLAZO FIJO EXENTO", "Intereses Plazo Fijo",
                       np.where(data["Importe"]>0,"Ingresos", "Egresos")))))
    data["Banco"] = i
    ciudad = pd.concat([ciudad, data])
    
