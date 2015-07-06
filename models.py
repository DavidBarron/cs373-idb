from django.db import models


class Division(models.Model):
"""
Model for a Division. Attributes conatined are : division name, division image,
conference name, lague name, sport, year founded, member teams, most recent champion,
team with most championships.
The __str__ function returns the division name as a string.
"""
    division = models.CharField(maxlength=200)
    division_image = models.CharField(maxlength=200)
    conference = models.CharField(maxlength=200)
    league = models.CharField(maxlength=200)
    sport = models.CharField(maxlength=200)
    founded = models.CharField(maxlength=200)
    teams = models.ForeignKey(Team)
    most_recent_champ = models.ForeignKey(Team)
    most_champs = models.ForeignKey(Team)

    def __str__(self) :
        return self.division


class Team(models.Model):
"""
Model for a Team. Attributes contained are: team name, team image, division,
state, city, stadium, stadium image, coach, year established, years of conference championships,
years of superbow wins.
The __str__ function returns the team name as a string.
"""    
    team = models.CharField(maxlength=200)
    team_image = models.CharField(maxlength=400)     
    division = models.ForeignKey(Division) 
    state = models.CharField(maxlength=200)
    city = models.CharField(maxlength=200)
    stadium = models.CharField(maxlength=200)
    stadium_image = models.DateField()
    coach = models.CharField(maxlength=200)     
    established = models.CharField(maxlength=200)
    conference_champs = models.CharField(maxlength=200)
    superbowl_champs = models.CharField(maxlength=200)


    def __str__(self) :
        return self.team 


class Player(models.Model):    
"""
Model for a Player. Attributes conatined are: player name, team, number, position, height,
weight, age, experience in seasons, college, image of player.
The __str__ function returns the player name as a string.
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

    
