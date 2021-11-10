from flask import Flask, jsonify, abort, make_response ,request
import subprocess
from waitress import serve

# import json
#ver2
api = Flask(__name__)

@api.route('/Users/test', methods=['GET'])
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
    subprocess.call("dir")
    return make_response(jsonify(result))
@api.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

if __name__ == '__main__':
    serve(api, host='0.0.0.0', port=3000)