import pandas as pd
import time
import calendar
from datetime import datetime

atual = "database/final.xlsx"

base = pd.read_excel(atual)

#Transformando Surfaces em números
base = base.replace("Hard", 0)
base = base.replace("Clay", 1)
base = base.replace("Grass", 2)
base = base.replace("Carpet", 3)

#Transformando Comments
n = 0
for i in base['Comment'].unique():
    base = base.replace(i, n)
    n += 1

#Transformando round
n = 0
for i in base['Round'].unique():
    base = base.replace(i, n)
    n += 1

#Transformando data
base = base.astype({"Date": str})

for i in base['Date'].unique():
    k = str(i).replace("-","")
    base = base.replace(i, k)

base = base.astype({"Date": int})
