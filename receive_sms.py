import os
from flask import Flask, request, redirect, send_from_directory
from twilio.twiml.messaging_response import MessagingResponse, Message

app = Flask(__name__, static_url_path='')

@app.route("/sms", methods=['GET', 'POST'])
def sms_reply():
        resp = MessagingResponse()
        msg = Message().body("Here is the schedule").media("https://47940283.ngrok.io/get_image")
        resp.append(msg)
        return str(resp)


@app.route('/get_image')
def get_image():
    return send_from_directory('', 'sampleprospect.png')

if __name__ == "__main__":
    app.run(debug=True)
