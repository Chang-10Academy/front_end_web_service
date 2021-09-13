# compose_flask/app.py
import asyncio
from flask import Flask, render_template, request, redirect, jsonify
from kafka import KafkaProducer, KafkaConsumer, TopicPartition
from redis import Redis
import os, sys, json


app = Flask(__name__)
redis = Redis(host='redis', port=6379)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == "GET":
        e = ""
        data_received = get_data()
        redis.incr('hits')
        
        return render_template("index.html", 
                                count=redis.incr('hits'), 
                                text_corpus=data_received,
                                debg="e")

    if request.method == "POST":
        data = request.form['dummy_data']
        data_dummy = "Data you sent: > " +str(data)
        
        return redirect("/")


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
    

if __name__ == "__main__":
    app.run(host="0.0.0.0",debug=True, port=5000)