'''
  Created on 29-08-2020
  @author : Femy

'''

from datetime import datetime

# the machine id  and delimiter will be read from a confgurationfile
machineid = "WM_01"
msg_delimiter = "#"

class ProtocolManager(object):
    def __init__(self):
        self.message = ""
        self.datetimestring = ""
        

    def get_datetimestring(self):
        """
           method that retreives the date time in a particular format
           to be appended to the final message string
        """
        current_time = datetime.now()
        self.datetimestring +=current_time.strftime("%d-%b-%Y (%H:%M:%S)")
        return self.datetimestring

    def get_devicename(self,devicetype):
        """
           method will return the device name corresponding to each each device type
           @param devicetype : the device type of the machine requested for message       
        """
        device_name = ""
        if devicetype==1:
            device_name=name=msg_delimiter+"Washing Machine"
        elif devicetype==2:
            device_name=msg_delimiter+"Dryer"
        else:
            device_name=msg_delimiter+"Dish Washer"
        return device_name


    def create_loginmessage(self,devicetype):
        """
           create the login message for the corresponding device instance connected
           to the server
        """
        self.message+=machineid
        self.message+=msg_delimiter+self.get_datetimestring()+self.get_devicename(devicetype)
        print (self.message)

    def create_statusmessage(devicetype):
        pass
    def create_loginresponse(devicetype):
        pass

pm_object = ProtocolManager()
pm_object.create_loginmessage(2)