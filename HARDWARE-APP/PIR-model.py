import RPi.GPIO as GPIO
import requests
import time

GPIO.setmode(GPIO.BCM)

GPIO.setup(23, GPIO.IN) #PIR

API_ENDPOINT = "http://uprcroomavailability.pythonanywhere.com/setRoomStatus"

API_KEY = "8975917845yhiWUEFHYDFU*(#@!$73RYUIAWGDF"

ROOM_NAME = "UPRC Study Room 1"

def getPIRStatus():
    time.sleep(2)
    if GPIO.input(23):
        return '1'
    else:
        return '0'

time.sleep(2)
while True:
    data = {
            'name':ROOM_NAME, 
            'isOccupied':getPIRStatus()}
    print(getPIRStatus())
    #sending post request
    r = requests.get(url = API_ENDPOINT, params = data)
        
    #extract response
    service_url = r.text
    print("The service URL is:%s"%service_url)
    time.sleep(10)
    
