#Movimientos bancarios del sistema
from InicioPrograma import callback, espacios, yy, mm, mm_a
import numpy as np
import pandas as pd

edificios = [76, 82, 83, 84, 85, 86, 87, 88, 89, 90, 96, 97, 98, 99, 109, 110, 111]
#edificios = [76, 89, 96, 97, 98, 99, 109, 110, 111]
#edificios = [82, 83, 84, 85, 86, 87, 88, 90]

banco_contable = pd.DataFrame()

for i in edificios:
    try:
        contable = pd.read_excel(f"C:/Users/Benja/Desktop/Adiminstracion - Python/Bancos/Conciliaciones bancarias/{yy}/{mm}-{yy}/Archivos entrada/MovimientosBancarios {i}.xls")
    except:
        continue
    else:
        col_nombres = list(contable.columns.values)
        contable.rename(columns = {col_nombres[4]:"Fecha",col_nombres[5]:"Movimiento",col_nombres[6]:"Referencia",col_nombres[9]:"Credito",col_nombres[10]:"Debito",col_nombres[11]:"Saldo",col_nombres[21]:"Mes",col_nombres[29]:"Consorcio",col_nombres[30]:"Banco"}, inplace=True)
        contable.drop(["Unnamed: 0","Unnamed: 1", "Unnamed: 2","Unnamed: 3","Unnamed: 7", "Unnamed: 8", "Unnamed: 12","Unnamed: 12", "Unnamed: 13", "Unnamed: 14","Unnamed: 15","Unnamed: 16","Unnamed: 17", "Unnamed: 18","Unnamed: 19","Unnamed: 20","Unnamed: 22","Unnamed: 23", "Unnamed: 24","Unnamed: 25", "Unnamed: 26","Unnamed: 27", "Unnamed: 27", "Unnamed: 28","Unnamed: 31"], axis=1, inplace=True)
        contable = contable.fillna(0)
        contable["Importe"]=np.where(contable["Credito"]>0,contable["Credito"],(contable["Debito"]*(-1)))
        contable.drop(["Credito","Debito","Saldo"], axis=1, inplace=True)
        contable["Consorcio"] = i
        banco_contable = pd.concat([banco_contable, contable])
    

banco_contable = banco_contable.groupby(['Importe', 'Consorcio']).apply(callback)
banco_contable["Concatenado"] = banco_contable["Consorcio"].astype("str") + banco_contable["Importe"].astype("str") + banco_contable["seq"].astype("str")
banco_contable.set_index("Concatenado", inplace=True)
