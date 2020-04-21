from flask import Flask, jsonify, render_template, request
from flask_socketio import SocketIO, send, emit
import string
import random

DEBUG = True

app = Flask(__name__)
app.host = '0.0.0.0'
app.debug = True
socketio = SocketIO(app, cors_allowed_origins='*')

class Client:
    def __init__(self, sid):
        self.sid = sid
        self.connected = True

    def emit(self, event, data):
        socketio.emit(event, data, room=self.sid)

class Instance:
    def __init__(self, base_sid):
        self.base_client = Client(base_sid)
        self.instance_code = ''.join(random.choices(string.ascii_uppercase, k=4))
        self.controllers = []
        self.base_client.emit('get_code', self.instance_code)
    def newController(self, controller_sid, index):
        controller = Client(controller_sid)
        controller.emit('get_index', index)
        self.controllers.append(controller)

instances = []

@app.route('/', methods=['GET', 'POST'])

def index():
    if request.method == 'GET':
        print('server connect')
    if request.method == 'POST':
        for i in instances:
            if i.instance_code == request.form['code']:
                i.base_client.emit('action', 'Connect')
    return render_template('index.html')

@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify('pong!')

@socketio.on('create_instance')
def createInstance():
    instances.append(Instance(request.sid))
    print(instances[0].instance_code)

@socketio.on('add_controller')
def addController(code):
    for i, inst in enumerate(instances):
        if inst.instance_code == code:
            inst.newController(request.sid, i)
            inst.base_client.emit('new_controller', request.sid)


@socketio.on('action')
def action(data):
    index = data['index']
    act = data['act']
    instances[index].base_client.emit('action', act)
    print(act)
if __name__== '__main__':
    socketio.run(app)