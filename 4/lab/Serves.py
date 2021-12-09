#4-1で作成したプログラムの実行
def create():
    subprocess.run(['python3 Convert.py '],shell=True)


#ansibleの実行
@api.route('/ansible', methods=['GET'])
def ansible():
    print('/ansibleにアクセスがありました。')
    subprocess.run(['ansible-playbook main.yaml'],shell=True)
    print('ansibleを実行しました。')
    return make_response('ansibleを実行しました。')
