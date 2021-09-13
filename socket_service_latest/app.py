from flask import Flask, send_from_directory, render_template
from flask_cors import CORS, cross_origin
from flask_socketio import SocketIO, emit
from kafka import KafkaProducer, KafkaConsumer, TopicPartition
import uuid, json
import os, sys

# sys.path.append(os.path.abspath(os.path.join('../scripts')))
from consumer1 import GetText

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
    
    return render_template("index.html", datarx=dataRx)

""" Kafka endpoints """


@socketio.on('connect', namespace='/kafka')
def test_connect():
    data = "Ethan connected"
    emit('logs', {'data': data})
    # kafkaconsumer()
    dataRx = dataRx = get_data()
    emit('logs', dataRx)


@socketio.on('kafkaconsumer', namespace="/kafka")
def kafkaconsumer():
    message = "Mimi"
    emit('kafkaconsumer', {'data': '????'})

    consumer = KafkaConsumer(
                             bootstrap_servers=BOOTSTRAP_SERVERS,
                             group_id="consumer-group-a",
                             enable_auto_commit = True,
                             request_timeout_ms = 11000,
                             consumer_timeout_ms=2000
                             )

    tp = TopicPartition(TOPIC_NAME, 0)
    # register to the topic
    print ("msg")
    consumer.assign([tp])

    # obtain the last offset value
    consumer.seek_to_end(tp)
    lastOffset = consumer.position(tp)
    consumer.seek_to_beginning(tp)
    emit('kafkaconsumer1', {'data': '>>>'})
    for message in consumer:
        emit('kafkaconsumer', {'data': message})
        if message.offset == lastOffset - 1:
            break
    consumer.close()


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
        data_received = "nothing here"
        consumer = KafkaConsumer(
                                "topic0001",
                                bootstrap_servers=BOOTSTRAP_SERVERS,
                                auto_offset_reset='latest',
                                enable_auto_commit = True,
                                consumer_timeout_ms=2000,
                                group_id="consumer-group-a")

        print("starting the consumer")
        for msg in consumer:
            data_received = json.loads(msg.value)
            print('data_received')
            print(data_received)
            break

        return data_received

if __name__ == '__main__':
    socketio.run(app)