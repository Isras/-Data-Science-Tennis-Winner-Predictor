import pandas as pd
import time
import calendar
import datetime
from openpyxl import Workbook, load_workbook

atual = "database/final.xlsx"

basepanda = pd.read_excel(atual)

lista_surfaces = []

for i in basepanda.Surface.unique():
    lista_surfaces.append(i)

for i in basepanda["Surface"]:
    print(i)