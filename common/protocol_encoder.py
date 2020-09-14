"""
@ author : Varsha Nizampure,Ashwini
date : 10/9/2020
"""

from common.utils import CommonUtils
from conf.smarthome_config import SmartConfig


class ProtocolEncoder(object):
    """
     class to handle all the encoding of messages for publishing in  a particular format
    """
    my_config = SmartConfig()
    my_utils = CommonUtils()

    def create_base_message(self):
        message = self.my_config.get_device_id()
        message += self.my_config.get_message_separator()
        message += self.my_utils.get_datetime_as_string()
        message += self.my_config.get_message_separator()
        message += self.my_config.get_device_type()
        return message


    def get_login_message(self):
        """
        function to formulate the login message
        """
        message = self.create_base_message()
        return message

    def get_status_message(self, status):
        """
            function to formulate the status message
            status can on,off ,machine running
        """
        message = self.create_base_message()
        message += self.my_config.get_message_separator()
        message += status
        return message

    # added method for programme selected message
    def get_programme_selected(self,programme):
        """
             function to formulate the programme selected message
        """
        message = self.create_base_message()
        message += self.my_config.get_message_separator()
        message += programme
        return message
