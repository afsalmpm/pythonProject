

file_paths = ["C:\\Users\\dell\\Desktop\\", "C:\\Users\\dell\\Desktop\\"]
file = ["P&L Record May 2021.xlsx", "JASI P&L Record May 2021.xlsx"]

for

    with open(file, 'rb') as f:
        file_data = f.read()
        file_name = f.name
    msg.add_attachment(file_data, maintype='spreadsheet', subtype='xlsx', filename=file_name)