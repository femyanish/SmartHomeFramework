"""
 @author : Femy Anish
 date : 07/09/2020
"""


class Programmes:
    """
      class displays  all programme menu related to the corresponding home appliances
    """
    def __init__(self):
        self.menu = ""

    def show_washingmachine_menu(self):
        ans = True
        while ans:
            print("""
            Programs Available
            1.Daily Wash
            2.Cotton Wash
            3.Eco wash
            4.Start
            0.Machine Off
            """)
            ans = input("What would you like to do? ")
            if ans == "1":
                print("\n Daily Wash Selected")
                menu ="Daily Wash"
                break
            elif ans == "2":
                print("\n Cotton Wash Selected")
                menu = "Cotton Wash"
                break
            elif ans == "3":
                print("\n Starting The selected program")
                menu = "Eco Wash"
                break
            elif ans == "4":
                print("\n Starting The selected program")
                menu = "Start"
                break
            elif ans == "0":
                menu = "Machine Off"
                break
                # Now inform the server that the washing is done
            elif ans != "":
                print("\n Not Valid Choice Try again")
                continue
            menu =ans
        return menu
