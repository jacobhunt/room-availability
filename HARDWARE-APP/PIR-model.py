import RPi.GPIO as GPIO
import requests

GPIO.setmode(GPIO.BCM)

GPIO.setup(23, GPIO.IN) #PIR

API_ENDPOINT = "http://uprcroomavailability.pythonanywhere.com/setRoomStatus"

API_KEY = "8975917845yhiWUEFHYDFU*(#@!$73RYUIAWGDF"

ROOM_NAME = "UPRC Study Room 1"

try:
    while True:
        data = {'api_dev_key':API_KEY,
                'api_status':getPIRStatus()
                'api_room_name':ROOM_NAME}
        #sending post request
        r = requests.pst(url = API_ENDPOINT, data = data)
        
        #extract response
        service_url = r.text
        print("The service URL is:%s"%service_url)
        
except:
    GPIO.cleanup()
    
def getPIRStatus():
    time.sleep(2)
    if GPIO.input(23):
        return "1"
    else:
        return "0"