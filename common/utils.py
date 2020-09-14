"""
 @ author Femy
 date 07/09/2020
"""
from datetime import datetime


class CommonUtils:

    def get_datetime_as_string(self):
        """
            method returns the string format of date time with a given format
        """
        current_time = datetime.now()
        datetime_string = current_time.strftime("%d-%b-%Y_%H:%M:%S")
        return datetime_string
