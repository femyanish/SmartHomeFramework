'''
    author : Padma
    date   : 11/9/2020
'''
import paho.mqtt.client as paho
from conf.smarthome_config import SmartConfig

class MQTTLib():
    """
      class that handles all functions related to publishing and subscribing
    """
    def __init__(self):
        self. my_config = SmartConfig()


    def create_client(self, client_id):
        return paho.Client(client_id)


    def connect(self, client_id):
        client_id.connect(self.my_config.get_server_ip(), self.my_config.get_server_port(), 60)

    def publish_message(self, publish_client, topic, message):
        publish_client.publish(topic, message)

    def subscribe_to_message(self, subscribe_client, topic, qos):
        subscribe_client.subscribe(topic, qos)






