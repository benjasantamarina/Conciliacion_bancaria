#Banco HSBC
import pandas as pd
import numpy as np
from InicioPrograma import espacios, callback, mm, yy, mm_a

bancos_hsbc = [89, 99]

hsbc = pd.DataFrame()

for i in bancos_hsbc:
    data = pd.read_csv(f"C:/Users/Benja/Desktop/Adiminstracion - Python/Bancos/Conciliaciones bancarias/{yy}/{mm}-{yy}/Archivos entrada/{i}.csv", sep=",")
    data = data.fillna(0)
    data["Importe"]=np.where(data["Débito"]<0,data["Débito"],data["Crédito"])
    data.drop(["Comprobante","Débito", "Crédito", "Descripción Completa", "movDesc2", "movDesc3"], axis=1, inplace=True)
    data.rename(columns = {"Tipo operación":"Nro Operacion","Descripción":"Descripcion"}, inplace=True)
    data["Consorcio"]=i
    data["Concepto"] = np.where((data["Descripcion"]=="IVA")|
                                (data["Descripcion"]=="I.V.A.")|
                                (data["Descripcion"]=="COMISION MANT.CTA")|
                                (data["Descripcion"]=="COMISION MOV CLEARING")|
                                (data["Descripcion"]=="COMISIONES")|
                                (data["Descripcion"]=="COM USO CAJERO AUTOM")|
                                (data["Descripcion"]=="COM.GESTION COBRO CH")|
                                (data["Descripcion"]=="ANULACION I LEY 25.413")|
                                (data["Descripcion"]=="COM OP INTERSUCURSAL")|
                                (data["Descripcion"]=="COM.POR EXTRACCIONES")|
                                (data["Descripcion"]=="INTERES SALDO DEUDOR")|
                                (data["Descripcion"]=="SELLADO")|
                                (data["Descripcion"]=="COMISION POR CHEQUERA")|
                                (data["Descripcion"]=="CIERRE DE CUENTA")|
                                (data["Descripcion"]=="COM ORDEN NO PAG CHEQ")|
                                (data["Descripcion"]=="IMP. LEY 25.413"),"Gasto Bancario",
                       np.where(data["Descripcion"]=="PLAZO FIJO CRED. CTA.", "Acreditacion Plazo Fijo",
                       np.where(data["Importe"]>0,"Ingresos", "Egresos")))
    data["Banco"] = i
    hsbc = pd.concat([hsbc, data])
