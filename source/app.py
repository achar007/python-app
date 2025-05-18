# '/api/v1/details'
# '/api/v1/healthz'

# Importing flask module in the project is mandatory
# An object of Flask class is our WSGI application.
from flask import Flask, jsonify
import datetime, socket

# Flask constructor takes the name of 
# current module (__name__) as argument.
app = Flask(__name__)

# The route() function of the Flask class is a decorator, 
# which tells the application which URL should call 
# the associated function.
@app.route('/api/v1/details')
# ‘/’ URL is bound with hello_world() function.
def details():
    return jsonify({
        'time': datetime.datetime.now(),
        'hostname': socket.gethostname(),
        'message1': "This is my first project in Devops, Hurray! :-)",
        'message2': "Great step for devops !!!!",
        'message3': "adding a line 123456789",
        "message4": "new line"
    })

@app.route('/api/v1/healthz')
# ‘/’ URL is bound with hello_world() function.
def healthz():
    return jsonify({
        'status': 'up'
    }), 200

# main driver function
if __name__ == '__main__':

    # run() method of Flask class runs the application 
    # on the local development server.
    app.run(host='0.0.0.0', port=5000)