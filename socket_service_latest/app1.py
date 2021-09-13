# from flask import Flask, render_template
# from flask_socketio import SocketIO, emit

# app = Flask(__name__)
# app.config['SECRET_KEY'] = 'secret!'
# socketio = SocketIO(app)

# @app.route('/')
# def index():
#     return render_template('index1.html')

# @socketio.on('my event')
# def test_message(message):
#     emit('my response', {'data': message['data']})

# @socketio.on('my broadcast event')
# def test_message(message):
#     emit('my response', {'data': message['data']}, broadcast=True)

# @socketio.on('connect')
# def test_connect():
#     emit('my response', {'data': 'Connected'})

# @socketio.on('disconnect')
# def test_disconnect():
#     print('Client disconnected')

# if __name__ == '__main__':
#     socketio.run(app)


# compose_flask/app.py
# from flask import Flask, render_template
# from flask_socketio import SocketIO, send, emit

# app = Flask(__name__)
# socketio = SocketIO(app)


# @app.route('/')
# def hello():
#     # redis.incr('hits')
#     return render_template('index1.html')


# @socketio.on('message')
# def handle_message(message):
#     send(message)

# @socketio.on('json')
# def handle_json(json):
#     send(json, json=True)

# @socketio.on('my event')
# def handle_my_custom_event(json):
#     emit('my response', json)

# @socketio.on('connect')
# def test_connect():
#     emit('my response', {'data': 'Connected'})


# if __name__ == "__main__":
#     socketio.run(app)

from consumer1 import GetText

data = GetText.get_data()
print(data)