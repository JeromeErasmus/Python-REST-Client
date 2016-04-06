import json

class Proxy():
    def __init__(self):
        self.proxy = dict()
        pass

    def set_values(self, scheme, proxyurl, port=None, username=None, password=None):
        self.scheme = scheme
        self.proxyurl = proxyurl
        self.port = port
        self.username = username
        self.password = password

        if username != None and password != None:
            pstr = '{0}://{1}:{2}@{3}'.format(scheme, username, password, proxyurl)
        else:
            pstr = '{0}://{1}'.format(scheme, proxyurl)

        if port != None:
            pstr = pstr + ':{0}/'.format(port)
        else:
            pstr = pstr + '/'

        if scheme == "http":
            self.proxy = dict(http=pstr)
        elif scheme == "https":
            self.proxy = dict(https=pstr)
    
    def get_values(self):
        return dict(scheme=self.scheme, proxyurl=self.proxyurl, port=self.port, username=self.username, password=self.password)


    #def to_json(self): 
        #return json.dumps(self.get_values())


class Config():
	def __init__(self):
		self.config = dict(proxy=None, request=None)

	def save_settings(self, proxy_obj, rest_requests):
		self.config = dict(proxy=proxy_obj.get_values(), requests=rest_requests.get_values())

		try:
			target = open("config.txt", "w")
			target.write(str(self.config))
			return True
		except IOError:
			print "Error: File does not appear to exist."
			return False

	def load_settings(self):
		pass