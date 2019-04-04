import xlrd

loc= ("RGBA Werte.xlsx")

wb= xlrd.open_workbook(loc)
sheet=wb.sheet_by_index(0)

print(sheet.cell_value(0,3))
#Cell_value is seted as (row, columm) 