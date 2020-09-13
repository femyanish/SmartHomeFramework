"""
 @author : Femy
 date    : 07/09/1020
"""

from appliances.washingmachine.washing_machine import WashingMachine as ws


class SmartHomeMain():
    """
       This is the main class for the entire Smart Home Project
       The user can select which machine needs to be run based on the menu given which will be redirected
       to the corresponding start method of the selected machine.
    """

    def start_machine(self):
        """
          method to display menu of machines available to run.Based on the menu selected
          the call is redirected to the corresponding machines start method
        """
        print("\n\nWhich machine you like to run:::")
        ans = True
        while ans:
            print("""
            1.Washing Machine
            2.Dryer
            3.Dishwasher            
            """)
            ans = input("Which machine you like to run:::")
            if ans == "1":
                self.start_washing_machine()
                break
            if ans == "2":
                print("\n service not  yet available.,please select only washing machine for now ,Thank you")
                continue
            if ans == "3":
                print("\n service not  yet available.,please select only washing machine for now ,Thank you")
                continue

    @staticmethod
    def start_washing_machine():
        ws().start()


smHome = SmartHomeMain()
smHome.start_machine()
