"""
 author : Femy Anish
 date   : 02/09/2020
"""

import paho.mqtt.client as mqtt
from conf.smarthome_config import SmartConfig

class SmartHomeServer(mqtt.Client):
    """
       class that handles all server related activities like subscribing to client topics and procseeing the
       messages and   sending the acknowledgements accordingly
    """
    my_conf = SmartConfig()

    def on_message(self, mqttc, obj, msg):
        print(msg.topic+"->"+str(msg.payload.decode('utf-8')))
        if msg.topic == self.my_conf.get_logintopic() :
            string_tokens=str(msg.payload.decode('utf-8')).split("#")
            machine_id = string_tokens[0]
            print("New Machine %s has been requesting to connect::",machine_id )
            valid_machine = self.my_conf.get_client_id()
            if machine_id == valid_machine:
                self.publish(self.my_conf.get_loginresponse(),"WELCOME-CONNECTED")
            else:
                self.publish(self.my_conf.get_loginresponse(),"INVALID")

        if msg.topic == self.my_conf.get_pgmselected():
            print("Server sending approval for programme selected")
            self.publish(self.my_conf.get_pgmresponse(), "OPERATION APPPROVED")

        if msg.topic == self.my_conf.get_machinestatus():
            print("Server sending approval for status ")
            self.publish(self.my_conf.get_statusack(), "STATUS APPPROVED")

        if msg.topic == self.my_conf.get_finished():
            print("server sending approval for programme done")
            self.publish(self.my_conf.get_finishedack(), "GOOD BYE ,INVOICE WILL BE MAILED")


    def start(self):
        self.connect("localhost", 1883, 60)
        self.subscribe("CLIENT/#", 0)

        rc = 0
        while rc == 0:
            rc = self.loop()
        return rc


smServer = SmartHomeServer()
rc = smServer.start()

print("rc: "+str(rc))