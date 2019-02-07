from flask import Flask
from flask import render_template
import sqlite3
import csv

conn = sqlite3.connect('timetracker.db')
d = conn.cursor
app = Flask(__name__)

@app.route('/home')
def home():


def create_table_input():
    try:
        cursor.execute('''CREATE TABLE input (first_name string, last_name string, timestamp int, in_out boolean)''')
    except Exception as e: print(e)

def input_to_hours():
    try:
        cursor.execute('''''')
    except Exception as e: print(e)

def delete_input_table():
    try:
        cursor.execute('''''')
    except Exception as e: print(e)

def create_table_hours():
    try:
        cursor.execute('''CREATE TABLE hours (first_name string, last_name string, hours int)''')
    except Exception as e: print(e)

def insert_hours():
    try:
        cursor.execute('''INSERT INTO hours (first_name, last_name, hours)
                            VALUES (?,?,?)''', (hours_stuff))
    except Exception as e: print(e)