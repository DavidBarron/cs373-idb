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
from wc_app.models import *

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
	def test_Player_name01(self):
	def test_Player_name02(self):
	def test_Player_name03(self):

	def test_Player_team01(self):
	def test_Player_team02(self):
	def test_Player_team03(self):

	def test_Player_number01(self):
	def test_Player_number02(self):
	def test_Player_number03(self):		

	def test_Player_pos01(self):
	def test_Player_pos02(self):
	def test_Player_pos03(self):

	def test_Player_height01(self):
	def test_Player_height02(self):		
	def test_Player_height03(self):

	def test_Player_weight01(self):
	def test_Player_weight02(self):
	def test_Player_weight03(self):

	def test_Player_age01(self):
	def test_Player_age02(self):
	def test_Player_age03(self):

	def test_Player_exp01(self):
	def test_Player_exp02(self):
	def test_Player_exp03(self):

	def test_Player_seasons01(self):
	def test_Player_seasons02(self):
	def test_Player_seasons03(self):

	def test_Player_college01(self):
	def test_Player_college02(self):
	def test_Player_college03(self):

	def test_Player_image01(self):
	def test_Player_image02(self):
	def test_Player_image03(self):

	#---------------
	# Division_model
	#---------------
	def test_Division_Conference01(self):
	def test_Division_Conference02(self):
	def test_Division_Conference03(self):

	def test_Division_League01(self):
	def test_Division_League02(self):
	def test_Division_League03(self):

	def test_Division_Sport01(self):
	def test_Division_Sport02(self):
	def test_Division_Sport03(self):

	def test_Division_Founded01(self):	
	def test_Division_Founded02(self):	
	def test_Division_Founded03(self):	

	def test_Division_Teams01(self):	
	def test_Division_Teams02(self):	
	def test_Division_Teams03(self):	

	def test_Division_year01(self):
	def test_Division_year02(self):
	def test_Division_year03(self):

	def test_Division_mst_rec_champion01(self):
	def test_Division_mst_rec_champion02(self):
	def test_Division_mst_rec_champion03(self):

	def test_Division_mst_title01(self):
	def test_Division_mst_title02(elf):
	def test_Division_mst_title03(self):

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
