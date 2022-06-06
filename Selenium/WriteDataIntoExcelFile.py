import openpyxl

file = "C:\\Users\\P N Babu\\Desktop\\demo.xlsx"
workbook = openpyxl.load_workbook(file)
sheet3 = workbook['Sheet3']
"""To store same data into all the rows and columns"""
# for r in range(1,6):
#     for c in range(1,4):
#         sheet3.cell(r,c).value = "welcome"
#
# workbook.save(file)



"""To store multiple data into rows and columns"""
data =[('Emp Id', 'Emp Name', 'Designation'),
       (1, 'XYZ', 'Manager'),
       (2, 'ABC', 'Consultant')]
for i in data:
    sheet3.append(i)

workbook.save(file)