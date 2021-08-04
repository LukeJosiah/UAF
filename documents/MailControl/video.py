from picamera import PiCamera
from email.mime.multipart import MIMEMultipart
from subprocess import call 
import os
import email.mime.application
import datetime
import smtplib
from time import sleep

camera = PiCamera()

# email information
from_email_addr = 'uafproject2021@gmail.com'
from_email_password = 'mjteywwhzjddoqme'
to_email_addr = 'uafproject2021@gmail.com'

# # video record
def convert(file_h264, file_mp4):
    # Record a 5 second video.
    #camera.rotation = 180
    camera.start_recording(file_h264)
    sleep(5)
    camera.stop_recording()
    print("Rasp_Pi => Video Recorded! \r\n")
    # Convert the h264 format to the mp4 format.
    command = "MP4Box -add " + file_h264 + " " + file_mp4
    call([command], shell=True)
    print("\r\nRasp_Pi => Video Converted! \r\n")
# camera.resolution = (640,480)
# camera.rotation = 180
# camera.start_recording('alert_video.h264')
# camera.wait_recording(15)
# camera.stop_recording()
# 
# # converting video from .h264 to .mp4
# command = "MP4Box -add " + alert_video.h264 + " " + alert_video.mp4
# call([command], shell=True)
convert('/home/pi/Documents/MailControl/alert_video.h264', '/home/pi/Documents/MailControl/Database/alert_video.mp4')
print("video converted")

# create the Message
msg = MIMEMultipart()
msg[ 'Subject'] = 'video captured'
msg['From'] = from_email_addr
msg['To'] = to_email_addr

# video attachment
Captured = '/home/pi/Documents/MailControl/Database/alert_video.mp4'
fp=open(Captured,'rb')
att = email.mime.application.MIMEApplication(fp.read(),_subtype=".mp4")
fp.close()
att.add_header('Content-Disposition','attachment',filename='video' + datetime.datetime.now().strftime('%Y-%m-%d%H:%M:%S') + '.mp4')
msg.attach(att)

# remove unnecessary files
os.remove("/home/pi/Documents/MailControl/alert_video.h264")

# rename video file using appropriate timestamp
os.rename('./Database/alert_video.mp4', datetime.datetime.now().strftime('%Y-%m-%d%H:%M:%S') + '.mp4')

#send Mail
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(from_email_addr, from_email_password)
server.sendmail(from_email_addr, to_email_addr, msg.as_string())
server.quit()