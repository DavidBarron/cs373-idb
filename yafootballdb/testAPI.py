import url

json =  "http://yetanotherfootballdb.me/"
	def test_div_api(self):		
		request = Request(self.url+"api/divisions")
		response = urlopen(request)
		response_body = response.read().decode("utf-8")
		self.assertEqual(response.getcode(), 200)
		response_data = loads(response_body)		
		res_obj = response_data["results"]