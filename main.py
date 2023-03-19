from flask import Flask, request
import requests

app = Flask(__name__)

@app.route('/tilda-webhook', methods=['POST'])
def tilda_webhook():
    data = request.json  # get the data sent by Tilda
    # process the data as needed
    # for example, you can save it to a database or send it to another service
    print(data)
    return 'OK'