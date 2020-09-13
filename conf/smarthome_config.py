"""
 author : Femy Anish
 date   : 12/09/2020
"""

import configparser
import os


class SmartConfig:
    # A class which is responsible for the confi values
    config = configparser.ConfigParser()

    def __init__(self):
        configFilePath = r'C:\Femy\Learning\Projects\SmartHomeFramework\conf\smarthome.ini'
        self.config.read(configFilePath)

    def get_client_id(self):
        return self.config['device']['id']

    def get_server_ip(self):
        return self.config['mqtt']['server_ip']

    def get_server_port(self):
        return int(self.config['mqtt']['server_port'])

    def get_device_id(self):
        return self.config['device']['id']

    def get_device_type(self):
        return self.config['device']['device_type']

    def get_message_separator(self):
        return self.config['message_delimiter']['separator']

    def get_logintopic(self):
        return self.config['topics']['login']

    def get_loginresponse(self):
        return self.config['topics']['login_response']

    def get_pgmselected(self):
        return self.config['topics']['programme_selected']

    def get_pgmresponse(self):
        return self.config['topics']['programme_ack']

    def get_machinestatus(self):
        return self.config['topics']['machine_status']

    def get_statusack(self):
        return self.config['topics']['status_ack']

    def get_finished(self):
        return self.config['topics']['finished']
    def get_finishedack(self):
        return self.config['topics']['finish_ack']



