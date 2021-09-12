# compose_flask/app.py
import asyncio
from flask import Flask, render_template, request, redirect, jsonify
from flask_cors import CORS
from redis import Redis
import os, sys, json


sys.path.append(os.path.abspath(os.path.join('scripts')))
from consumer1 import GetText


app = Flask(__name__)
redis = Redis(host='redis', port=6379)

@app.route('/', methods=['GET', 'POST'])
async def home():
    if request.method == "GET":
        e = ""
        data_received = await GetText.get_text_corpus()
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
    app.run(host="0.0.0.0",debug=True, port=5003)