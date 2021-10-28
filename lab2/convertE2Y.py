import openpyxl
import yaml
import logging
import sys

# Logger名の指定。
logger = logging.getLogger('LoggingTest')

# 標準出力(コンソール)にログを出力するハンドラを生成する
#sh = logging.StreamHandler(sys.stdout)
#sh.setLevel(logging.INFO)

# ハンドラをロガーに紐づける
#logger.addHandler(sh)

# Excel ファイルを指定する
wbook = openpyxl.load_workbook("AnsiblePythonLab.xlsx")

# Excel ファイルのシートリストを取得する
sheets = wbook.sheetnames

# sheet の枚数分繰り返す
for sheet in sheets:
  # 出力ファイルの指定
  yaml_output = open("host_vars/"+ sheet + ".yaml", 'w')


  print("-- Processing : " + sheet + " sheet --")
  sheet = wbook[sheet]
  hostname = sheet["B2"]
  ip = sheet["B3"]
  cider = sheet["B4"]
  gateway = sheet["B5"]
  dns = sheet["B6"]

  out_data = {'hostanme': hostname.value,
              'ip': ip.value,
              'cider': cider.value,
              'gateway': gateway.value,
              'dns': dns.value
             }
  
  # 各シートの情報を yaml に変換して出力
  yaml_output.write(yaml.dump(out_data))
  yaml_output.close()
  
  # yaml出力内容の出力
  logger.info(hostname.value)
  logger.info(ip.value)
  logger.info(cider.value)
  logger.info(gateway.value)
  logger.info(dns.value)
 