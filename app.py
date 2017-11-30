from flask import Flask
import socket
app = Flask(__name__)

@app.route('/')
def index():
	return "My hotname is "+ str(socket.gethostbyname_ex(socket.gethostname()))
