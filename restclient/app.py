import requests
from rest_requests import RestRequests, Headers, Parameters
from utils import Proxy, Config
import json
import sys

config = Config()

rest_requests = RestRequests()

def app():

	headers = {"user-agent":"my-app/0.0.1", "Accept":"xml"}
	parameters = {}
	proxy = Proxy()

	do_request(headers, parameters, proxy)
	config.save_settings(proxy, rest_requests)


def do_request(headers, parameters, proxy):
	#headers = Headers()
	#headers.add_header("user-agent", "my-app/0.0.1")
	#params = Parameters()

	proxy.set_values(**dict(scheme="http", proxyurl="proxy.copyright.com.au", port=3218, username="jerasmus", password="Password4"));
	response = rest_requests.get('https://api.github.com/events/', proxy.proxy, headers)


if __name__ == '__main__':
	app()

