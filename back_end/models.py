from django.db import models

class Players(models.Model):	
	def Players_name(self): #Char
		player = models.CharField(maxlength=200)

	def Players_team(self): #Char
		team = models.CharField(maxlength=200)

	def Players_number(self): #Decimal
		number = models.IntegerField()

	def Players_pos(self):#Decimal		
		pos = models.IntegerField()

	def Players_height(self): #Float
		height = models.CharField(maxlength=200)

	def Players_weight(self): #Float
		weight = models.FloatField()

	def Players_age(self): #Decimal
		height = models.IntegerField()

	def Players_exp(self): #Float
		weight = models.FloatField()

	def Players_seasons(self): #Decimal
		height = models.IntegerField()

	def Players_college(self): #Char
		college = models.CharField(maxlength=200)

	def Players_image(self): #Image	
		image = models.ImageField()

class Divisions(models.Model):
	def Division_Conference(self): #Char
		conference = models.CharField(maxlength=200)
	def Division_League(self): #Char 
		league = models.CharField(maxlength=200)
	def Division_Sport(self): #Char
		sport = models.CharField(maxlength=200)
	def Division_Founded(self): #Date
		founded = models.DateField()
	def Division_Teams(self): #Char
		teams = models.CharField(maxlength=200)
	def Division_mst_rec_champion(self): #Char
		mst_rec_champ = models.CharField(maxlength=200)
	def Division_mst_title(self): #Integer
		mst_title = models.ImageField()

class Teams(models.Model):
	def Team_team(self): #Char
		mst_title = models.CharField(maxlength=200)		

	def Team_division(self):#Char
		mst_title = models.CharField(maxlength=200)	

	def Team_state(self):	#Char
		mst_title = models.CharField(maxlength=200)

	def Team_city(self):#Char
		mst_title = models.CharField(maxlength=200)

	def Team_statium(self):#Char	
		mst_title = models.CharField(maxlength=200)

	def Team_established(self): #Date
		mst_title = models.DateField()

	def Team_coach(self): #Char		
		mst_title = models.CharField(maxlength=200)		

	def Team_owner(self):#Char
		mst_title = models.CharField(maxlength=200)		

	