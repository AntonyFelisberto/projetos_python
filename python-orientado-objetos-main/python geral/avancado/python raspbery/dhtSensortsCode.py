import Adafruit_DHT as dht
import time
import requests
while(True):
    h,t=dht.read_retry(11,21)
    print("Temperature",t)
    print("Humidity",h)
    time.sleep(1)
    url="https://api.thingspeak.com/update?api_key=FF2QQAK4DCGGEGMB&field1=%s&field2=%s"%(t,h)
    print(url)
    requests.get(url)
