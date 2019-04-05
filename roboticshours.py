import sqlite3
import csv
import os
import datetime

import gui

conn = sqlite3.connect("attendance.db")
c = conn.cursor

data = ('id', 'name')

c.execute('''CREATE TABLE name_ids (?,?)''', data)