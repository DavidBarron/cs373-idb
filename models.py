from django.db import models


class Division(models.Model):
"""
"""
    division = models.CharField(maxlength=200)
    conference =  
    league = models.CharField(maxlength=200)
    sport = models.CharField(maxlength=200)
    founded = models.DateField()
    teams = models.CharField(maxlength=200)
    mst_rec_champ = models.CharField(maxlength=200)
    mst_title = models.ImageField()

    def __str__(self) :
        return self.division


class Team(models.Model):
"""
"""    
    team = models.CharField(maxlength=200)
    team_image =      
    division = models.CharField(maxlength=200) 
    state = models.CharField(maxlength=200)
    city = models.CharField(maxlength=200)
    stadium = models.CharField(maxlength=200)
    stadium_image = models.DateField()
    coach = models.CharField(maxlength=200)     
    established = models.CharField(maxlength=200)


    def __str__(self) :
        return self.team 


class Player(models.Model):    
"""
"""
    name = models.CharField(maxlength=200)
    team = models.ForeignKey(Team)
    number = models.IntegerField()
    position = models.CharField(maxlength=2)
    height = models.CharField(maxlength=200)
    weight = models.FloatField()
    age = models.FloatField()
    experience = models.CharField(maxlength=200)
    college = models.CharField(maxlength=200)
    player_image = models.CharField(maxlength=400)

    def __str__(self) :
        return self.name

    
