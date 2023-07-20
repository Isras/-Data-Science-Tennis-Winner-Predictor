import pandas as pd
import time
import calendar
import datetime
from openpyxl import Workbook, load_workbook

atual = "database/final.xlsx"

base = pd.read_excel(atual)

#Transformando Surfaces em números
base = base.replace("Hard", 0)
base = base.replace("Clay", 1)
base = base.replace("Grass", 2)
base = base.replace("Carpet", 3)

# print(type(base['Comment'].unique()))
# for i in base['Comment'].unique():
#     base = base.replace(i, (base['Comment'].unique()).)