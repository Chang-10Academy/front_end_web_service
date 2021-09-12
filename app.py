# compose_flask/app.py
from flask import Flask, render_template, request, redirect
from redis import Redis
import os, sys, json
from kafka import KafkaConsumer

local_boostrap_server_address = 'localhost:9092'

# sys.path.append(os.path.abspath(os.path.join('scripts')))
# from scripts import consumer1

a = 0
try:
    consumer = KafkaConsumer(
                    "topic0001",
                    bootstrap_servers=local_boostrap_server_address,
                    auto_offset_reset='latest',
                    group_id="consumer-group-a")

    a=1

except:
    a = 0

app = Flask(__name__)
redis = Redis(host='redis', port=6379)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == "GET":
        e = ""
        data_received = get_text_corpus
        redis.incr('hits')
        
        return render_template("index.html", 
                                count=redis.get('hits'), 
                                text_corpus=data_received,
                                debg="e")

    if request.method == "POST":
        data = request.form['dummy_data']
        data_dummy = "Data you sent: > " +str(data)
        
        return redirect("/")

def get_text_corpus():
    global a, consumer
    if (a==1):
        print("starting the consumer")
        for msg in consumer:
            data_received = json.loads(msg.value)
            break


    else:
        try:
            consumer = KafkaConsumer(
                            "topic0001",
                            bootstrap_servers=local_boostrap_server_address,
                            auto_offset_reset='latest',
                            group_id="consumer-group-a")

            a=1

            print("starting the consumer")
            for msg in consumer:
                data_received = json.loads(msg.value)
                break

        except:
            data_received = "Refresh the page to get a Text"

    return data_received

if __name__ == "__main__":
    app.run(host="0.0.0.0",debug=True)