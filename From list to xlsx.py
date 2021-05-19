test_list = [['Date', 'Company', 'QTY', 'BUY', 'SELL', 'Closing Date', 'DP Applicable?'],
             ['15/12/2020', 'BOROLTD', 10, 196.4, 198.35, '23/04/2021', 'yes'],
             ['21/12/2020', 'ESCORTS', 2, 1301, None, None, None],
             ['22/12/2020', 'ESCORTS', 2, 1230, None, None, None],
             ['24/12/2020', 'ESCORTS', 2, 1245, None, None, None],
             ['28/12/2020', 'ESCORTS', 2, 1245, None, None, None],
             ['31/12/2020', 'BORORENEW', 5, 312.2, None, None, None],
             ['05/01/2021', 'BECTORFOOD', 10, 485.9, None, None, None],
             ['05/01/2021', 'IEX', 10, 221.7, None, None, None],
             ['11/12/2020', 'IRCTC', 2, 1417, None, None, None],
             ['05/01/2021', 'BORORENEW', 10, 284.8, None, None, None],
             ['08/01/2021', 'TOTAL', 25, 80.05, None, None, None],
             ['13/01/2021', 'TOTAL', 5, 68.05, None, None, None],
             ['13/01/2021', 'GLENMARK', 10, 510.1, 513.9, '08/04/2021', 'yes'],
             ['20/01/2021', 'BECTORFOOD', 1, 434.2, None, None, None],
             ['21/12/2020', 'GLENMARK', 4, 502.65, 513.9, '08/04/2021', 'Sold w others'],
             ['21/12/2020', 'GLENMARK', 1, 501.05, 513.9, '08/04/2021', 'Sold w others'],
             ['21/12/2020', 'GLENMARK', 1, 500.1, 513.9, '08/04/2021', 'Sold w others'],
             ['21/12/2020', 'ASIANPAINT', 2, 2742, None, None, None],
             ['21/12/2020', 'ASIANPAINT', 2, 2700, None, None, None],
             ['21/12/2020', 'GRANULES', 5, 340.25, None, None, None],
             ['22/01/2021', 'ASIANPAINT', 2, 2615, None, None, None],
             ['22/01/2021', 'ASIANPAINT', 1, 2592, None, None, None],
             ['25/01/2021', 'ESCORTS', 1, 1245, None, None, None],
             ['25/01/2021', 'ESCORTS', 1, 1225, None, None, None],
             ['27/01/2021', 'ASIANPAINT', 2, 2440, None, None, None],
             ['27/01/2021', 'GLENMARK', 2, 490, 513.9, '08/04/2021', 'Sold w others']]

# import Utils
#
# test_list = Utils.stock_entry()

# To create a new xlsx file from scratch

from openpyxl import Workbook

wb = Workbook()
wb["Sheet"].title = "P&LLL"
sh2 = wb.active
# to write any list of lists to individual points to excel file
column_start = 1
for i in test_list:
    row_start = 1
    for j in i:
        sh2.cell(row=column_start, column=row_start, value=j)
        row_start = row_start + 1
    column_start = column_start + 1
sh2.insert_rows(7)
wb.save("5Python.xlsx")
