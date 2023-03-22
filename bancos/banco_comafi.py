#Banco Comafi
import pandas as pd
import numpy as np
from InicioPrograma import espacios, callback, mm, yy, mm_a

bancos_comafi = [88]

comafi = pd.DataFrame()

for i in bancos_comafi:
    data=pd.read_excel(f"C:/Users/Benja/Desktop/Adiminstracion - Python/Bancos/Conciliaciones bancarias/{yy}/{mm}-{yy}/Archivos entrada/{i}.xlsx")
    data.drop(["Fecha de Carga"], axis = 1, inplace = True)
    data.rename(columns = {"ID Operación": "Nro Operacion", "Descripción":"Descripcion"}, inplace = True)
    data = data[["Fecha","Nro Operacion", "Descripcion", "Importe"]]
    data["Consorcio"] = i
    data["Concepto"] = np.where((data["Descripcion"] == "Imp.débitos tasa general")|
                                (data["Descripcion"] == "Impuesto a los créditos")|
                                (data["Descripcion"] == "Imp.Debs t.gral Art.45 L 27541")|
                                (data["Descripcion"] == "Com.Transf. eBanking")|
                                (data["Descripcion"] == "Comisión Pago de Cheques")|
                                (data["Descripcion"] == "IVA Alícuota General")|
                                (data["Descripcion"] == "Mantenimiento de Cuenta")|
                                (data["Descripcion"] == "Devol. Imp.débitos tasa gral.")|
                                (data["Descripcion"] == "Impuesto a los creditos-tasa general")|
                                (data["Descripcion"] == "Comision emision resumen de cuenta")|
                                (data["Descripcion"] == "Comisión por mantenimiento de cuenta")|
                                (data["Descripcion"] == "Comision transferencias e-Banking")|
                                (data["Descripcion"] == "Impuesto a los debitos - tasa general")|
                                (data["Descripcion"] == "IVA - Alicuota General")|
                                (data["Descripcion"] == "Devol. Imp.débitos tasa gral.")|
                                (data["Descripcion"] == "Resumen de Cuenta"), "Gasto Bancario",
                        np.where(data["Importe"] > 0, "Ingresos", "Egresos"))
    data["Banco"] = i
    comafi = pd.concat([comafi, data])