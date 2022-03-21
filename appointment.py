~ import modules
from tkinter import *
import sqlite3
import tkinter.messagebox
~ connect to the databse.
conn = sqlite3.connect('database.db')
~ cursor to move around the databse
c = conn.cursor()

