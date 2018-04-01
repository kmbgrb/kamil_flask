from flask import Flask
import socket
app = Flask(__name__)

@app.route('/')
def index():
	return "My hostname is "+ str(socket.gethostbyname_ex(socket.gethostname()))
