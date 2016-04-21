import requests
import json

class RestRequests:

	def __init__(self):
		self.requests_list = []

	def get(self, url, proxy=None, headers=None, parameters=None, body=None, method="GET", to_json=True):
		
		self.requests_list.append(dict(url=url, parameters=parameters, headers=headers, body=body))

		try:
			if method == "GET":
				r = requests.get(url, proxy)
			elif method == "POST":
				r = requests.POST(url, proxy, data={}, allow_redirects=False)
			elif method == "PUT":
				pass
			elif method == "PATCH":
				pass
			elif method == "DELETE":
				pass
			return self.create_response(r)
			
		except requests.exceptions.Timeout:
			return False
			# Maybe set up for a retry, or continue in a retry loop
		except requests.exceptions.TooManyRedirects:
			return False
			# Tell the user their URL was bad and try a different one
		except requests.exceptions.RequestException as e:
			# catastrophic error. bail.
			print e
			return False


	def create_response(self, response):
		headers = {}
		response_text = response.text

		for header in response.headers:
			headers[header] = response.headers[header]

		if response.status_code == 200:
			success = True
		else:
			success = False

		if "application/json" in response.headers.get("Content-Type"):
			response_text = json.loads(response_text)
		
		obj = dict(status_code=response.status_code,  response=response_text, headers=headers, format="json", success=success)
		return obj

	def get_values(self):
		return self.requests_list
			
		

	#def to_json(self): 
		#return json.dumps(self.requests_list)
		#return "{u'scheme': %r, u'proxyurl': %r}" % (self.scheme.decode('utf-8'),  self.proxyurl.decode('utf-8'))
