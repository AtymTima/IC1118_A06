import paho.mqtt.client as mqtt
from .models import Event
import json

ID="A06"
mqtt_broker = "ia.ic.polyu.edu.hk"
mqtt_port=1883
mqtt_qos=1
mqtt_topic = "iot/sensor"

def mqtt_on_message(client, userdata, msg):
    d_msg=str(msg.payload.decode("utf-8"))
    iotData=json.loads(d_msg)
    if "node_id" not in iotData:
        return
    if iotData["node_id"] == ID:
        print("Received message on topic %s : %s" %(msg.topic, iotData))
        p=Event(node_id=iotData["node_id"],loc=iotData["loc"],temp=iotData["temp"],hum=iotData["hum"],light=iotData["light"],snd=iotData["snd"])
        p.save()

mqtt_client= mqtt.Client("A06_receiver")
mqtt_client.on_message=mqtt_on_message
mqtt_client.connect(mqtt_broker,mqtt_port)
print("Connect to MQTT broker")
mqtt_client.subscribe(mqtt_topic,mqtt_qos)
mqtt_client.loop_start()