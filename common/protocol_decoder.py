"""
 author: Varsha,Ashwini
 date : 11/09/2020
"""

class ProtocolDecoder(object):
    """
     class responsible for decoding the message payload for extracting the desired elements

    """
    string_tokens = []
    def get_decoded_message(self, payload):
            self.string_tokens=str(payload.decode('utf-8')).split("#")
            return self.string_tokens

    def get_machine_id(self):
            return self.string_tokens[0]

    def get_date_time(self):
        return self.string_tokens[1]

    def get_device_type(self):
        return self.string_tokens[2]

    def get_status(self):
       return self.string_tokens[3]

    def get_programme(self):
        return self.string_tokens[3]


