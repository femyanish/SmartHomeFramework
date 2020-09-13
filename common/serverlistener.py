"""
  author :
  date  :
"""
import threading
import paho.mqtt.client as paho

from common.status_timer import StatusTimer
from conf.smarthome_config import SmartConfig


class ServerListener:
    """
     class that handles all functions related to subscribing to the related topics and processing the messages/acknowledgements
    """
    def __init__(self):
        self.publish_client = paho.Client
        self.my_config = SmartConfig()
        self.opAck = False

    def connect(self, name):
        listener_client = paho.Client("listener")
        listener_client .connect(self.my_config.get_server_ip(), self.my_config.get_server_port(), 60)
        listener_client .on_message = self.on_server_request
        listener_client .subscribe("SERVER/#")
        listener_client .loop_forever()

    def run(self):
        x = threading.Thread(target=self.connect, args=(1,))
        x.start()

    def on_server_request(self, client, userdata, message):
        print(message.payload)
        if message.topic == self.my_config.get_loginresponse():
            if str(message.payload.decode('utf-8') == "WELCOME-CONNECTED"):
                print(":::Connected to the Server Successfully:::\n")
                self.opAck = True
            else:
                print(":::You seems to be an invalid user:::")

        if message.topic == self.my_config.get_pgmresponse():
            print(":::Selected programme is approved,You can start the programme :::")
            self.opAck = True

        if message.topic == self.my_config.get_statusack():
            print("\n::: MACHINE RUNNING:::")
            StatusTimer(self.publish_client, "Machine running").send_machine_status()  # calling timer class
            self.opAck = True

        if message.topic == self.my_config.get_finishedack():
            self.opAck = True
            client.disconnect()
