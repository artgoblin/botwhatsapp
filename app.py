from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

from utils import fetch_reply 

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World!"

@app.route("/sms", methods=['POST'])
def sms_reply():
    """Respond to incoming calls with a simple text message."""
    # Fetch the message
    msg = request.form.get('Body')
    phone_no=request.form.get('From')
    
   
    if msg=="who" :
        reply = artgoblin()
        
    if msg=="meeting-links":
        reply=meetinglinks()
        
    if msg=="attendance-links":
        reply=attendancelinks()
        
    if msg=="show-routine":
        reply="https://drive.google.com/file/d/1579vCDJgsE3tQVfDbbXXX7ZtM2_tO_xr/view?usp=sharing"
        
    if msg=="funn-time":
        reply="https://www.instagram.com/"
        
    else:
        reply= fetch_reply(msg,phone_no)

    # Create reply
    resp = MessagingResponse()
    resp.message(reply)

    return str(resp)

def meetinglinks():
    meetings="meeting links\n\n" \
    "1>*analogue ECE-494 lab(abhijit and bholanath sir)*=https://us04web.zoom.us/j/6182151842?pwd=VFczNVVWKzVHQmdEYXh0VUltL1k4UT09\n"\
    "2>*analogue ECE-404 theory(abhijit sir)*=https://us04web.zoom.us/j/6182151842?pwd=VFczNVVWKzVHQmdEYXh0VUltL1k4UT09\n"\
    "3>*digital ECE-403 theory(moupali ma'am)*=https://zoom.us/j/9939445614?pwd=ZFZ4ZkprU3V6eXdSQU5VMGtwNytjdz09\n"\
    "4>*digital ECE-493 lab(moupali ma'am and atunu sir)*=https://docs.google.com/forms/d/e/1FAIpQLSeSFjZTw71l4-kKSbcWsXa7SPa08y0LqskxttrCFCHzG7cirA/viewform?usp=sf_link\n"
    "5>*signals and systems ECE-401 (pronob sir)*=https://us02web.zoom.us/j/9695083521 \n"
    return meetings


def attendancelinks():
    attendance="attendance links\n\n\n"\
    "1>*electronics devices and ckt(surojit sir)*=https://forms.gle/rad9YeTFwJPEyoEu7\n\n"\
    "2>*digital ECE-403 theory(moupali ma'am)*=https://docs.google.com/forms/d/e/1FAIpQLSep79lE8_oG2HgfI0TVEnCwEEl96drlQoF7D8BpvSPJthubBw/viewform?usp=sf_link\n\n"\
    "3>*digital ECE-493 lab(moupali ma'am and atunu sir)*=https://docs.google.com/forms/d/e/1FAIpQLSeSFjZTw71l4-kKSbcWsXa7SPa08y0LqskxttrCFCHzG7cirA/viewform?usp=sf_link\n\n"
    return attendance 
           


def artgoblin():
    artgoblin="this is artgoblin's work"
    return artgoblin

if __name__ == "__main__":
    app.run()

