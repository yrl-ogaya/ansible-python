from flask import Flask, make_response ,request
import subprocess
from waitress import serve

# import json
#ver2
api = Flask(__name__)

@api.route('/', methods=['GET'])
def get():
    search = request.args.get("search")
    #email = request.form.get("search")
    print(search)
    result = {
        "result":True,
        "data":{
            "user":"test"
            }
        }
    subprocess.call("dir",shell=True)
    return make_response('アクセス完了')

if __name__ == '__main__':
    serve(api, host='0.0.0.0', port=3000)