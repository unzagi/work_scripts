import xlrd
import sys
from collections import defaultdict
result = defaultdict(list)
workbook = xlrd.open_workbook(r"C:\Users\sbrooks\Downloads\SxGfL VirginMedia Connections.xlsx")
worksheet = workbook.sheet_by_name(workbook.sheet_names()[1])

headers = worksheet.row(0)
for index in range(worksheet.nrows)[1:]:
    try:
        for header, col in zip(headers, worksheet.row(index)):
            result[header.value].append(col.value)
    except:
        print (sys.exc_info())

print (result)

