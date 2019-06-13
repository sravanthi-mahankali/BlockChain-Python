import binascii

import Crypto
import Crypto.Random
from Crypto.PublicKey import RSA

from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('./index.html')

@app.route('/wallet/new', methods=['GET'])
def new_wallet():

if __name__ == '__main__':
    from argparse import ArgumentParser

    parser = ArgumentParser()
    parser.add_argument('-p', '--port', default=8080, type=int, help='port to listen on')
    args = parser.parse_args()
    port = args.port

    app.run(host='127.0.0.1', port=port)