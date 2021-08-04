import os
import glob
import picamera
import RPi.GPIO as GPIO
import time
import smtplib
from subprocess import call

# import gmailwrapper class
from gmailwrapper import gmailwrapper
#from RpiMotorLib import RpiMotorLib

# import modules for sending mail
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.MIMEBase import MIMEBase
from email import encoders

HOSTNAME = 'imap.gmail.com'
USERNAME = 'uafproject2021@gmail.com'
PASSWORD = 'mjteywwhzjddoqme'
sender = USERNAME
password = PASSWORD
receiver = USERNAME

# database for image capture
DIR = './Database/'
FILE_PREFIX = 'image'

# allows user to feed animal via action
def feedByMail():
    #gmailWrapper = gmailwrapper(HOSTNAME, USERNAME, PASSWORD)
    ids = gmailWrapper.getIdsBySubject('feed')
    if(len(ids) > 0):
        try:
            feed()
            gmailWrapper.markAsRead(ids)
        except:
            print("feeding did not work")


def treatByMail():
    #gmailWrapper = gmailwrapper(HOSTNAME, USERNAME, PASSWORD)
    ids = gmailWrapper.getIdsBySubject('treat')
    if(len(ids) > 0):
        try:
            treat()
            gmailWrapper.markAsRead(ids)
        except:
            print("treat launching did not succeed")

# test code to check unread email subject lines and enable a light 
# if email found with subject line 'redLight'
def rlightByMail():
    #gmailWrapper = gmailwrapper(HOSTNAME, USERNAME, PASSWORD)
    ids = gmailWrapper.getIdsBySubject('redLight')
    if(len(ids) > 0):
        try:
            rlight()
            gmailWrapper.markAsRead(ids)
        except:
            print("red light not working")

# test code to check unread email subject lines and enable a light 
# if email found with subject line 'blueLight'
def blightByMail():
    #gmailWrapper = gmailwrapper(HOSTNAME, USERNAME, PASSWORD)
    ids = gmailWrapper.getIdsBySubject('blueLight')
    if(len(ids) > 0):
        try:
            blight()
            gmailWrapper.markAsRead(ids)
        except:
            print("blue light not working")
            
def captureImageByMail():
    ids = gmailWrapper.getIdsBySubject('image-capture')
    if(len(ids) > 0):
        try:
            image_capture()
            gmailWrapper.markAsRead(ids)
        except:
            print("image capture not working")
            
def captureVideoByMail():
    ids = gmailWrapper.getIdsBySubject('video-capture')
    if(len(ids) > 0):
        try:
            call(["python", "video.py"])
            gmailWrapper.markAsRead(ids)
        except:
            print("video capture not working")

