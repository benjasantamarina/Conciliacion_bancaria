#Banco ITAU
import pandas as pd
import numpy as np
from InicioPrograma import callback, espacios, mm, yy, mm_a


bancos_itau = [76, 96, 97, 109, 110, 111]

itau = pd.DataFrame()

for i in bancos_itau:
    data = pd.read_table(f"C:/Users/Benja/Desktop/Adiminstracion - Python/Bancos/Conciliaciones bancarias/{yy}/{mm}-{yy}/Archivos entrada/{i}.txt", sep=',')
    col_nombres = list(data.columns.values)
    data.rename(columns = {col_nombres[0]:"Fecha",col_nombres[1]:"Descripcion", col_nombres[2]:"Nro Operacion", col_nombres[3]:"Importe", col_nombres[4]:"Moneda", col_nombres[5]:"Saldo"}, inplace=True)
    #data["Importe"] = data["Importe"].apply(espacios)
    #data["Descripcion"] = data["Descripcion"].apply(espacios)
    data["Importe"] = data["Importe"].astype(float)
    data.drop(["Moneda", "Saldo"], axis=1, inplace=True)
    data["Consorcio"] = i
    data["Banco"] = i
    data["Concepto"] = np.where((data["Descripcion"]=="IMPUESTO -LEY 25413")|
                                (data["Descripcion"]=="IMPUESTO - LEY 25413")|
                                (data["Descripcion"]=="COM. INTERDEP/EXTRAC")|
                                (data["Descripcion"]=="COM. MANT. MENSUAL")|
                                (data["Descripcion"]=="COMIS DEP POR CAJA")|
                                (data["Descripcion"]=="COMISION CLEARING")|
                                (data["Descripcion"]=="IVA 21%")|
                                (data["Descripcion"]=="PER IIBB AGIP 939/13")|
                                (data["Descripcion"]=="COM. EMISION ECHEQ")|
                                (data["Descripcion"]=="COM. VALOR AL COBRO")|
                                (data["Descripcion"]=="COM CML HABERES")|
                                (data["Descripcion"]=="COM DEP CHEQUE")|
                                (data["Descripcion"]=="DEVO IM/CG 25413")|
                                (data["Descripcion"]=="COB IMP/C 25413")|
                                (data["Descripcion"]=="COM. RECH. CH. TERC.")|
                                (data["Descripcion"]=="COM TRANSF. ELECTRON"),"Gasto Bancario",
                       np.where(data["Descripcion"]=="ACREDITACION DE P.F.","Acreditacion Plazo Fijo",
                       np.where(data["Descripcion"]=="PLAZO FIJO -IBE","Colocacion Plazo Fijo",        
                       np.where(data["Importe"]>0,"Ingresos","Egresos"))))
    data = data[["Fecha","Nro Operacion", "Descripcion", "Importe", "Consorcio", "Concepto", "Banco"]]
    itau = pd.concat([itau, data])