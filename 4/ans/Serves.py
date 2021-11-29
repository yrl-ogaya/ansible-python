from flask import Flask, make_response ,request
import subprocess
from waitress import serve
import sys

# import json
api = Flask(__name__)

#yamlファイルを生成
@api.route('/create', methods=['GET'])
def create():
    print('/createにアクセスがありました。')
    ip = request.args.get('ip')
    subprocess.run(['python3 Convert.py '+ip],shell=True)
    print('yamlファイルが生成しました。')
    return make_response('yamlファイルを作成しました。\n')

#ansibleの実行
@api.route('/ansible', methods=['GET'])
def ansible():
    print('/ansibleにアクセスがありました。')
    subprocess.run(['ansible-playbook main.yaml'],shell=True)
    print('ansibleを実行しました。')
    return make_response('ansibleを実行しました。\n')

if __name__ == '__main__':
    serve(api, host='0.0.0.0', port=3000)