from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

from utils import fetch_reply 
from utils1.1 import reply_music
app = Flask(__name__)

@app.route("/")
def hello():
    return "ARTGOBLIN!"

@app.route("/sms", methods=['POST'])
def sms_reply():
    """Respond to incoming calls with a simple text message."""
    # Fetch the message
    msg = request.form.get('Body')
    phone_no=request.form.get('From')
    
   
    if msg=="who" :
        reply = artgoblin()
    
    elif msg=="//help":
        reply=helpaa()
        
    elif msg=="Meeting-links":
        reply=meetinglinks()
        
    elif msg=="Attendance-links":
        reply=attendancelinks()
        
    elif msg=="Show-routine":
        reply="https://drive.google.com/file/d/1579vCDJgsE3tQVfDbbXXX7ZtM2_tO_xr/view?usp=sharing"
    
    elif msg=="//syl":
        reply="https://drive.google.com/file/d/1-x6N3b3rIOZerBF_q08DXl8XFXqJ5h9d/view?usp=sharing"
        
    elif msg=="Funn-time":
        reply= reply_music(msg,phone_no)
        
    else:
        reply= fetch_reply(msg,phone_no)

    # Create reply
    resp = MessagingResponse()
    resp.message(reply)

    return str(resp)

def meetinglinks():
    meet="meeting links\n\n" \
    "1>*analogue ECE-494 lab(abhijit and bholanath sir)*=https://us04web.zoom.us/j/6182151842?pwd=VFczNVVWKzVHQmdEYXh0VUltL1k4UT09\n"\
    "2>*analogue ECE-404 theory(abhijit sir)*=https://us04web.zoom.us/j/6182151842?pwd=VFczNVVWKzVHQmdEYXh0VUltL1k4UT09\n"\
    "3>*digital ECE-403 theory(moupali ma'am)*=https://zoom.us/j/9939445614?pwd=ZFZ4ZkprU3V6eXdSQU5VMGtwNytjdz09\n"\
    "4>*digital ECE-493 lab(moupali ma'am and atunu sir)*=https://docs.google.com/forms/d/e/1FAIpQLSeSFjZTw71l4-kKSbcWsXa7SPa08y0LqskxttrCFCHzG7cirA/viewform?usp=sf_link\n"
    "5>*signals and systems ECE-401 (pronob sir)*=https://us02web.zoom.us/j/9695083521 \n"
    return meet


def attendancelinks():
    atten="attendance links\n\n\n"\
    "1>*electronics devices and ckt(surojit sir)*=https://forms.gle/rad9YeTFwJPEyoEu7\n\n"\
    "2>*digital ECE-403 theory(moupali ma'am)*=https://docs.google.com/forms/d/e/1FAIpQLSep79lE8_oG2HgfI0TVEnCwEEl96drlQoF7D8BpvSPJthubBw/viewform?usp=sf_link\n\n"\
    "3>*digital ECE-493 lab(moupali ma'am and atunu sir)*=https://docs.google.com/forms/d/e/1FAIpQLSeSFjZTw71l4-kKSbcWsXa7SPa08y0LqskxttrCFCHzG7cirA/viewform?usp=sf_link\n\n"
    return atten
       
def helpaa():
    hel="all commands that you should know-\n\n"\
    "1>To get all meeting links-(Meeting-links)\n"\
    "2>To get all attendance links-(Attendance-links)\n"\
    "3>To relax-(Funn-time)\n"\
    "4>To get the routine-(Show-routine)\n"\
    "5>To get random jokes- just mention the word jokes in your sentance or say (yes)\n"\
    "6>To get the link of syllabus-(//syl)\n"\
    "have a great day thanks for using and also there are many secrets ....have fun discovering them ;-)....."
    return hel

def artgoblin():
    artgoblin="this is artgoblin's work"
    return artgoblin

if __name__ == "__main__":
    app.run()

