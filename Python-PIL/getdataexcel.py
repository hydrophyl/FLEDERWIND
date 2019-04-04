import xlrd

loc= ("RGB_level_190130.xlsx")

wb= xlrd.open_workbook(loc)
sheet=wb.sheet_by_index(0)

sheet.cell_value(12,13)

print(sheet.cell_value(12,13))
