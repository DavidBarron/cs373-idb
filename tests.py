# -------------------------------
# Created by Kiu Fung "Nicolas" Lam
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
import watson



class testModels (TestCase):

	#------------
	# Player_model
	#------------

	'''
	Player attribute:
	name, team, number, position, height, weight, age, exp, college, image
	'''
	test_Player_dict01 = {"David Barron": ["David Barron","Liverpool","99","C","6'99",200.00,90,"123","University of Something","http://www.google.com/images"]}
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
						  player_image=test_Player_dict01["David Barron"][9]
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
						  player_image=test_Player_dict02["Mount Doritos"][9]
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
						  player_image=test_Player_dict03["Shrek Love"][9]
						 )

	def test_Player_model01(self):				
		Player01 = Player.object.get(name="David Barron")				
		self.assertEqual(Player01.name,test_Player_dict01[0])
		self.assertEqual(Player01.team,test_Player_dict01[1])
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
		self.assertEqual(Player02.name,test_Player_dict02[0])
		self.assertEqual(Player02.team,test_Player_dict02[1])
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
		self.assertEqual(Player03.name,test_Player_dict03[0])
		self.assertEqual(Player03.team,test_Player_dict03[1])
		self.assertEqual(Player03.number,test_Player_dict03[2])
		self.assertEqual(Player03.position,test_Player_dict03[3])
		self.assertEqual(Player03.height,test_Player_dict03[4])
		self.assertEqual(Player03.weight,test_Player_dict03[5])
		self.assertEqual(Player03.age,test_Player_dict03[6])
		self.assertEqual(Player03.exp,test_Player_dict03[7])
		self.assertEqual(Player03.college,test_Player_dict03[8])
		self.assertEqual(Player03.image,test_Player_dict03[9])		

	#---------------
	# Division_model
	#---------------
	'''
	Division attribute:
	division,division_image,conference,league,sport,founded,teams,mst_rec_champ,mst_champs
	'''
	test_Division_dict1 = {"Pacific 420": [0,1,2,3,4,5,6,7,8]}
	Player.objects.create(
						  division= test_Division_dict1[0]
						  division_image=test_Division_dict[1]
						  conference=test_Division_dict1[2]
						  league=test_Division_dict1[3]
						  sport=test_Division_dict1[4]
						  founded=test_Division_dict1[5]
						  teams=test_Division_dict1[6]
						  most_recent_champ=test_Division_dict1[7]
						  most_champs=test_Division_dict1[8]
						 )

	test_Division_dict2 = {"Illuminati Blaze it": [0,1,2,3,4,5,6,7,8]}
	Player.objects.create(
						  division= test_Division_dict2[0]
						  division_image=test_Division_dict2[1]
						  conference=test_Division_dict2[2]
						  league=test_Division_dict2[3]
						  sport=test_Division_dict2[4]
						  founded=test_Division_dict2[5]
						  teams=test_Division_dict2[6]
						  most_recent_champ=test_Division_dict2[7]
						  most_champs=test_Division_dict2[8]
						 )

	test_Division_dict3 = {"U WOT M8": [0,1,2,3,4,5,6,7,8]}
	Player.objects.create(
						  division= test_Division_dict3[0]
						  division_image=test_Division_dict3[1]
						  conference=test_Division_dict3[2]
						  league=test_Division_dict3[3]
						  sport=test_Division_dict3[4]
						  founded=test_Division_dict3[5]
						  teams=test_Division_dict3[6]
						  most_recent_champ=test_Division_dict3[7]
						  most_champs=test_Division_dict3[8]
						 )

	def test_Division_model01(self):				
		Division01 = Division.object.get(name="David Barron")				
		self.assertEqual(Division01.name,test_Division_dict01[0])
		self.assertEqual(Division01.team,test_Division_dict01[1])
		self.assertEqual(Division01.number,test_Division_dict01[2])
		self.assertEqual(Division01.position,test_Division_dict01[3])
		self.assertEqual(Division01.height,test_Division_dict01[4])
		self.assertEqual(Division01.weight,test_Division_dict01[5])
		self.assertEqual(Division01.age,test_Division_dict01[6])
		self.assertEqual(Division01.exp,test_Division_dict01[7])
		self.assertEqual(Division01.college,test_Division_dict01[8])
		self.assertEqual(Division01.image,test_Division_dict01[9])

	def test_Division_model02(self):		
		Division02 = Division.object.get(name="Mount Doritos")
		self.assertEqual(Division02.name,test_Division_dict02[0])
		self.assertEqual(Division02.team,test_Division_dict02[1])
		self.assertEqual(Division02.number,test_Division_dict02[2])
		self.assertEqual(Division02.position,test_Division_dict02[3])
		self.assertEqual(Division02.height,test_Division_dict02[4])
		self.assertEqual(Division02.weight,test_Division_dict02[5])
		self.assertEqual(Division02.age,test_Division_dict02[6])
		self.assertEqual(Division02.exp,test_Division_dict02[7])
		self.assertEqual(Division02.college,test_Division_dict02[8])
		self.assertEqual(Division02.image,test_Division_dict02[9])

	def test_Division_model03(self):
		Division03 = Division.object.get(name="Shrek Love")
		self.assertEqual(Division03.name,test_Division_dict03[0])
		self.assertEqual(Division03.team,test_Division_dict03[1])
		self.assertEqual(Division03.number,test_Division_dict03[2])
		self.assertEqual(Division03.position,test_Division_dict03[3])
		self.assertEqual(Division03.height,test_Division_dict03[4])
		self.assertEqual(Division03.weight,test_Division_dict03[5])
		self.assertEqual(Division03.age,test_Division_dict03[6])
		self.assertEqual(Division03.exp,test_Division_dict03[7])
		self.assertEqual(Division03.college,test_Division_dict03[8])
		self.assertEqual(Division03.image,test_Division_dict03[9])		


	
	#---------------
	# Team_model
	#---------------
	def Team_team01(self): 
	def Team_team02(self): 
	def Team_team03(self): 

	def Team_division01(self):
	def Team_division02(self):
	def Team_division03(self):

	def Team_state01(self):	
	def Team_state02(self):	
	def Team_state03(self):	

	def Team_city01(self):
	def Team_city02(self):
	def Team_city03(self):

	def Team_statium01(self):
	def Team_statium02(self):
	def Team_statium03(self):

	def Team_established01(self):
	def Team_established02(self):
	def Team_established03(self):

	def Team_coach01(self):
	def Team_coach02(self):
	def Team_coach03(self):
			
	def Team_conference01(self):		
	def Team_conference02(self):		
	def Team_conference03(self):		
			
	def Team_owner01(self):
	def Team_owner02(self):
	def Team_owner03(self):


if __name__ == "__main__" :
    main()
