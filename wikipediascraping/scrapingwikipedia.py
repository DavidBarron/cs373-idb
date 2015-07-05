#!/usr/bin/env python3

# -------------------------------
# projects/cs373-idb/scrapingwikipedia.py
# Copyright (C) 2015
# charlieWork
# -------------------------------

# This script follows the scraping method explained here:
# http://docs.python-guide.org/en/latest/scenarios/scrape/

# -------
# imports
# -------

from lxml import html
import requests


# --------------------
# create_division_json
# --------------------

def create_division_json(division):

	page = requests.get('https://en.wikipedia.org/wiki/' + division)
	tree = html.fromstring(page.text)

	keys = tree.xpath('//table[@class="infobox"]//th[@scope="row"]/text()')
	#print(keys)
	values = tree.xpath('//table[@class="infobox"]//td/text() | //table[@class="infobox"]//a/text() | //table[@class="infobox"]//div/text()')
	values = [value for value in values if value[0] != "\n" and value != u'\xa0']
	#print(values)
	values[4] = (values[4], values[5], values[6], values[7])
	del values[5:8]


	f = open("divisions/" + division + ".json","w")

	f.write("{\n")
	for i, (k, v) in enumerate(zip(keys,values)):
		if type(v) is tuple:
			f.write('    "' + k + '": ["' + v[0] + '", "' + v[1] + '", "' + v[2] + '", "' + v[3]+ '"]')	
		else:
			f.write('    "' + k + '": "' + v + '"')
		if i != len(keys)-1:
			f.write(",")
		f.write("\n")
	f.write("}")

# ----
# main
# ----

if __name__ == "__main__":
	conferences = ["AFC", "NFC"]
	directions = ["North","South","East","West"]
	for i in [conf + "_" + direct for conf in conferences for direct in directions]:
		create_division_json(i)




