# compose_flask/app.py
from flask import Flask, render_template, request, redirect
from redis import Redis
import os, sys

sys.path.append(os.path.abspath(os.path.join('scripts')))
from scripts import consumer1

app = Flask(__name__)
redis = Redis(host='redis', port=6379)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == "GET":
        e = ""
        data_received = consumer1.get_text_corpus
        redis.incr('hits')
        
        return render_template("index.html", 
                                count=redis.get('hits'), 
                                text_corpus=data_received,
                                debg="e")

    if request.method == "POST":
        data = request.form['dummy_data']
        data_dummy = "Data you sent: > " +str(data)
        
        return redirect("/")


if __name__ == "__main__":
    app.run(host="0.0.0.0",debug=True)