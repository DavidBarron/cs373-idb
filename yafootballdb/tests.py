# -------------------------------
# Created by XXX
# June 2015
# -------------------------------

from io       import StringIO
from unittest import main, TestCase

# Create your tests here.
import os
import sys
import json
from django.test.utils import setup_test_environment
from django.core.urlresolvers import reverse
from django.core.management import call_command

#New Imports
from django.utils import unittest
from django.test import TestCase
from django.http import HttpResponse

from json import dumps, loads


from django.test import TestCase
from models.py import *

try:
    from urllib.request import urlopen, Request
except:
    from urllib2 import *

from tastypie.test import ResourceTestCase

import json



class testModels (TestCase):
	#---------------
	# Division_model
	#---------------
	'''
	Division attribute:
	division,division_image,conference,league,sport,founded,teams,mst_rec_champ,mst_champs
	'''
	test_Division_dict1 = [
						   "AFC North",
						   "static/images/afc_north.jpg",
							"American Football Conference",
							"static/images/afc.jpg",
							"1967",
							"Pittsburgh Steelers",
							"Pittsburgh Steelers",
							"19"
						  ]
	a = Division.objects.create(
						  division=test_Division_dict1[0],
						  dimage=test_Division_dict[1],
						  conference=test_Division_dict1[2],
						  cimage=test_Division_dict1[3],					  
						  founded=test_Division_dict1[4],						  
						  rchamp=test_Division_dict1[5],
						  mchamps=test_Division_dict1[6],
						  cnum=test_Division_dict1[7],
						 )

	test_Division_dict2 = ["AFC South",
						   "static/images/afc_south.jpg",
						   "American Football Conference",
						   "static/images/afc.jpg",
						   "2002",
						   "Indianapolis Colts",
						   "Indianapolis Colts",
						   "9"
						  ]
	b = Division.objects.create(
						  division= test_Division_dict1[0],
						  dimage=test_Division_dict[1],
						  conference=test_Division_dict1[2],
						  cimage=test_Division_dict1[3],				  
						  founded=test_Division_dict1[4],						  
						  rchamp=test_Division_dict1[5],
						  mchamps=test_Division_dict1[6],
						  cnum=test_Division_dict1[7],
						 )

	test_Division_dict3 = ["AFC West",
						   "static/images/afc_west.jpg",
						   "American Football Conference",
						   "static/images/afc.jpg",
						   "1960",
						   "Denver Broncos",
						   "Oakland Raiders",
						   "15"
						  ]

	c = Division.objects.create(
						  division= test_Division_dict1[0],
						  dimage=test_Division_dict[1],
						  conference=test_Division_dict1[2],
						  cimage=test_Division_dict1[3]	,					  
						  founded=test_Division_dict1[4],						  
						  rchamp=test_Division_dict1[5],
						  mchamps=test_Division_dict1[6],
						  cnum=test_Division_dict1[7],
						 )

	def test_Division_model01(self):									
		self.assertEqual(a.name,test_Division_dict01[0])
		self.assertEqual(a.team,test_Division_dict01[1])
		self.assertEqual(a.number,test_Division_dict01[2])
		self.assertEqual(a.position,test_Division_dict01[3])
		self.assertEqual(a.height,test_Division_dict01[4])
		self.assertEqual(a.weight,test_Division_dict01[5])
		self.assertEqual(a.age,test_Division_dict01[6])
		self.assertEqual(a.exp,test_Division_dict01[7])
		self.assertEqual(a.college,test_Division_dict01[8])
		self.assertEqual(a.image,test_Division_dict01[9])

	def test_Division_model02(self):				
		self.assertEqual(b.name,test_Division_dict02[0])
		self.assertEqual(b.team,test_Division_dict02[1])
		self.assertEqual(b.number,test_Division_dict02[2])
		self.assertEqual(b.position,test_Division_dict02[3])
		self.assertEqual(b.height,test_Division_dict02[4])
		self.assertEqual(b.weight,test_Division_dict02[5])
		self.assertEqual(b.age,test_Division_dict02[6])
		self.assertEqual(b.exp,test_Division_dict02[7])
		self.assertEqual(b.college,test_Division_dict02[8])
		self.assertEqual(b.image,test_Division_dict02[9])

	def test_Division_model03(self):		
		self.assertEqual(c.name,test_Division_dict03[0])
		self.assertEqual(c.team,test_Division_dict03[1])
		self.assertEqual(c.number,test_Division_dict03[2])
		self.assertEqual(c.position,test_Division_dict03[3])
		self.assertEqual(c.height,test_Division_dict03[4])
		self.assertEqual(c.weight,test_Division_dict03[5])
		self.assertEqual(c.age,test_Division_dict03[6])
		self.assertEqual(c.exp,test_Division_dict03[7])
		self.assertEqual(c.college,test_Division_dict03[8])
		self.assertEqual(c.image,test_Division_dict03[9])

	#---------------
	# Team_model
	#---------------
	'''
	Team attribute:
	team,team_image,division,state,city,stadium,stadium_image,coach,established,conference_champs,superbowl_champs
	'''	
	test_Team_dict01 = {"Team01": ["Dallas Cowboys",
								   "static/images/cowyboys.png",
								   "NFC East",
								   "TX",
								   "Arlington",
								   "AT&T Stadium",
								   "https://upload.wikimedia.org/wikipedia/commons/2/29/Cowboys_stadium.JPG",
								   "Jason Garrett",
								   "1960",
								   "10",
								   "5"]}

	Team.objects.create(team=test_Team_dict1["Team01"][0],
						team_image=test_Team_dict1["Team01"][1],
						division=test_Team_dict1["Team01"][2],
						state=test_Team_dict1["Team01"][3],
						city=test_Team_dict1["Team01"][4],
						stadium=test_Team_dict1["Team01"][5],
						stadium_image=test_Team_dict1["Team01"][6],
						coach=test_Team_dict1["Team01"][7],
						established=test_Team_dict1["Team01"][8],
						conference_champs=test_Team_dict1["Team01"][9],
						superbowl_champs=test_Team_dict1["Team01"][10],
					   )

	test_Team_dict02 = {"Team02": ["New York Giants",
								   "static/images/giants.png"								   
								   "NFC East",
								   "NJ",
								   "East Rutherford",
								   "MetLife Stadium",
								   "https://upload.wikimedia.org/wikipedia/commons/4/46/New_Meadowlands_Stadium_Mezz_Corner.jpg",
								   "Tom Coughlin",
								   "1925",
								   "11",
								   "4"]}

	Team.objects.create(team=test_Team_dict2["Team02"][0],
						team_image=test_Team_dict2["Team02"][1],
						division=test_Team_dict2["Team02"][2],
						state=test_Team_dict2["Team02"][3],
						city=test_Team_dict2["Team02"][4],
						stadium=test_Team_dict2["Team02"][5],
						stadium_image=test_Team_dict2["Team02"][6],
						coach=test_Team_dict2["Team02"][7],
						established=test_Team_dict2["Team02"][8],
						conference_champs=test_Team_dict2["Team02"][9],
						superbowl_champs=test_Team_dict2["Team02"][10]	,				   	
				 	   )

	test_Team_dict03 = {"Team03": ["Philadelphia Eagles",
								   "NFC East",
								   "static/images/eagles.png",
								   "PA",
								   "Philadelphia",
								   "Lincoln Financial Field",
								   "https://upload.wikimedia.org/wikipedia/commons/7/71/Philly_%%2845%%29.JPG",
								   "Chip Kelly",
								   "1933",
								   "3",
								   "0"]}

	Team.objects.create(team=test_Team_dict3["Team03"][0],
						team_image=test_Team_dict3["Team03"][1],
						division=test_Team_dict3["Team03"][2],
						state=test_Team_dict3["Team03"][3],
						city=test_Team_dict3["Team03"][4],
						stadium=test_Team_dict3["Team03"][5],
						stadium_image=test_Team_dict3["Team03"][6],
						coach=test_Team_dict3["Team03"][7],
						established=test_Team_dict3["Team03"][8],
						conference_champs=test_Team_dict3["Team03"][9],
						superbowl_champs=test_Team_dict3["Team03"][10],
						 )

	def test_Team_model01(self):				
		Team01 = Team.object.get(team="Team01")				
		self.assertEqual(Team01.team,test_Team_dict01["Team01"][0])
		self.assertEqual(Team01.team_image,test_Team_dict01["Team01"][1])
		self.assertEqual(Team01.division.division,test_Team_dict01["Team01"][2])
		self.assertEqual(Team01.state,test_Team_dict01["Team01"][3])		
		self.assertEqual(Team01.city,test_Team_dict01["Team01"][4])
		self.assertEqual(Team01.stadium,test_Team_dict01["Team01"][5])
		self.assertEqual(Team01.stadium_image,test_Team_dict01["Team01"][6])
		self.assertEqual(Team01.coach,test_Team_dict01["Team01"][7])
		self.assertEqual(Team01.established,test_Team_dict01["Team01"][7])
		self.assertEqual(Team01.conference_champs,test_Team_dict01["Team01"][8])
		self.assertEqual(Team01.superbowl_champs,test_Team_dict01["Team01"][9])

	def test_Team_model02(self):		
		Team02 = Team.object.get(team="Team02")
		self.assertEqual(Team02.team,test_Team_dict02["Team02"][0])
		self.assertEqual(Team02.team_image,test_Team_dict02["Team02"][1])
		self.assertEqual(Team02.division,test_Team_dict02["Team02"][2])
		self.assertEqual(Team02.state,test_Team_dict02["Team02"][3])		
		self.assertEqual(Team02.city,test_Team_dict02["Team02"][4])
		self.assertEqual(Team02.stadium,test_Team_dict02["Team02"][5])
		self.assertEqual(Team02.stadium_image,test_Team_dict02["Team02"][6])
		self.assertEqual(Team02.coach,test_Team_dict02["Team02"][7])
		self.assertEqual(Team02.established,test_Team_dict02["Team02"][7])
		self.assertEqual(Team02.conference_champs,test_Team_dict02["Team02"][8])
		self.assertEqual(Team02.superbowl_champs,test_Team_dict02["Team02"][9])

	def test_Team_model03(self):
		Team03 = Team.object.get(name="Team03")
		self.assertEqual(Team03.team,test_Team_dict03["Team03"][0])
		self.assertEqual(Team03.team_image,test_Team_dict03["Team03"][1])
		self.assertEqual(Team03.division,test_Team_dict03["Team03"][2])
		self.assertEqual(Team03.state,test_Team_dict03["Team03"][3])		
		self.assertEqual(Team03.city,test_Team_dict03["Team03"][4])
		self.assertEqual(Team03.stadium,test_Team_dict03["Team03"][5])
		self.assertEqual(Team03.stadium_image,test_Team_dict03["Team03"][6])
		self.assertEqual(Team03.coach,test_Team_dict03["Team03"][7])
		self.assertEqual(Team03.established,test_Team_dict03["Team03"][7])
		self.assertEqual(Team03.conference_champs,test_Team_dict03["Team03"][8])
		self.assertEqual(Team03.superbowl_champs,test_Team_dict03["Team03"][9])


	#------------
	# Player_model
	#------------

	'''
	Player attribute:
	name, team, number, position, height, weight, age, exp, college, image
	'''
	test_Player_dict01 = {"David Barron": ["Drew Brees",
										   "Indianapolis Colts",
										   "45","LS",
										   "6-0",
										   241,
										   36,
										   "15",
										   "Western Washington",
										   "http://a.espncdn.com/combiner/i?img=/i/headshots/nfl/players/full/2580.png"]}
	Player.objects.create(
						  name="David Barron",
						  team=test_Player_dict01["David Barron"][1],
						  number=test_Player_dict01["David Barron"][2],
						  position=test_Player_dict01["David Barron"][3],
						  height=test_Player_dict01["David Barron"][4],
						  weight=test_Player_dict01["David Barron"][5],
						  age=test_Player_dict01["David Barron"][6],
						  experience=test_Player_dict01["David Barron"][7],
						  college=test_Player_dict01["David Barron"][8],
						  pimage=test_Player_dict01["David Barron"][9]
						 )

	test_Player_dict02 = {"Mount Doritos": ["Mount Doritos","Illuminati","420","DT","4'20",69.420,69,"R","University of What Mate","http://www.xxxDDDDWOTDDDDxxx.com"]}
	Player.objects.create(
						  name="Mount Doritos",
						  team=test_Player_dict02["Mount Doritos"][1],
						  number=test_Player_dict02["Mount Doritos"][2],
						  position=test_Player_dict02["Mount Doritos"][3],
						  height=test_Player_dict02["Mount Doritos"][4],
						  weight=test_Player_dict02["Mount Doritos"][5],
						  age=test_Player_dict02["Mount Doritos"][6],
						  experience=test_Player_dict02["Mount Doritos"][7],
						  college=test_Player_dict02["Mount Doritos"][8],
						  pimage=test_Player_dict02["Mount Doritos"][9]
						 )

	test_Player_dict03 = {"Shrek Love": ["Shrek Love","Fight","360","DT","4'32",374.25,"R","University of Phoenix","www.uop.com/images"]}
	Player.objects.create(
						  name="Shrek Love",
						  team=test_Player_dict03["Shrek Love"][1],
						  number=test_Player_dict03["Shrek Love"][2],
						  position=test_Player_dict03["Shrek Love"][3],
						  height=test_Player_dict03["Shrek Love"][4],
						  weight=test_Player_dict03["Shrek Love"][5],
						  age=test_Player_dict03["Shrek Love"][6],
						  experience=test_Player_dict03["Shrek Love"][7],
						  college=test_Player_dict03["Shrek Love"][8],
						  pimage=test_Player_dict03["Shrek Love"][9]
						 )

	def test_Player_model01(self):				
		Player01 = Player.object.get(name="David Barron")				
		self.assertEqual(Player01.name,"David Barron")
		self.assertEqual(Player01.team.team,test_Player_dict01[1])
		self.assertEqual(Player01.number,test_Player_dict01[2])
		self.assertEqual(Player01.position,test_Player_dict01[3])
		self.assertEqual(Player01.height,test_Player_dict01[4])
		self.assertEqual(Player01.weight,test_Player_dict01[5])
		self.assertEqual(Player01.age,test_Player_dict01[6])
		self.assertEqual(Player01.exp,test_Player_dict01[7])
		self.assertEqual(Player01.college,test_Player_dict01[8])
		self.assertEqual(Player01.image,test_Player_dict01[9])

	def test_Player_model02(self):		
		Player02 = Player.object.get(name="Mount Doritos")
		self.assertEqual(Player02.name,"Mount Doritos")
		self.assertEqual(Player02.team.team,test_Player_dict02[1])
		self.assertEqual(Player02.number,test_Player_dict02[2])
		self.assertEqual(Player02.position,test_Player_dict02[3])
		self.assertEqual(Player02.height,test_Player_dict02[4])
		self.assertEqual(Player02.weight,test_Player_dict02[5])
		self.assertEqual(Player02.age,test_Player_dict02[6])
		self.assertEqual(Player02.exp,test_Player_dict02[7])
		self.assertEqual(Player02.college,test_Player_dict02[8])
		self.assertEqual(Player02.image,test_Player_dict02[9])

	def test_Player_model03(self):
		Player03 = Player.object.get(name="Shrek Love")
		self.assertEqual(Player03.name,"Shrek Love")
		self.assertEqual(Player03.team.team,test_Player_dict03[1])
		self.assertEqual(Player03.number,test_Player_dict03[2])
		self.assertEqual(Player03.position,test_Player_dict03[3])
		self.assertEqual(Player03.height,test_Player_dict03[4])
		self.assertEqual(Player03.weight,test_Player_dict03[5])
		self.assertEqual(Player03.age,test_Player_dict03[6])
		self.assertEqual(Player03.exp,test_Player_dict03[7])
		self.assertEqual(Player03.college,test_Player_dict03[8])
		self.assertEqual(Player03.image,test_Player_dict03[9])		

	
	



if __name__ == "__main__" :
    main()
