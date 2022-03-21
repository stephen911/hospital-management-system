~ update the appointments
from tkinter import *
import tkinter.messagebox 
import sqlite3

conn = sqlite3.connect('database.db')
c = conn.cursor()

