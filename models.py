from django.db import models


class Division(models.Model):
    """
    Model for a Division. Attributes conatined are : division name, division image,
    conference name, lague name, sport, year founded, member teams, most recent champion,
    team with most championships.
    The __str__ function returns the division name as a string.
    """
    division = models.CharField(max_length=200,default="default")
    dimage = models.CharField(max_length=200,default="default")
    conference = models.CharField(max_length=200,default="default")
    cimage = models.CharField(max_length=200,default="default")
    founded = models.CharField(max_length=200,default="default")
    rchamp = models.CharField(max_length=200,default="default")     # most recent champion
    mchamps = models.CharField(max_length=200,default="default")    # most championships
    cnum = models.CharField(max_length=200,default="default")  # the number of championships
    

    def __str__(self) :
        return self.division


class Team(models.Model):
    """
    Model for a Team. Attributes contained are: team name, team image, division,
    state, city, stadium, stadium image, coach, year established, years of conference championships,
    years of superbow wins.
    The __str__ function returns the team name as a string.
    """    
    team = models.CharField(max_length=200,default="default")
    division = models.ForeignKey(Division)
    timage = models.CharField(max_length=400,default="default")
    state = models.CharField(max_length=200,default="default")
    city = models.CharField(max_length=200,default="default")
    stadium = models.CharField(max_length=200,default="default")
    simage = models.CharField(max_length=200,default="default")
    coach = models.CharField(max_length=200,default="default")
    established = models.CharField(max_length=200,default="default")
    cchamps = models.CharField(max_length=200,default="default")
    schamps = models.CharField(max_length=200,default="default")


    def __str__(self) :
        return self.team 


class Player(models.Model):    
    """
    Model for a Player. Attributes conatined are: player name, team, number, position, height,
    weight, age, experience in seasons, college, image of player.
    The __str__ function returns the player name as a string.
    """
    name = models.CharField(max_length=200,default="default")
    team = models.ForeignKey(Team)
    number = models.CharField(max_length=200,default="default")
    position = models.CharField(max_length=2,default="default")
    height = models.CharField(max_length=200,default="default")
    weight = models.CharField(max_length=200,default="default")
    age = models.CharField(max_length=200,default="default")
    experience = models.CharField(max_length=200,default="default")
    college = models.CharField(max_length=200,default="default")
    pimage = models.CharField(max_length=400,default="default")

    def __str__(self) :
        return self.name
