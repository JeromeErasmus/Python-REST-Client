import requests
from rest_requests import RestRequests
from utils import Proxy, Config
import json
import sys
from flask import Flask, jsonify, render_template, request

app = Flask(__name__)
app.debug = True
config = Config()
rest_requests = RestRequests()
proxy = Proxy()

def appx():
	proxy.set_values(**dict(scheme="http", proxyurl="proxy.copyright.com.au", port=3218, username="jerasmus", password="Password4"));
	config.save_settings(proxy, rest_requests)


@app.route("/")
def index():
    return render_template('index.html')


#@app.route("/requestx", methods=["POST", "GET"])
#def requestx():
#	headers = {"user-agent":"my-app/0.0.1", "Accept":"xml"}
#	parameters = {}
#	response = rest_requests.get('http://jsonplaceholder.typicode.com/posts/1', proxy.proxy, headers)
	

#	return jsonify(response)

@app.route("/requestsettings", methods=["GET"])
def loaddata():
	print "LOADING DATA..."
	return jsonify(dict(parameters=[dict(name="jerome", value="jerome@gmail"), dict(name="ben", value="ben@gmail")]) )


@app.route("/requestsettings", methods=["POST"])
def savedata():
	print "SAVING DATA..."
	return ""

@app.route("/sendrequest", methods=["POST"])
def send_request():
	print "SENDING DATA..."
	
	if request.method == "POST":
		response = rest_requests.get(request.json['url'], proxy.proxy, request.json["headers"], request.json["parameters"], request.json["body"], request.json["method"])

		#proxy.set_values(**dict(scheme="http", proxyurl="proxy.copyright.com.au", port=3218, username="jerasmus", password="Password4"));
		#config.save_settings(proxy, rest_requests)
		return jsonify(response)
	
@app.route("/getsavedrequests", methods=["POST"])
def get_saved_requests():
	print "SENDING DATA..."



if __name__ == '__main__':
	app.run()





