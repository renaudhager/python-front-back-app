import os
import socket
import json

from flask import Flask, request, jsonify

import requests

app = Flask(__name__)

@app.route('/')
def hello():
    provider = str(os.environ.get('PROVIDER', 'world'))
    return 'Hello ' + provider + '!'

@app.route('/backend/a/<path>')
def query_service_a(path):
    service_a_fqdn = str(os.environ.get('SERVICE_A_FQDN'))
    r = requests.get('http://' + service_a_fqdn + "/" + path)
    return jsonify(r.json())

@app.route('/backend/b/<path>')
def query_service_b(path):
    service_b_fqdn = str(os.environ.get('SERVICE_B_FQDN'))
    r = requests.get('http://' + service_b_fqdn + "/" + path)
    return jsonify(r.json())

@app.route("/hostname")
def return_hostname():
    return "This is an example wsgi app served from {} to {}".format(socket.gethostname(), request.remote_addr)

@app.route("/headers")
def return_headers():
    return str(request.headers)

@app.route("/http_code")
def return_http_code():
    code = request.args.get('code', default = 200, type = int)
    return str(code), code

@app.route("/health")
def return_health():
    code = request.args.get('code', default = 200, type = int)
    return "Healthy", 200

if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('CONTAINER_PORT', 5000))
    app.run(host='0.0.0.0', port=port)
