from flask import Flask, request
import requests
import random
from twilio.twiml.messaging_response import MessagingResponse

from utils import fetch_reply 
from links import replya
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
    # Create reply
    resp = MessagingResponse()
    mss=resp.message()
    responded=False
   
    if msg=="who" :
        mss.body(artgoblin())
        responded = True
    elif msg=="//help":
        mss.body(helpaa())
        responded = True
    elif msg=="Meeting-links":
        mss.body(meetinglinks())
        responded = True
    elif msg=="Attendance-links":
        mss.body(attendancelinks())
        responded = True
    elif msg=="Show-routine":
        mss.body(rou())
        responded = True
    elif msg=="//syl":
        mss.body(syl())
        responded = True
        
    elif msg=="Funn-time":
       
       mss.body(fun())
       responded = True
       
    elif msg=="meet":
        
        mss.body((replya()))
        responded = True
    elif msg=="memes":
          r = requests.get('https://www.reddit.com/r/memes/top.json?limit=20?t=day', headers = {'User-agent': 'your bot 0.1'})
            
          if r.status_code == 200:
                data = r.json()
                memes = data['data']['children']
                random_meme = random.choice(memes)
                meme_data = random_meme['data']
                title = meme_data['title']
                image = meme_data['url']
                mss.body(title)
                mss.media(image)
          responded = True
    
        
    elif msg=="sextonine":
        mss.body(forbidden())
        responded = True

    else:
        reply= fetch_reply(msg,phone_no)
        mss.body(reply)
        responded = True

    
    return str(resp)


def syl():
    sl="https://drive.google.com/file/d/1-x6N3b3rIOZerBF_q08DXl8XFXqJ5h9d/view?usp=sharing"
    return sl

def rou():
    r="https://drive.google.com/file/d/1579vCDJgsE3tQVfDbbXXX7ZtM2_tO_xr/view?usp=sharing"
    return r


def meetinglinks():
    meet="meeting links\n\n" \
    "1>*analogue ECE-494 lab(abhijit and bholanath sir)*=https://us04web.zoom.us/j/6182151842?pwd=VFczNVVWKzVHQmdEYXh0VUltL1k4UT09\n"\
    "2>*analogue ECE-404 theory(abhijit sir)*=https://us04web.zoom.us/j/6182151842?pwd=VFczNVVWKzVHQmdEYXh0VUltL1k4UT09\n"\
    "3>*digital ECE-403 theory(moupali ma'am)*=https://zoom.us/j/9939445614?pwd=ZFZ4ZkprU3V6eXdSQU5VMGtwNytjdz09\n"\
    "4>*signals and systems ECE-401 (pronob sir)*=https://us02web.zoom.us/j/9695083521 \n"
    return meet


def attendancelinks():
    atten="attendance links\n\n\n"\
    "1>*electronics devices and ckt(surojit sir)*=https://forms.gle/rad9YeTFwJPEyoEu7\n\n"\
    "2>*digital ECE-403 theory(moupali ma'am)*=https://docs.google.com/forms/d/e/1FAIpQLSep79lE8_oG2HgfI0TVEnCwEEl96drlQoF7D8BpvSPJthubBw/viewform?usp=sf_link\n\n"\
    "3>*digital ECE-493 lab(moupali ma'am and atunu sir)*=https://docs.google.com/forms/d/e/1FAIpQLSeSFjZTw71l4-kKSbcWsXa7SPa08y0LqskxttrCFCHzG7cirA/viewform?usp=sf_link\n\n"\
    "4>*signal and systems (pronob hazra sir)*=https://docs.google.com/forms/d/e/1FAIpQLSdD8ba9rG5EImu7QMleTh2FCS7vXRV7Ce2n-ZMYud-ZdTP7Tw/viewform?usp=sf_link"
    return atten
       
def helpaa():
    hel="all commands that you should know-\n\n"\
    "1>To get all meeting links-(Meeting-links)\n"\
    "2>To get all attendance links-(Attendance-links)\n"\
    "3>To relax-(Funn-time)\n"\
    "4>To get the routine-(Show-routine)\n"\
    "5>To get random jokes- just mention the word jokes in your sentance or say (yes)\n"\
    "6>To get the link of syllabus-(//syl)\n"\
    "7>To generate new meeting link-(meet)\n"\
    "8>To get random memes-(memes)\n"\
    "have a great day thanks for using and also there are many secrets ....have fun discovering them ;-)....."
    return hel
def fun():
    funt="https://www.instagram.com/\n\n"\
    "https://www.facebook.com/\n\n"\
    "https://www.youtube.com/"
    return funt

def forbidden():
    lol="xhamster7.desi/videos/supergirl-multiple-squirts-with-fuck-machine-on-webcam-xhnNuRZ\n"\
    "https://www.xxxhdporno.net/porn-video/12700/hot-xxnx-com/\n"\
    "https://www.pornhat.one/sites/brazzers/\n"\
    "https://beeg.porn/site/pornhub/\n"\
    "https://brattysisters.com/\n"\
    "https://in.letmejerk6.com/se/big-bangbros\n"\
    "https://xhamster7.desi/videos/red-teamer-markus-hired-for-state-sponsored-anal-pen-test-9016713\n"\
    "https://xhamster7.desi/videos/kinky-euro-babe-leanne-gets-doggystyle-banged-after-deepthroat-xh4mIlw\n"\
    "sleep tight"
    return lol
   
        
def artgoblin():
    artgoblin="this is artgoblin's work"
    return artgoblin

if __name__ == "__main__":
    app.run()
