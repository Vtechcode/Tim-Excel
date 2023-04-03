from openpyxl import Workbook, load_workbook

wb = Workbook()
ws = wb.active
#Changing the name of the worksheet
ws.title = "Data"

#Writing into an excel file
ws.append(['Tim', 'Is', 'Great', '!'])
ws.append(['Tim', 'Is', 'Great', '!'])
ws.append(['Tim', 'Is', 'Great', '!'])
ws.append(['Tim', 'Is', 'Great', '!'])
ws.append(["end"])

wb.save('tim.xlsx')