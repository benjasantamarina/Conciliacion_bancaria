#Banco Santander Rio
import pandas as pd
import numpy as np
from InicioPrograma import espacios, callback, mm, yy, mm_a

bancos_srio = [82,84, 85,86,87]

srio = pd.DataFrame()

for i in bancos_srio:
    data = pd.read_excel(f"C:/Users/Benja/Desktop/Adiminstracion - Python/Bancos/Conciliaciones bancarias/{yy}/{mm}-{yy}/Archivos entrada/{i}.xlsx")
    data.drop(["Suc. Origen","Desc. Sucursal", "Referencia", "Saldo Pesos"], axis=1, inplace=True)
    data.rename(columns = {"Concepto":"Descripcion","Cod. Operativo":"Nro Operacion","Importe Pesos":"Importe"}, inplace=True)
    data["Consorcio"] = i
    data["Concepto"] = np.where((data["Nro Operacion"] == 4637)|
                                (data["Nro Operacion"] == 4633)|
                                (data["Nro Operacion"] == 4585)|
                                (data["Nro Operacion"] == 3204)|
                                (data["Nro Operacion"] == 434)|
                                (data["Nro Operacion"] == 3000)|
                                (data["Nro Operacion"] == 2960)|
                                (data["Nro Operacion"] == 1922)|
                                (data["Nro Operacion"] == 1924)|
                                (data["Nro Operacion"] == 3253)|
                                (data["Nro Operacion"] == 3254)|
                                (data["Nro Operacion"] == 9633)|
                                (data["Nro Operacion"] == 1923)|
                                (data["Nro Operacion"] == 4757),"Gasto Bancario", 
                       np.where(data["Nro Operacion"] == 267,"Colocacion Plazo Fijo",
                       np.where(data["Nro Operacion"] == 261, "Acreditacion Plazo Fijo",
                       np.where(data["Importe"]>0,"Ingresos", "Egresos"))))
    data["Banco"] = i
    srio = pd.concat([srio, data])
