"""
 author :
 date   :
"""
import time


class StatusTimer:
     """
      class that send status to server at particular intervals while the machine is running
     """
     def __init__(self,client, status_message):
        self.publish_client = client
        self.message = status_message

     def send_machine_status(self):
        t_end = time.time() + 1 * 60
        while time.time() < t_end:
            time.sleep(10)
            print(":::sending status to server every 10 sec:::")
            self.publish_client.publish("CLIENT/CURRENT_MACHINE_STATUS", self.message)
        print("\n:::PROGRAMME DONE , please off the machine or select another wash::::")



