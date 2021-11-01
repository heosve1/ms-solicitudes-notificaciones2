from flask import Flask
from flask import request
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from twilio.rest import Client
import os


app = Flask(__name__)
@app.route("/")
def hello():
    return "hello world"
@app.route("/email")
def enviarCorreo():
    destino = request.args.get("correo_destino")
    asunto = request.args.get("asunto")
    mensaje = request.args.get("mensaje")
    message = Mail(
    from_email='david.1701713821@ucaldas.edu.co',
    to_emails=destino,
    subject=asunto,
    html_content=mensaje)
    try:
        sg = SendGridAPIClient('')
        response = sg.send(message)
        return "OK"
    except Exception as e:
        #print(e.message)
        return "KO"

@app.route("/sms")
def enviarSms():
    destino = request.args.get("destino")
    mensaje = request.args.get("mensaje")
    try:
        account_sid = ""
        auth_token = ""
        client = Client(account_sid, auth_token)

        message = client.messages \
            .create(
                body=mensaje,
                from_="+15342203458",
                to="+"+destino
        )
        print(message.sid)
        print("SMS enviado correctamente")
        return "OK"
    except Exception as e:
        #print(e.message)
        return "KO"

if __name__ == '__main__':
    app.run()

#version con notificaciones por SMS