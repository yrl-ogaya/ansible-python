import openpyxl

# Excel ファイルを指定する
wbook = openpyxl.load_workbook("lab2/AnsiblePythonLab.xlsx")

# Excel ファイルのシートリストを取得する
sheets = wbook.sheetnames


print(sheets)