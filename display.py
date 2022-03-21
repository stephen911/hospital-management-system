from tkinter import *
import sqlite3
import pyttsx3



~ connection to database
conn = sqlite3.connect('database.db')
c = conn.cursor()

~ empty lists to append later
number = []
