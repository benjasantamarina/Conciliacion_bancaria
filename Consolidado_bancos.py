#Consolidado de bancos

import pandas as pd
import numpy as pd
from InicioPrograma import callback
from banco_ciudad import ciudad
from banco_comafi import comafi
from banco_HSBC import hsbc
from banco_itau import itau
from banco_provincia import provincia
from banco_santander import srio


consolidado_bancos = pd.concat([itau, hsbc, srio, provincia, ciudad, comafi])
#consolidado_bancos = pd.concat([itau, hsbc, provincia])
#consolidado_bancos = pd.concat([srio, ciudad, comafi])
expensas_banco = consolidado_bancos
expensas_banco = expensas_banco[(expensas_banco["Concepto"] != "Gasto Bancario")]
expensas_banco = expensas_banco.groupby(['Importe', 'Consorcio']).apply(callback)
expensas_banco["Concatenado"] = expensas_banco["Consorcio"].astype("str") + expensas_banco["Importe"].astype("str") + expensas_banco["seq"].astype("str")