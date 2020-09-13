"""
 @author : Femy Anish
 date : 02/09/2020
"""

import paho.mqtt.client as paho
import time

from common.serverlistener import ServerListener
from conf.smarthome_config import SmartConfig
from appliances.programme_menu import Programmes
from common.protocol_encoder import ProtocolEncoder


class WashingMachine:
    """
      class that handles all functions related to the home appliance washing machine like connecting to server,
      programme mode selection and handling, publishing messages to server corresponding to the programme selected
    """
    def __init__(self):
        self.config = SmartConfig()
        self.protocol_man = ProtocolEncoder()
        self.command_listener = ServerListener()
        self.command_publisher = paho.Client(self.config.get_client_id())  # to be changed for MQtt Library

    def start(self):
        self.command_listener.run()
        self.command_publisher.connect(self.config.get_server_ip(), self.config.get_server_port())
        self.command_publisher.publish(self.config.get_logintopic(), self.protocol_man.get_login_message())

        while True:
            time.sleep(5)
            if self.command_listener.opAck:
                mode_selected = Programmes().show_washingmachine_menu()
                print("WASHING MACHINE, programme selected:::", mode_selected,"\n")
                if mode_selected != "Machine Off":
                    if mode_selected != "Start":
                        self.command_listener.opAck = False
                        self.command_publisher.publish(self.config .get_pgmselected(),mode_selected)
                    else:
                        self.command_listener.opAck = False
                        self.command_listener.publish_client = self.command_publisher
                        self.command_publisher.publish(self.config .get_machinestatus(), mode_selected)
                else:
                    self.command_listener.opAck = False
                    print(mode_selected,"Machine Off")
                    self.command_publisher.publish(self.config .get_finished(), mode_selected)
                    self.command_publisher.loop_stop()
                    self.command_publisher.disconnect()
                    break

        try:
            self.command_publisher.loop_forever()
        finally:
            self.command_publisher.disconnect()



