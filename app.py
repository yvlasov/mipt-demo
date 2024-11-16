#!/usr/bin/env python3

from flask import Flask
from datetime import datetime
import os

app = Flask(__name__)


@app.route('/')
def hello_world():
    # Get current time
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    app_version = os.getenv('APP_VER', 'Unknown')
    # Return HTML with current time
    return f'''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Hello World</title>
    </head>
    <body>
        <h1>Hello, New Happy DevOps World!</h1>
        <p>Current time: {current_time}</p>
        <p>We use semantic-release</p>
        <p>Version: {app_version}</p>
        <p>New feature</p>
        <p>Minor feature</p>
    </body>
    </html>
    '''


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
