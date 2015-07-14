#!/bin/python

# Dependencies:
# pip install flask
# pip install stsplatform
# pip install requests

from flask import Flask, request, session, render_template
import json
import stsplatform.client as sts

app = Flask(__name__)
app.secret_key = '12fdas098234!#@!#TyX R~X@@!$!#!!#%' # something really secret
app.config['SESSION_TYPE'] = 'filesystem'
app.debug = True

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/data', methods=['POST','GET'])
def data():
    if 'key_id' not in session:
        return "You must set your credentials"
    else:
        client = sts.Client({
            'auth':{
                'key_id':session['key_id'],
                'key_password':session['key_password']
                }
            })
        sensor = sts.Sensors(client,session['sensor_name'])
        data = sts.Data(sensor)

        if request.method == 'GET':
            response = data.get({'beforeE':1}).data
            return json.dumps(response)

        if request.method == 'POST':
            value = request.form['value']
            code = data.post({'value':value}).code
            return "Value %s sent to wotkit, received code %d" % (value, code),code

@app.route('/auth', methods=['POST'])
def auth():
    if request.method == 'POST':
        session['key_id'] = request.form['key_id']
        session['key_password'] = request.form['key_password']
        session['sensor_name'] = request.form['sensor_name']
        return "Credentials Set"

if __name__ == "__main__":
    app.run()
