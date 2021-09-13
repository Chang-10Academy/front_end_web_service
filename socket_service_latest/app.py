from flask import Flask, send_from_directory, render_template
from flask_cors import CORS, cross_origin
from flask_socketio import SocketIO, emit
from kafka import KafkaProducer, KafkaConsumer, TopicPartition
import uuid, json
import os, sys

# sys.path.append(os.path.abspath(os.path.join('../scripts')))
# from consumer1 import GetText

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

BOOTSTRAP_SERVERS = 'localhost:9093'
TOPIC_NAME = 'topic0001'


@app.route('/')
@cross_origin()
def home():

    dataRx = get_data()
    # kafkaconsumer()
    return render_template("index.html", datarx=dataRx)

""" Kafka endpoints """


@socketio.on('connect', namespace='/kafka')
def test_connect():
    data = "Ethan connected"
    emit('logs', {'data': data})
    kafkaconsumer()


@socketio.on('kafkaconsumer', namespace="/kafka")
def kafkaconsumer():
    message1 = get_data()
    emit('kafkaconsumer1', message1)


@socketio.on('kafkaproducer', namespace="/kafka")
def kafkaproducer(message):
    print(TOPIC_NAME)
    print(BOOTSTRAP_SERVERS)
    producer = KafkaProducer(bootstrap_servers=BOOTSTRAP_SERVERS, value_serializer=json_serializer)
    producer.send(TOPIC_NAME, {"data":message})
    emit('logs', {'data': 'Added ' + message + ' to topic'})
    emit('kafkaproducer', {'data': message})
    producer.close()
    print("messahe sent", message)
    kafkaconsumer(message)
    print(">>")

def json_serializer(data):
    return json.dumps(data).encode("utf-8")

def get_data():
    message1 = "Refresh the page to get the Translation"
    consumer = KafkaConsumer('topic0001',
                        group_id='my-group5',
                        bootstrap_servers=['localhost:9092'])
    messages = consumer.poll(timeout_ms=1000,max_records=1)

    for tp, mess in messages.items():
        message=mess[0]
        print ("%s:%d:%d: key=%s value=%s" % (tp.topic, tp.partition,
                                            message.offset, message.key,
                                            message.value.decode('utf-8')))

        message1 = message.value.decode('utf-8')

    return message1


if __name__ == '__main__':
    socketio.run(app)