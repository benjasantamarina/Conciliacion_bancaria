#Importacion de librerias y creacion de funciones

import pandas as pd
import numpy as np

def espacios (texto):
    a = texto.strip()
    a = a.replace(" ","")
    return a

def callback(x):
    x['seq'] = range(1, x.shape[0] + 1)
    return x


while True:
    mm = input("Mes a conciliar: ")
    
    try:
        aa = int(mm)
        
        if aa < 1 or aa > 12:
            print("Error, debe ingresar un numero entre 1 y 12")
            continue
            
        elif len(mm) != 2:
            print("Error, el formato para ingresar el mes es de 2 digitos, ejemplo mayo = 05")
            continue
            
        else:
            break
    except:
        print("Error, debe ingresar un numero entero")
        continue
        
while True:
    yy = input("Año a conciliar: ")
    
    try:
        bb = int(yy)
        
        if bb < 2000 or bb > 2100:
            print("Error, debe ingresar un año entre 2000 y 2100")
            continue
            
        else:
            break
    except:
        print("Error, ingresar un numero entero")
        continue        
    
mm_a = str(int(mm)-1)



if len(mm_a) < 2:
    mm_a = "0" + mm_a
else:
    pass