# code to run stepper for feed auger
def feed():
    out1 = 13
    out2 = 11
    out3 = 15
    out4 = 12
    
    i=0
    positive=0
    negative=0
    y=0
    
    GPIO.setmode(GPIO.BOARD)
    GPIO.setwarnings(False)
    GPIO.setup(out1,GPIO.OUT)
    GPIO.setup(out2,GPIO.OUT)
    GPIO.setup(out3,GPIO.OUT)
    GPIO.setup(out4,GPIO.OUT)
    
    #while(1):
    GPIO.output(out1,GPIO.LOW)
    GPIO.output(out2,GPIO.LOW)
    GPIO.output(out3,GPIO.LOW)
    GPIO.output(out4,GPIO.LOW)
    
    # the x value determines how long the stepper should turn
    x = 10
    if x>0 and x<=1000:
        for y in range(x,0,-1):
            if negative==1:
                if i==7:
                    i=0
                else:
                    i=i+1
                y=y+2
                negative=0
            positive=1
          #print((x+1)-y)
            if i==0:
                GPIO.output(out1,GPIO.HIGH)
                GPIO.output(out2,GPIO.LOW)
                GPIO.output(out3,GPIO.LOW)
                GPIO.output(out4,GPIO.LOW)
                time.sleep(0.001)
                  #time.sleep(1)
            elif i==1:
                GPIO.output(out1,GPIO.HIGH)
                GPIO.output(out2,GPIO.HIGH)
                GPIO.output(out3,GPIO.LOW)
                GPIO.output(out4,GPIO.LOW)
                time.sleep(0.001)
                  #time.sleep(1)
            elif i==2:  
                GPIO.output(out1,GPIO.LOW)
                GPIO.output(out2,GPIO.HIGH)
                GPIO.output(out3,GPIO.LOW)
                GPIO.output(out4,GPIO.LOW)
                time.sleep(0.001)
                  #time.sleep(1)
            elif i==3:    
                GPIO.output(out1,GPIO.LOW)
                GPIO.output(out2,GPIO.HIGH)
                GPIO.output(out3,GPIO.HIGH)
                GPIO.output(out4,GPIO.LOW)
                time.sleep(0.001)
                  #time.sleep(1)
            elif i==4:  
                GPIO.output(out1,GPIO.LOW)
                GPIO.output(out2,GPIO.LOW)
                GPIO.output(out3,GPIO.HIGH)
                GPIO.output(out4,GPIO.LOW)
                time.sleep(0.001)
                  #time.sleep(1)
            elif i==5:
                GPIO.output(out1,GPIO.LOW)
                GPIO.output(out2,GPIO.LOW)
                GPIO.output(out3,GPIO.HIGH)
                GPIO.output(out4,GPIO.HIGH)
                time.sleep(0.001)
                  #time.sleep(1)
            elif i==6:    
                GPIO.output(out1,GPIO.LOW)
                GPIO.output(out2,GPIO.LOW)
                GPIO.output(out3,GPIO.LOW)
                GPIO.output(out4,GPIO.HIGH)
                time.sleep(0.001)
                  #time.sleep(1)
            elif i==7:    
                GPIO.output(out1,GPIO.HIGH)
                GPIO.output(out2,GPIO.LOW)
                GPIO.output(out3,GPIO.LOW)
                GPIO.output(out4,GPIO.HIGH)
                time.sleep(0.001)
                  #time.sleep(1)
            if i==7:
                i=0
                continue
            i=i+1
    GPIO.cleanup()

    #        

    #GpioPins = [13, 15, 11, 12]
    #mymotortest = RpiMotorLib.BYJMotor("MyMotorOne", "Nema")
    #time.sleep(1)
    #mymotortest.motor_run(GpioPins , 0.001, 512, False, True, "half", .05)
    #GPIO.cleanup()

