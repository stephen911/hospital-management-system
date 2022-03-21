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
                                                                    