import xlrd

loc= ("RGBA Werte.xlsx")

wb= xlrd.open_workbook(loc)
sheet=wb.sheet_by_index(0)

for i in range(1,33):
    rgb_werte = [sheet.cell_value(i,1),sheet.cell_value(i,2),sheet.cell_value(i,3)]
    print(rgb_werte)
#Cell_value is setted as (row, columm) 