from tkinter import *
import sqlite3
import pyttsx3



~ connection to database
conn = sqlite3.connect('database.db')
c = conn.cursor()

~ empty lists to append later
number = []
patients = []

sql = "SELECT * FROM appointments"
res = c.execute(sql)
for r in res:
        ids = r[0]
            name = r[1]
                number.append(ids)
                    patients.append(name)
                        print(ids, name)

                        ~ window
                        class Application:
                                def __init__(self, master):
                                            self.master = master

                                                    self.x = 0
                                                            
                                                                    ~ heading
                                                                            self.heading = Label(master, text="Appointments", font=('arial 60 bold'), fg='green')
                                                                                    self.heading.place(x=350, y=0)

                                                                                            ~ button to change patients
                                                                                                    self.change = Button(master, text="Next Patient", width=25, height=2, bg='steelblue', command=self.func)
                                                                                                            self.change.place(x=500, y=600)

                                                                                                                    ~ empty text labels to later config
                                                                                                                            self.n = Label(master, text="", font=('arial 200 bold'))
                                                                                                                                    self.n.place(x=500, y=100)

                                                                                                                                            self.pname = Label(master, text="", font=('arial 80 bold'))
                                                                                                                                                    self.pname.place(x=350, y=400)
                                                                                                                                                        ~ function to speak the text and update the text
                                                                                                                                                            def func(self):
                                                                                                                                                                        self.n.config(text=str(number[self.x]))
                                                                                                                                                                        