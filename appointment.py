~ import modules
from tkinter import *
import sqlite3
import tkinter.messagebox
~ connect to the databse.
conn = sqlite3.connect('database.db')
~ cursor to move around the databse
c = conn.cursor()

~ empty list to later append the ids from the database
ids = []

~ tkinter window
class Application:
        def __init__(self, master):
                    self.master = master

                            ~ creating the frames in the master
                                    self.left = Frame(master, width=800, height=720, bg='lightgreen')
                                            self.left.pack(side=LEFT)

                                                    self.right = Frame(master, width=400, height=720, bg='steelblue')
                                                            self.right.pack(side=RIGHT)

                                                                    ~ labels for the window
                                                                            self.heading = Label(self.left, text="STEDAP Hospital Appointments", font=('arial 40 bold'), fg='black', bg='lightgreen')
                                                                                    self.heading.place(x=0, y=0)
                                                                                            ~ patients name
                                                                                                    self.name = Label(self.left, text="Patient's Name", font=('arial 18 bold'), fg='black', bg='lightgreen')
                                                                                                            self.name.place(x=0, y=100)

                                                                                                                    ~ age
                                                                                                                            self.age = Label(self.left, text="Age", font=('arial 18 bold'), fg='black', bg='lightgreen')
                                                                                                                                    self.age.place(x=0, y=140)

                                                                                                                                            ~ gender
                                                                                                                                                    self.gender = Label(self.left, text="Gender", font=('arial 18 bold'), fg='black', bg='lightgreen')
                                                                                                                                                            self.gender.place(x=0, y=180)

                                                                                                                                                                    ~ location
                                                                                                                                                                            self.location = Label(self.left, text="Location", font=('arial 18 bold'), fg='black', bg='lightgreen')
                                                                                                                                                                                    self.location.place(x=0, y=220)

                                                                                                                                                                                            ~ appointment time
                                                                                                                                                                                                    self.time = Label(self.left, text="Appointment Time", font=('arial 18 bold'), fg='black', bg='lightgreen')
                                                                                                                                                                                                            self.time.place(x=0, y=260)

                                                                                                                                                                                                                    ~ phone
                                                                                                                                                                                                                            self.phone = Label(self.left, text="Phone Number", font=('arial 18 bold'), fg='black', bg='lightgreen')
                                                                                                                                                                                                                                    self.phone.place(x=0, y=300)

                                                                                                                                                                                                                                            ~ Entries for all labels============================================================
                                                                                                                                                                                                                                                    self.name_ent = Entry(self.left, width=30)
                                                                                                                                                                                                                                                            self.name_ent.place(x=250, y=100)

                                                                                                                                                                                                                                                                    self.age_ent = Entry(self.left, width=30)
                                                                                                                                                                                                                                                                            self.age_ent.place(x=250, y=140)
                                                                                                                                                                                                                                                                                
                                                                                                                                                                                                                                                                                        self.gender_ent = Entry(self.left, width=30)
                                                                                                                                                                                                                                                                                                self.gender_ent.place(x=250, y=180)

                                                                                                                                                                                                                                                                                                        self.location_ent = Entry(self.left, width=30)
                                                                                                                                                                                                                                                                                                                self.location_ent.place(x=250, y=220)

                                                                                                                                                                                                                                                                                                                        self.time_ent = Entry(self.left, width=30)
                                                                                                                                                                                                                                                                                                                                self.time_ent.place(x=250, y=260)

                                                                                                                                                                                                                                                                                                                                        self.phone_ent = Entry(self.left, width=30)
                                                                                                                                                                                                                                                                                                                                                self.phone_ent.place(x=250, y=300)

                                                                                                                                                                                                                                                                                                                                                        ~ button to perform a command
                                                                                                                                                                                                                                                                                                                                                                self.submit = Button(self.left, text="Add Appointment", width=20, height=2, bg='steelblue', command=self.add_appointment)
                                                                                                                                                                                                                                                                                                                                                                        self.submit.place(x=300, y=340)
                                                                                                                                                                                                                                                                                                                                                                            
                                                                                                                                                                                                                                                                                                                                                                                    ~ getting the number of appointments fixed to view in the log
                                                                                                                                                                                                                                                                                                                                                                                            sql2 = "SELECT ID FROM appointments "
                                                                                                                                                                                                                                                                                                                                                                                                    self.result = c.execute(sql2)
                                                                                                                                                                                                                                                                                                                                                                                                            for self.row in self.result:
                                                                                                                                                                                                                                                                                                                                                                                                                            self.id = self.row[0]
                                                                                                                                                                                                                                                                                                                                                                                                                                        ids.append(self.id)
                                                                                                                                                                                                                                                                                                                                                                                                                                        