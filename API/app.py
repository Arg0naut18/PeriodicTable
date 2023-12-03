from flask import Flask, jsonify, Response
from flask_cors import CORS
import pandas as pd
from mongo_connector import Connector


app = Flask(__name__)
CORS(app)
collection = Connector()

data = pd.DataFrame(collection.get_data())

METHOD_NOT_ALLOWED = "Method not allowed!"
DOES_NOT_EXIST = "Does not exist!"
MIMETYPE = 'application/json'

def get_data(field_in_dataset, element):
    if data[field_in_dataset].str.contains(element).sum()==0:
        return jsonify(message=DOES_NOT_EXIST, status=404)
    return Response(data.loc[data[field_in_dataset]==element].to_json(indent=4, orient='records'), mimetype=MIMETYPE)

@app.route('/')
def home():
    return Response(data.to_json(indent=4, orient='records'), mimetype=MIMETYPE)

@app.route('/element/atomicnumber/<int:atomic_number>')
def atomicnumber(atomic_number):
    if atomic_number not in range(1, 119):
        return jsonify(message=DOES_NOT_EXIST, status=404)
    return Response(data.loc[[atomic_number-1]].to_json(indent=4, orient='records'), mimetype=MIMETYPE)

@app.route('/element/atomicname/<string:atomic_name>')
def atomicname(atomic_name):
    return get_data('name', atomic_name)

@app.route('/element/symbol/<string:symbol>')
def atomicsymbol(symbol):
    return get_data('symbol', symbol)

@app.route('/elements/groupblock/<string:block>')
def atomicgroupblock(block):
    return get_data('groupblock', block)

@app.route('/elements/bondingtype/<string:bonding_type>')
def atomicbondingtype(bonding_type):
    return get_data('bondingType', bonding_type)

@app.route('/elements/state/<string:state>')
def atomicstate(state):
    return get_data('standardState', state)


if __name__ == '__main__':
    app.run(port=80,debug=True)
