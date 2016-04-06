import requests
import json


class Headers:
	def __init__(self):
		self.headers = dict()

	def add_header(self, field, value):
		self.headers[field] = value
		

	def remove_header(self, field):
		pass

	def update_header(self, field, value):
		pass

	def set_values(self, field, value):
		pass

	def get_values():
		return self.headers


class Parameters:
	def __init__(self):
		self.params = dict()

	def add_param(self, field, value):
		pass

	def remove_param(self, field):
		pass

	def update_param(self, field, value):
		pass
	
	def set_values(self, field, value):
		pass

	def get_values():
		return self.params


class RestRequests:

	def __init__(self):
		self.requests_list = []

	def get(self, url, proxy=None, headers=None, parameters=None, body=None, to_json=True):
		
		self.requests_list.append(dict(url=url, parameters=parameters, headers=headers))

		try:
			r = requests.get(url, proxy, allow_redirects=False)
			return self.create_response(r, to_json)
			
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


	def create_response(self, response, to_json):
		obj = dict(status_code=response.status_code, headers=response.headers, json=response.json, content_type=response.headers.get('content-type'))
		return obj
		if to_json:
			return json.dumps(obj)
		else:
			return obj

	def get_values(self):
		return self.requests_list
			
		

	#def to_json(self): 
		#return json.dumps(self.requests_list)
		#return "{u'scheme': %r, u'proxyurl': %r}" % (self.scheme.decode('utf-8'),  self.proxyurl.decode('utf-8'))
