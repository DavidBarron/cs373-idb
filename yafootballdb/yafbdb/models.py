from django.db import models


class Division(models.Model):
    """
    Model for a Division. Attributes conatined are : division name, division image,
    conference name, lague name, sport, year founded, member teams, most recent champion,
    team with most championships.
    The __str__ function returns the division name as a string.
    """
    division = models.CharField(max_length=200)
    dimage = models.CharField(max_length=200)
    conference = models.CharField(max_length=200)
    cimage = models.CharField(max_length=200)
    founded = models.CharField(max_length=200)
    rchamp = models.CharField(max_length=200)     # most recent champion
    mchamps = models.CharField(max_length=200)    # most championships
    cnum = models.CharField(max_length=200)  # that number of champs
    # teams

    def __str__(self) :
        return self.division


class Team(models.Model):
    """
    Model for a Team. Attributes contained are: team name, team image, division,
    state, city, stadium, stadium image, coach, year established, years of conference championships,
    years of superbow wins.
    The __str__ function returns the team name as a string.
    """    
    team = models.CharField(max_length=200)
    timage = models.CharField(max_length=400)     
    state = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    stadium = models.CharField(max_length=200)
    simage = models.CharField(max_length=200)
    coach = models.CharField(max_length=200)   
    established = models.CharField(max_length=200)
    cchamps = models.CharField(max_length=200)
    schamps = models.CharField(max_length=200)
    #players


    def __str__(self) :
        return self.team 


class Player(models.Model):    
    """
    Model for a Player. Attributes conatined are: player name, team, number, position, height,
    weight, age, experience in seasons, college, image of player.
    The __str__ function returns the player name as a string.
    """
    name = models.CharField(max_length=200)
    team = models.ForeignKey(Team)
    number = models.CharField()
    position = models.CharField(max_length=2)
    height = models.CharField(max_length=200)
    weight = models.CharField()
    age = models.CharField()
    experience = models.CharField(max_length=200)
    college = models.CharField(max_length=200)
    pimage = models.CharField(max_length=400)

    def __str__(self) :
        return self.name
