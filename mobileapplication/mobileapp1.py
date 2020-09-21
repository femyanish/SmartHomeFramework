from tkinter import *
import tkinter as tk
from PIL import ImageTk,Image
from appliances.programme_menu import programmes

root = Tk()
root.title('Python Mobile Simulator')
root.geometry('{}x{}'.format(460, 300))

class Application(tk.Frame):

    def __init__(self, master):
       super().__init__(master)
       self.master = master
       self.imgfile()
       self.main_containers()


    # create all of the main containers
    def main_containers(self):
        self.selected_pgm = programmes().show_program_menu()

        self.top_frame = Frame(root, bg='plum2', width=450, height=50, pady=3)
        self.center = Frame(root, bg='plum2', width=50, height=40, padx=3, pady=3)

        # layout all of the main containers
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)

        #grid to show frames in the output using grid
        self.top_frame.grid(row=0, sticky="ew")
        self.center.grid(row=1, sticky="nsew")

        # create the widgets for the top frame
        self.model_label = Label(self.top_frame, text='Online Devices', background='cyan', width = 25, height = 2, font=("Arial", 10, "bold"))

        # layout the widgets in the top frame
        self.model_label.grid(row=0, columnspan=3)

        self.ctr_north_south1 = Frame(self.center, bg='dodger blue', width=250, height=190)
        self.ctr_ns_lbl1 = Label(self.center, text='List of Devices\nwith Status\n(Online/Offline)', font = ("Arial", 20, "bold")).grid(row=0, column=0, padx=10, pady=2)

        self.ctr_north_east2 = Frame(self.center, bg='yellow', width=200, height=70, padx=3, pady=3)
        self.ctr_ne_lbl2 = Label(self.ctr_north_east2, text="Remaining Time", font=("Arial", 15, "bold")).grid(row=1, column=0, padx=10, pady=2)

        self.ctr_west3 = Frame(self.center, bg='blue violet', width=200, height=70, padx=3, pady=3)
        self.ctr_w_lbl3 = Label(self.center, text="Selected Program :", font=("Arial", 15, "bold")).grid(row=0, column=1, sticky="w", padx=10, pady=2)
        self.ctr_w_lbl4 = Label(self.center, text= self.selected_pgm, font=("Arial", 5, "bold")).grid(row=1, column=1, sticky="ne", padx=10, pady=2)

        self.ctr_west_south4 = Frame(self.center, bg='lime green', width=200, height=70, padx=3, pady=3)
        self.ctr_ws_lbl4 = Label(self.center, text="Invoice Balance", font=("Arial", 15, "bold")).grid(row=0, column=1, sticky="ws", padx=10, pady=2)

        self.ctr_north_south1.grid(row=0, column=0, sticky="ns")
        self.ctr_north_east2.grid(row=0, column=1, sticky="ne")
        self.ctr_west3.grid(row=0, column=1, sticky="w")

        self.ctr_west_south4.grid(row=0, column=1, sticky="ws")

    def imgfile(self):
        self.canvas = Canvas(self.master, width=70, height=50)
        self.canvas.pack()
        self.img = ImageTk.PhotoImage(Image.open("C:/Users/jobs4/Desktop/homeapp.jpg"))
        self.canvas.create_image(20, 20, anchor=NW, image=self.img)
        self.canvas.place(x=250, y=0)


app = Application(root)
root.mainloop()

