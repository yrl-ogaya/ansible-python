#4-1で作成したプログラムを実行してください

#ansibleの実行
@api.route('/ansible', methods=['GET'])
def ansible():
    print('/ansibleにアクセスがありました。')
    #subprocessを使いansibleを実行してください。

    print('ansibleを実行しました。')
    return make_response('ansibleを実行しました。')

if __name__ == '__main__':
    serve(api, host='0.0.0.0', port=3000)