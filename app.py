from flask import Flask, render_template, request
from pymysql import connections
import os
import random
import argparse
import time

app = Flask(__name__)  # Fix: Use double underscores around 'name'

# Environment configuration
DBHOST = os.environ.get("DBHOST") or "localhost"
DBUSER = os.environ.get("DBUSER") or "root"
DBPWD = os.environ.get("DBPWD") or "rootpassword"
DATABASE = os.environ.get("DATABASE") or "employees"
COLOR_FROM_ENV = os.environ.get('APP_COLOR') or "lime"
DBPORT = os.environ.get("DBPORT")
if DBPORT is not None:
    try:
        DBPORT = int(DBPORT)
    except ValueError:
        print("Invalid value for DBPORT. Using default port 3306.")
        DBPORT = 3306
else:
    DBPORT = 3306

# Supported color codes
color_codes = {
    "red": "#e74c3c",
    "green": "#16a085",
    "blue": "#89CFF0",
    "blue2": "#30336b",
    "pink": "#f4c2c2",
    "darkblue": "#130f40",
    "lime": "#C1FF9C",
}

# Supported colors string
SUPPORTED_COLORS = ",".join(color_codes.keys())

# Random color selection
COLOR = random.choice(list(color_codes.keys()))

# Function to connect to the database with retry logic
def connect_to_database(attempts=5, delay=5):
    while attempts > 0:
        try:
            conn = connections.Connection(
                host=DBHOST,
                port=DBPORT,
                user=DBUSER,
                password=DBPWD,
                db=DATABASE
            )
            return conn
        except Exception as e:
            print(f"Failed to connect to the database, retrying in {delay} seconds...")
            time.sleep(delay)
            attempts -= 1
    raise Exception("Could not connect to the database after several attempts")

# Initialize database connection
db_conn = connect_to_database()

# Define your Flask route handlers here...
# For example:
@app.route("/", methods=['GET', 'POST'])
def home():
    return render_template('addemp.html', color=color_codes[COLOR])

# ... rest of your route handlers ...

if __name__ == '__main__':  # Fix: Use double underscores around 'name'
    # Command line argument for color
    parser = argparse.ArgumentParser()
    parser.add_argument('--color', required=False)
    args = parser.parse_args()

    if args.color:
        print(f"Color from command line argument = {args.color}")
        COLOR = args.color.lower()
        if COLOR_FROM_ENV:
            print(f"A color was set through the environment variable - {COLOR_FROM_ENV}. However, color from the command line argument takes precedence.")
    elif COLOR_FROM_ENV:
        print(f"No Command line argument. Color from the environment variable = {COLOR_FROM_ENV}")
        COLOR = COLOR_FROM_ENV.lower()
    else:
        print(f"No command line argument or environment variable. Picking a Random Color = {COLOR}")

    # Check if input color is a supported one
    if COLOR not in color_codes:
        print(f"Color not supported. Received '{COLOR}' expected one of {SUPPORTED_COLORS}")
        exit(1)

    # Run the Flask app
    app.run(host='0.0.0.0', port=8080, debug=False)
