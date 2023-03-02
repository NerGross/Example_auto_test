from openpyxl import load_workbook
from random import choices, choice
from datetime import datetime

import config

wb = load_workbook("valid.xlsx")
sheet = wb.active

current_day = datetime.now()
VIN = choices(config.str_vin, k=17)
reg_nim = (choices(config.str_rus, k=1)) + (choices(config.str_number, k=3)) + (choices(config.str_rus, k=2)) + (
    choices(config.str_number, k=3))
inn = 1
kpp = 2
num = ("00{:02}{:02}".format(current_day.day, current_day.month))

sheet['B4'] = inn
sheet['C4'] = kpp
sheet['I4'] = "".join(VIN)
sheet['L4'] = "".join(reg_nim)
sheet['S4'] = num

wb.save("valid.xlsx")

