~ update the appointments
from tkinter import *
import tkinter.messagebox 
import sqlite3

conn = sqlite3.connect('database.db')
c = conn.cursor()

class Application:
        def __init__(self, master):
                    self.master = master
                            ~ heading label
                                    self.heading = Label(master, text="Update Appointments",  fg='steelblue', font=('arial 40 bold'))
                                            self.heading.place(x=150, y=0)

                                                    ~ search criteria -->name 
                                                            self.name = Label(master, text="Enter Patient's Name", font=('arial 18 bold'))
                                                            