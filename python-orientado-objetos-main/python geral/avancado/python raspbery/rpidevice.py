from awscrt import io, mqtt, auth, http
from awsiot import mqtt_connection_builder
import time as time
import json
import Adafruit_DHT as dht
# Define ENDPOINT, CLIENT_ID, PATH_TO_CERT, PATH_TO_KEY, PATH_TO_ROOT, MESSAGE, TOPIC, and RANGE
ENDPOINT = "a3vm########.iot.us-east-1.amazonaws.com" #replace with your endpoint
CLIENT_ID = "rpiDevice"
PATH_TO_CERT = "certificate.pem.crt" #certificate file path
PATH_TO_KEY = "private.pem.key"#private key file path
PATH_TO_ROOT = "AmazonRootCA1.pem" #root ca certificate file path
TOPIC = "iotdata"#iot topic

# Spin up resources
event_loop_group = io.EventLoopGroup(1)
host_resolver = io.DefaultHostResolver(event_loop_group)
client_bootstrap = io.ClientBootstrap(event_loop_group, host_resolver)
mqtt_connection = mqtt_connection_builder.mtls_from_path(
            endpoint=ENDPOINT,
            cert_filepath=PATH_TO_CERT,
            pri_key_filepath=PATH_TO_KEY,
            client_bootstrap=client_bootstrap,
            ca_filepath=PATH_TO_ROOT,
            client_id=CLIENT_ID,
            clean_session=False,
            keep_alive_secs=6
            )
print("Connecting to {} with client ID '{}'...".format(
        ENDPOINT, CLIENT_ID))
# Make the connect() call
connect_future = mqtt_connection.connect()
# Future.result() waits until a result is available
connect_future.result()
print("Connected!")
# Publish message to server desired number of times.
print('Begin Publish')
while(True):
    h,t=dht.read_retry(11,21) #sensor data pin is connceted to 21 (GPIO Numbering)
    print("Temperature is {} and Humidity is {}".format(t,h))
    message = {"id" : "Rpi_Device","Temperature":t,"Humidity":h}
    mqtt_connection.publish(topic=TOPIC, payload=json.dumps(message), qos=mqtt.QoS.AT_LEAST_ONCE)
    print("Published: '" + json.dumps(message) + "' to the topic: " + "'iotdata'")
    time.sleep(1)
print('Publish End')
disconnect_future = mqtt_connection.disconnect()
disconnect_future.result()