def treat():
    out1 = 13
    out2 = 11
    out3 = 15
    out4 = 12
    
    i=0
    positive=0
    negative=0
    y=0
    
    GPIO.setmode(GPIO.BOARD)
    GPIO.setwarnings(False)
    GPIO.setup(out1,GPIO.OUT)
    GPIO.setup(out2,GPIO.OUT)
    GPIO.setup(out3,GPIO.OUT)
    GPIO.setup(out4,GPIO.OUT)
    
    #while(1):
    GPIO.output(out1,GPIO.LOW)
    GPIO.output(out2,GPIO.LOW)
    GPIO.output(out3,GPIO.LOW)
    GPIO.output(out4,GPIO.LOW)
    
    # the x value determines how long the stepper should turn
    x = 1000
    if x>0 and x<=1000:
        for y in range(x,0,-1):
            if negative==1:
                if i==7:
                    i=0
                else:
                    i=i+1
                y=y+2
                negative=0
            positive=1
          #print((x+1)-y)
            if i==0:
                GPIO.output(out1,GPIO.HIGH)
                GPIO.output(out2,GPIO.LOW)
                GPIO.output(out3,GPIO.LOW)
                GPIO.output(out4,GPIO.LOW)
                time.sleep(0.001)
                  #time.sleep(1)
            elif i==1:
                GPIO.output(out1,GPIO.HIGH)
                GPIO.output(out2,GPIO.HIGH)
                GPIO.output(out3,GPIO.LOW)
                GPIO.output(out4,GPIO.LOW)
                time.sleep(0.001)
                  #time.sleep(1)
            elif i==2:  
                GPIO.output(out1,GPIO.LOW)
                GPIO.output(out2,GPIO.HIGH)
                GPIO.output(out3,GPIO.LOW)
                GPIO.output(out4,GPIO.LOW)
                time.sleep(0.001)
                  #time.sleep(1)
            elif i==3:    
                GPIO.output(out1,GPIO.LOW)
                GPIO.output(out2,GPIO.HIGH)
                GPIO.output(out3,GPIO.HIGH)
                GPIO.output(out4,GPIO.LOW)
                time.sleep(0.001)
                  #time.sleep(1)
            elif i==4:  
                GPIO.output(out1,GPIO.LOW)
                GPIO.output(out2,GPIO.LOW)
                GPIO.output(out3,GPIO.HIGH)
                GPIO.output(out4,GPIO.LOW)
                time.sleep(0.001)
                  #time.sleep(1)
            elif i==5:
                GPIO.output(out1,GPIO.LOW)
                GPIO.output(out2,GPIO.LOW)
                GPIO.output(out3,GPIO.HIGH)
                GPIO.output(out4,GPIO.HIGH)
                time.sleep(0.001)
                  #time.sleep(1)
            elif i==6:    
                GPIO.output(out1,GPIO.LOW)
                GPIO.output(out2,GPIO.LOW)
                GPIO.output(out3,GPIO.LOW)
                GPIO.output(out4,GPIO.HIGH)
                time.sleep(0.001)
                  #time.sleep(1)
            elif i==7:    
                GPIO.output(out1,GPIO.HIGH)
                GPIO.output(out2,GPIO.LOW)
                GPIO.output(out3,GPIO.LOW)
                GPIO.output(out4,GPIO.HIGH)
                time.sleep(0.001)
                  #time.sleep(1)
            if i==7:
                i=0
                continue
            i=i+1
    GPIO.cleanup()

# test code to turn red light on for 5 seconds
def rlight():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(23, GPIO.OUT)
    GPIO.output(23, GPIO.HIGH)
    time.sleep(5)
    GPIO.output(23, GPIO.LOW)
    GPIO.cleanup()
    
# test code to turn blue light on for 5 seconds
def blight():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(24, GPIO.OUT)
    GPIO.output(24, GPIO.HIGH)
    time.sleep(5)
    GPIO.output(24, GPIO.LOW)
    GPIO.cleanup()
    
def setup():
    # activates button. allows for recording of portion size
    return 0

def image_capture():
    print 'Sending E-Mail'
    # Create the directory if not exists
    if not os.path.exists(DIR):
        os.makedirs(DIR)
    # Find the largest ID of existing images.
    # Start new images after this ID value.
    files = sorted(glob.glob(os.path.join(DIR, FILE_PREFIX + '[0-9][0-9][0-9].jpg')))
    count = 0
    
    if len(files) > 0:
        # Grab the count from the last filename.
        count = int(files[-1][-7:-4])+1

    # Save image to file
    filename = os.path.join(DIR, FILE_PREFIX + '%03d.jpg' % count)
    # Capture the face
    with picamera.PiCamera() as camera:
        pic = camera.capture(filename)
    # Sending mail
    msg = MIMEMultipart()
    msg['From'] = sender
    msg['To'] = receiver
    msg['Subject'] = 'Capture Taken'
    
    body = 'Picture is Attached.'
    msg.attach(MIMEText(body, 'plain'))
    attachment = open(filename, 'rb')
    part = MIMEBase('application', 'octet-stream')
    part.set_payload((attachment).read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', 'attachment; filename= %s' % filename)
    msg.attach(part)
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(sender, password)
    text = msg.as_string()
    server.sendmail(sender, receiver, text)
    server.quit()



    
if __name__ == "__main__":
    gmailWrapper = gmailwrapper(HOSTNAME, USERNAME, PASSWORD)
    while(1):
        feedByMail()
        treatByMail()
        rlightByMail()
        blightByMail()
        captureImageByMail()
        captureVideoByMail()