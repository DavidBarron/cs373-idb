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
from yafbdb.models import *

try:
    from urllib.request import urlopen, Request
except:
    from urllib2 import *

import json



class testModels (TestCase):
	#---------------
	# Division_model
	#---------------
	'''
	Division attribute:
	division,division_image,conference,league,sport,founded,teams,mst_rec_champ,mst_champs
	'''

	print(Division.objects.all())

	def test_Division_model01(self):		
		test_Division_dict01 = [
							   "AFC North",
							   "static/images/afc_north.jpg",
								"American Football Conference",
								"static/images/afc.jpg",
								"1967",
								"Pittsburgh Steelers",
								"Pittsburgh Steelers",
								"19"
							  ]			

		a = Division(
						division=test_Division_dict01[0],
						dimage=test_Division_dict01[1],
						conference=test_Division_dict01[2],
						cimage=test_Division_dict01[3],					  
						founded=test_Division_dict01[4],						  
						rchamp=test_Division_dict01[5],
						mchamps=test_Division_dict01[6],
						cnum=test_Division_dict01[7]
					)
		self.assertEqual(a.division,test_Division_dict01[0])
		self.assertEqual(a.dimage,test_Division_dict01[1])
		self.assertEqual(a.conference,test_Division_dict01[2])
		self.assertEqual(a.cimage,test_Division_dict01[3])
		self.assertEqual(a.founded,test_Division_dict01[4])
		self.assertEqual(a.rchamp,test_Division_dict01[5])
		self.assertEqual(a.mchamps,test_Division_dict01[6])
		self.assertEqual(a.cnum,test_Division_dict01[7])

	def test_Division_model02(self):				
		div_dic = ["AFC South",
						   "static/images/afc_south.jpg",
						   "American Football Conference",
						   "static/images/afc.jpg",
						   "2002",
						   "Indianapolis Colts",
						   "Indianapolis Colts",
						   "9"
						  ]
		b = Division.objects.create(
						  division= div_dic[0],
						  dimage=div_dic[1],
						  conference=div_dic[2],
						  cimage=div_dic[3],				  
						  founded=div_dic[4],						  
						  rchamp=div_dic[5],
						  mchamps=div_dic[6],
						  cnum=div_dic[7]
						 )

		self.assertEqual(b.division,div_dic[0])
		self.assertEqual(b.dimage,div_dic[1])
		self.assertEqual(b.conference,div_dic[2])
		self.assertEqual(b.cimage,div_dic[3])
		self.assertEqual(b.founded,div_dic[4])
		self.assertEqual(b.rchamp,div_dic[5])
		self.assertEqual(b.mchamps,div_dic[6])
		self.assertEqual(b.cnum,div_dic[7])

	def test_Division_model03(self):		
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
						  division= test_Division_dict3[0],
						  dimage=test_Division_dict3[1],
						  conference=test_Division_dict3[2],
						  cimage=test_Division_dict3[3]	,					  
						  founded=test_Division_dict3[4],						  
						  rchamp=test_Division_dict3[5],
						  mchamps=test_Division_dict3[6],
						  cnum=test_Division_dict3[7]
						 )

		self.assertEqual(c.division,test_Division_dict3[0])
		self.assertEqual(c.dimage,test_Division_dict3[1])
		self.assertEqual(c.conference,test_Division_dict3[2])
		self.assertEqual(c.cimage,test_Division_dict3[3])
		self.assertEqual(c.founded,test_Division_dict3[4])
		self.assertEqual(c.rchamp,test_Division_dict3[5])
		self.assertEqual(c.mchamps,test_Division_dict3[6])
		self.assertEqual(c.cnum,test_Division_dict3[7])


	# #---------------
	# # Team_model
	# #---------------
	# '''
	# Team attribute:
	# team,team_image,division,state,city,stadium,stadium_image,coach,established,conference_champs,superbowl_champs
	# '''	
	def test_Team_model01(self):
		div_dic = [
							   "AFC North",
							   "static/images/afc_north.jpg",
								"American Football Conference",
								"static/images/afc.jpg",
								"1967",
								"Pittsburgh Steelers",
								"Pittsburgh Steelers",
								"19"
							  ]	

		a = Division(
							division=div_dic[0],
							dimage=div_dic[1],
							conference=div_dic[2],
							cimage=div_dic[3],					  
							founded=div_dic[4],						  
							rchamp=div_dic[5],
							mchamps=div_dic[6],
							cnum=div_dic[7]
						)	
		a.save()

		team_dict = {"Team01": ["Dallas Cowboys",
									   "static/images/cowyboys.png",
									   "AFC North",
									   "TX",
									   "Arlington",
									   "AT&T Stadium",
									   "https://upload.wikimedia.org/wikipedia/commons/2/29/Cowboys_stadium.JPG",
									   "Jason Garrett",
									   "1960",
									   "10",
									   "5"
									  ]}

		b = Team(team=team_dict["Team01"][0],
				timage=team_dict["Team01"][1],
				division=a,
				state=team_dict["Team01"][3],
				city=team_dict["Team01"][4],
				stadium=team_dict["Team01"][5],
				simage=team_dict["Team01"][6],
				coach=team_dict["Team01"][7],
				established=team_dict["Team01"][8],
				cchamps=team_dict["Team01"][9],
				schamps=team_dict["Team01"][10],
				)

		self.assertEqual(b.team,team_dict["Team01"][0])
		self.assertEqual(b.timage,team_dict["Team01"][1])
		self.assertEqual(b.division.division,team_dict["Team01"][2])
		self.assertEqual(b.state,team_dict["Team01"][3])		
		self.assertEqual(b.city,team_dict["Team01"][4])
		self.assertEqual(b.stadium,team_dict["Team01"][5])
		self.assertEqual(b.simage,team_dict["Team01"][6])
		self.assertEqual(b.coach,team_dict["Team01"][7])
		self.assertEqual(b.established,team_dict["Team01"][8])
		self.assertEqual(b.cchamps,team_dict["Team01"][9])
		self.assertEqual(b.schamps,team_dict["Team01"][10])

	def test_Team_model02(self):
		div_dic = ["AFC South",
						   "static/images/afc_south.jpg",
						   "American Football Conference",
						   "static/images/afc.jpg",
						   "2002",
						   "Indianapolis Colts",
						   "Indianapolis Colts",
						   "9"
						  ]	

		a = Division(
							division=div_dic[0],
							dimage=div_dic[1],
							conference=div_dic[2],
							cimage=div_dic[3],					  
							founded=div_dic[4],						  
							rchamp=div_dic[5],
							mchamps=div_dic[6],
							cnum=div_dic[7]
						)	
		a.save()

		team_dict = {"Team01": ["Dallas Cowboys",
									   "static/images/cowyboys.png",
									   "AFC South",
									   "TX",
									   "Arlington",
									   "AT&T Stadium",
									   "https://upload.wikimedia.org/wikipedia/commons/2/29/Cowboys_stadium.JPG",
									   "Jason Garrett",
									   "1960",
									   "10",
									   "5"
									  ]}

		b = Team(team=team_dict["Team01"][0],
				 timage=team_dict["Team01"][1],
				 division=a,
				 state=team_dict["Team01"][3],
				 city=team_dict["Team01"][4],
				 stadium=team_dict["Team01"][5],
				 simage=team_dict["Team01"][6],
				 coach=team_dict["Team01"][7],
				 established=team_dict["Team01"][8],
				 cchamps=team_dict["Team01"][9],
				 schamps=team_dict["Team01"][10],
				)

		self.assertEqual(b.team,team_dict["Team01"][0])
		self.assertEqual(b.timage,team_dict["Team01"][1])
		self.assertEqual(b.division.division,team_dict["Team01"][2])
		self.assertEqual(b.state,team_dict["Team01"][3])		
		self.assertEqual(b.city,team_dict["Team01"][4])
		self.assertEqual(b.stadium,team_dict["Team01"][5])
		self.assertEqual(b.simage,team_dict["Team01"][6])
		self.assertEqual(b.coach,team_dict["Team01"][7])
		self.assertEqual(b.established,team_dict["Team01"][8])
		self.assertEqual(b.cchamps,team_dict["Team01"][9])
		self.assertEqual(b.schamps,team_dict["Team01"][10])

	def test_Team_model03(self):
		div_dic = ["AFC West",
						   "static/images/afc_west.jpg",
						   "American Football Conference",
						   "static/images/afc.jpg",
						   "1960",
						   "Denver Broncos",
						   "Oakland Raiders",
						   "15"
						  ]

		a = Division(
							division=div_dic[0],
							dimage=div_dic[1],
							conference=div_dic[2],
							cimage=div_dic[3],					  
							founded=div_dic[4],						  
							rchamp=div_dic[5],
							mchamps=div_dic[6],
							cnum=div_dic[7]
						)	
		a.save()

		team_dict = {"Team01": ["Dallas Cowboys",
									   "static/images/cowyboys.png",
									   "AFC West",
									   "TX",
									   "Arlington",
									   "AT&T Stadium",
									   "https://upload.wikimedia.org/wikipedia/commons/2/29/Cowboys_stadium.JPG",
									   "Jason Garrett",
									   "1960",
									   "10",
									   "5"
									  ]}

		b = Team(team=team_dict["Team01"][0],
							timage=team_dict["Team01"][1],
							division=a,
							state=team_dict["Team01"][3],
							city=team_dict["Team01"][4],
							stadium=team_dict["Team01"][5],
							simage=team_dict["Team01"][6],
							coach=team_dict["Team01"][7],
							established=team_dict["Team01"][8],
							cchamps=team_dict["Team01"][9],
							schamps=team_dict["Team01"][10],
							)

		self.assertEqual(b.team,team_dict["Team01"][0])
		self.assertEqual(b.timage,team_dict["Team01"][1])
		self.assertEqual(b.division.division,team_dict["Team01"][2])
		self.assertEqual(b.state,team_dict["Team01"][3])		
		self.assertEqual(b.city,team_dict["Team01"][4])
		self.assertEqual(b.stadium,team_dict["Team01"][5])
		self.assertEqual(b.simage,team_dict["Team01"][6])
		self.assertEqual(b.coach,team_dict["Team01"][7])
		self.assertEqual(b.established,team_dict["Team01"][8])
		self.assertEqual(b.cchamps,team_dict["Team01"][9])
		self.assertEqual(b.schamps,team_dict["Team01"][10])

	def test_Player_model01(self):
		div_dic = ["AFC West",
						   "static/images/afc_west.jpg",
						   "American Football Conference",
						   "static/images/afc.jpg",
						   "1960",
						   "Denver Broncos",
						   "Oakland Raiders",
						   "15"
				   ]

		a = Division(
							division=div_dic[0],
							dimage=div_dic[1],
							conference=div_dic[2],
							cimage=div_dic[3],					  
							founded=div_dic[4],						  
							rchamp=div_dic[5],
							mchamps=div_dic[6],
							cnum=div_dic[7]
						)	
		a.save()

		team_dict = {"Team01": ["Dallas Cowboys",
									   "static/images/cowyboys.png",
									   "AFC West",
									   "TX",
									   "Arlington",
									   "AT&T Stadium",
									   "https://upload.wikimedia.org/wikipedia/commons/2/29/Cowboys_stadium.JPG",
									   "Jason Garrett",
									   "1960",
									   "10",
									   "5"
									  ]}

		b = Team(team=team_dict["Team01"][0],
							timage=team_dict["Team01"][1],
							division=a,
							state=team_dict["Team01"][3],
							city=team_dict["Team01"][4],
							stadium=team_dict["Team01"][5],
							simage=team_dict["Team01"][6],
							coach=team_dict["Team01"][7],
							established=team_dict["Team01"][8],
							cchamps=team_dict["Team01"][9],
							schamps=team_dict["Team01"][10],
							)
		b.save()

		ply_dict = ["Drew Brees",
					"Dallas Cowboys",
					"45","LS",
					"6-0",
					241,
					36,
					"15",
					"Western Washington",
					"http://a.espncdn.com/combiner/i?img=/i/headshots/nfl/players/full/2580.png"
					]
		Player01 = Player.objects.create(
								name="David Barron",
								team=b,
								number=ply_dict[2],
								position=ply_dict[3],
								height=ply_dict[4],
								weight=ply_dict[5],
								age=ply_dict[6],
								experience=ply_dict[7],
								college=ply_dict[8],
								pimage=ply_dict[9]
							  )

		self.assertEqual(Player01.name,"David Barron")
		self.assertEqual(Player01.team.team,ply_dict[1])
		self.assertEqual(Player01.number,ply_dict[2])
		self.assertEqual(Player01.position,ply_dict[3])
		self.assertEqual(Player01.height,ply_dict[4])
		self.assertEqual(Player01.weight,ply_dict[5])
		self.assertEqual(Player01.age,ply_dict[6])
		self.assertEqual(Player01.experience,ply_dict[7])
		self.assertEqual(Player01.college,ply_dict[8])
		self.assertEqual(Player01.pimage,ply_dict[9])

	def test_Player_model02(self):
		div_dic = ["AFC West",
						   "static/images/afc_west.jpg",
						   "American Football Conference",
						   "static/images/afc.jpg",
						   "1960",
						   "Denver Broncos",
						   "Oakland Raiders",
						   "15"
				   ]

		a = Division(
							division=div_dic[0],
							dimage=div_dic[1],
							conference=div_dic[2],
							cimage=div_dic[3],					  
							founded=div_dic[4],						  
							rchamp=div_dic[5],
							mchamps=div_dic[6],
							cnum=div_dic[7]
						)	
		a.save()

		team_dict = {"Team01": ["Dallas Cowboys",
									   "static/images/cowyboys.png",
									   "AFC West",
									   "TX",
									   "Arlington",
									   "AT&T Stadium",
									   "https://upload.wikimedia.org/wikipedia/commons/2/29/Cowboys_stadium.JPG",
									   "Jason Garrett",
									   "1960",
									   "10",
									   "5"
									  ]}

		b = Team(team=team_dict["Team01"][0],
							timage=team_dict["Team01"][1],
							division=a,
							state=team_dict["Team01"][3],
							city=team_dict["Team01"][4],
							stadium=team_dict["Team01"][5],
							simage=team_dict["Team01"][6],
							coach=team_dict["Team01"][7],
							established=team_dict["Team01"][8],
							cchamps=team_dict["Team01"][9],
							schamps=team_dict["Team01"][10],
							)
		b.save()

		ply_dict = ["Drew Brees",
					"Dallas Cowboys",
					"45","LS",
					"6-0",
					241,
					36,
					"15",
					"Western Washington",
					"http://a.espncdn.com/combiner/i?img=/i/headshots/nfl/players/full/2580.png"
					]
		Player01 = Player.objects.create(
								name="David Barron",
								team=b,
								number=ply_dict[2],
								position=ply_dict[3],
								height=ply_dict[4],
								weight=ply_dict[5],
								age=ply_dict[6],
								experience=ply_dict[7],
								college=ply_dict[8],
								pimage=ply_dict[9]
							  )		
		self.assertEqual(Player01.name,"David Barron")
		self.assertEqual(Player01.team.team,ply_dict[1])
		self.assertEqual(Player01.number,ply_dict[2])
		self.assertEqual(Player01.position,ply_dict[3])
		self.assertEqual(Player01.height,ply_dict[4])
		self.assertEqual(Player01.weight,ply_dict[5])
		self.assertEqual(Player01.age,ply_dict[6])
		self.assertEqual(Player01.experience,ply_dict[7])
		self.assertEqual(Player01.college,ply_dict[8])
		self.assertEqual(Player01.pimage,ply_dict[9])

	def test_Player_model03(self):
		div_dic = ["AFC West",
						   "static/images/afc_west.jpg",
						   "American Football Conference",
						   "static/images/afc.jpg",
						   "1960",
						   "Denver Broncos",
						   "Oakland Raiders",
						   "15"
						  ]

		a = Division(
							division=div_dic[0],
							dimage=div_dic[1],
							conference=div_dic[2],
							cimage=div_dic[3],					  
							founded=div_dic[4],						  
							rchamp=div_dic[5],
							mchamps=div_dic[6],
							cnum=div_dic[7]
						)	
		a.save()
		team_dict = ["Dallas Cowboys",
					"static/images/cowyboys.png",
					"AFC West",
					"TX",
					"Arlington",
					"AT&T Stadium",
					"https://upload.wikimedia.org/wikipedia/commons/2/29/Cowboys_stadium.JPG",
					"Jason Garrett",
					"1960",
					"10",
					"5"
					]

		b = Team(team=team_dict[0],
							timage=team_dict[1],
							division=a,
							state=team_dict[3],
							city=team_dict[4],
							stadium=team_dict[5],
							simage=team_dict[6],
							coach=team_dict[7],
							established=team_dict[8],
							cchamps=team_dict[9],
							schamps=team_dict[10],
							)
		b.save()

		ply_dict= ["Shrek Love","Dallas Cowboys","360","DT","4'32",374.25,"99","R","University of Phoenix","www.uop.com/images"]
		Player01 = Player(       name="Shrek Love",
						  team=b,
						  number=ply_dict[2],
						  position=ply_dict[3],
						  height=ply_dict[4],
						  weight=ply_dict[5],
						  age=ply_dict[6],
						  experience=ply_dict[7],
						  college=ply_dict[8],
						  pimage=ply_dict[9]
						)

		self.assertEqual(Player01.name,"Shrek Love")
		self.assertEqual(Player01.team.team,ply_dict[1])
		self.assertEqual(Player01.number,ply_dict[2])
		self.assertEqual(Player01.position,ply_dict[3])
		self.assertEqual(Player01.height,ply_dict[4])
		self.assertEqual(Player01.weight,ply_dict[5])
		self.assertEqual(Player01.age,ply_dict[6])
		self.assertEqual(Player01.experience,ply_dict[7])
		self.assertEqual(Player01.college,ply_dict[8])
		self.assertEqual(Player01.pimage,ply_dict[9])






	# #------------
	# # Player_model
	# #------------

	# '''
	# Player attribute:
	# name, team, number, position, height, weight, age, exp, college, image
	# '''
	# test_Player_dict01 = {"David Barron": ["Drew Brees",
	# 									   "Indianapolis Colts",
	# 									   "45","LS",
	# 									   "6-0",
	# 									   241,
	# 									   36,
	# 									   "15",
	# 									   "Western Washington",
	# 									   "http://a.espncdn.com/combiner/i?img=/i/headshots/nfl/players/full/2580.png"]}
	# Player.objects.create(
	# 					  name="David Barron",
	# 					  team=test_Player_dict01["David Barron"][1],
	# 					  number=test_Player_dict01["David Barron"][2],
	# 					  position=test_Player_dict01["David Barron"][3],
	# 					  height=test_Player_dict01["David Barron"][4],
	# 					  weight=test_Player_dict01["David Barron"][5],
	# 					  age=test_Player_dict01["David Barron"][6],
	# 					  experience=test_Player_dict01["David Barron"][7],
	# 					  college=test_Player_dict01["David Barron"][8],
	# 					  pimage=test_Player_dict01["David Barron"][9]
	# 					 )

	# test_Player_dict02 = {"Mount Doritos": ["Mount Doritos","Illuminati","420","DT","4'20",69.420,69,"R","University of What Mate","http://www.xxxDDDDWOTDDDDxxx.com"]}
	# Player.objects.create(
	# 					  name="Mount Doritos",
	# 					  team=test_Player_dict02["Mount Doritos"][1],
	# 					  number=test_Player_dict02["Mount Doritos"][2],
	# 					  position=test_Player_dict02["Mount Doritos"][3],
	# 					  height=test_Player_dict02["Mount Doritos"][4],
	# 					  weight=test_Player_dict02["Mount Doritos"][5],
	# 					  age=test_Player_dict02["Mount Doritos"][6],
	# 					  experience=test_Player_dict02["Mount Doritos"][7],
	# 					  college=test_Player_dict02["Mount Doritos"][8],
	# 					  pimage=test_Player_dict02["Mount Doritos"][9]
	# 					 )

	# ply_dict = {"Shrek Love": ["Shrek Love","Fight","360","DT","4'32",374.25,"R","University of Phoenix","www.uop.com/images"]}
	# Player.objects.create(
	# 					  name="Shrek Love",
	# 					  team=ply_dict["Shrek Love"][1],
	# 					  number=ply_dict["Shrek Love"][2],
	# 					  position=ply_dict["Shrek Love"][3],
	# 					  height=ply_dict["Shrek Love"][4],
	# 					  weight=ply_dict["Shrek Love"][5],
	# 					  age=ply_dict["Shrek Love"][6],
	# 					  experience=ply_dict["Shrek Love"][7],
	# 					  college=ply_dict["Shrek Love"][8],
	# 					  pimage=ply_dict["Shrek Love"][9]
	# 					 )

	# def test_Player_model01(self):				
	# 	Player01 = Player.object.get(name="David Barron")				
	# 	self.assertEqual(Player01.name,"David Barron")
	# 	self.assertEqual(Player01.team.team,test_Player_dict01[1])
	# 	self.assertEqual(Player01.number,test_Player_dict01[2])
	# 	self.assertEqual(Player01.position,test_Player_dict01[3])
	# 	self.assertEqual(Player01.height,test_Player_dict01[4])
	# 	self.assertEqual(Player01.weight,test_Player_dict01[5])
	# 	self.assertEqual(Player01.age,test_Player_dict01[6])
	# 	self.assertEqual(Player01.exp,test_Player_dict01[7])
	# 	self.assertEqual(Player01.college,test_Player_dict01[8])
	# 	self.assertEqual(Player01.image,test_Player_dict01[9])

	# def test_Player_model02(self):		
	# 	Player02 = Player.object.get(name="Mount Doritos")
	# 	self.assertEqual(Player02.name,"Mount Doritos")
	# 	self.assertEqual(Player02.team.team,test_Player_dict02[1])
	# 	self.assertEqual(Player02.number,test_Player_dict02[2])
	# 	self.assertEqual(Player02.position,test_Player_dict02[3])
	# 	self.assertEqual(Player02.height,test_Player_dict02[4])
	# 	self.assertEqual(Player02.weight,test_Player_dict02[5])
	# 	self.assertEqual(Player02.age,test_Player_dict02[6])
	# 	self.assertEqual(Player02.exp,test_Player_dict02[7])
	# 	self.assertEqual(Player02.college,test_Player_dict02[8])
	# 	self.assertEqual(Player02.image,test_Player_dict02[9])

	# def test_Player_model03(self):
	# 	Player03 = Player.object.get(name="Shrek Love")
	# 	self.assertEqual(Player03.name,"Shrek Love")
	# 	self.assertEqual(Player03.team.team,ply_dict[1])
	# 	self.assertEqual(Player03.number,ply_dict[2])
	# 	self.assertEqual(Player03.position,ply_dict[3])
	# 	self.assertEqual(Player03.height,ply_dict[4])
	# 	self.assertEqual(Player03.weight,ply_dict[5])
	# 	self.assertEqual(Player03.age,ply_dict[6])
	# 	self.assertEqual(Player03.exp,ply_dict[7])
	# 	self.assertEqual(Player03.college,ply_dict[8])
	# 	self.assertEqual(Player03.image,ply_dict[9])		





if __name__ == "__main__" :
	main()
