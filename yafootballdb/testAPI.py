from json import dumps, loads
try:
    from urllib.request import urlopen, Request
except:
    from urllib2 import *

def test_artist_api():		
	url =  "http://volumemax.me/"
	request = Request(url+"api/artists")	
	response = urlopen(request)
	response_body = response.read().decode("utf-8")	
	# assert((response.getcode) == 200)
	response_data = loads(response_body)
	#print(response_data[0]["origin"])		
	dict_Btich = response_data[0]
	print(dict_Btich["full_name"])

	# res_obj = response_data["results"]

test_artist_api()
