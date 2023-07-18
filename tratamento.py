import pandas as pd
import time
import calendar
import datetime
from openpyxl import Workbook, load_workbook

atual = "database/final.xlsx"

basepanda = pd.read_excel(atual)

planilha = load_workbook(atual)
aba_ativa = planilha["database"]

