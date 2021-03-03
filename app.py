import os
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

from selenium import webdriver 


from utils import fetch_reply 
op = webdriver.ChromeOption()
op.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
op.add_argument("--headless")
op.add_argument("--disable-dev-sh-usage")
op.add_argument("--no-sandbox")

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
       
       reply="https://www.instagram.com/\n\n"\
       "https://www.facebook.com/\n\n"\
       "https://www.youtube.com/"
   
    elif msg=="Gmeet":
        
    driver = webdriver.Chrome(executable_path= os.environ.get("CHROMEDRIVER_PATH", chromeoptions=op)
    driver.implicitly_wait(20)
    driver.get("https://meet.google.com/")

    #clicking the meeting tabs
    Tosignin=driver.find_element_by_css_selector('#page-content > section.module-hero.glue-mod-spacer-6-top.glue-mod-spacer-6-bottom.hero > div > div:nth-child(1) > div.primary-meet-cta.hero-cta > div > a > button')
    Tosignin.click()
    driver.implicitly_wait(10)

    #to sign in
    password = "s1234DAS2000"
    l= "projectsmail768@gmail.com"
    driver.find_element_by_xpath('//*[@id="identifierId"]').send_keys(email)
    driver.find_element_by_id('identifierNext').click()

    driver.find_element_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input').send_keys(password)
    driver.find_element_by_xpath('//*[@id="passwordNext"]/div/button/div[2]').click()

    driver.find_element_by_xpath('//*[@id="yDmH0d"]/div[3]/div/div[2]/div[3]/div/span/span').click()

    reply=driver.current_url
    


    
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
    "7>To generate random meeting links-Gmeet"
    "have a great day thanks for using and also there are many secrets ....have fun discovering them ;-)....."
    return hel


def artgoblin():
    artgoblin="this is artgoblin's work"
    return artgoblin




if __name__ == "__main__":
    app.run()

