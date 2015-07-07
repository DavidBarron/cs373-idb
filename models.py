from django.db import models


class Division(models.Model):
    """
    Model for a Division. Attributes conatined are : division name, division image,
    conference name, lague name, sport, year founded, member teams, most recent champion,
    team with most championships.
    The __str__ function returns the division name as a string.
    """
    division = models.CharField(max_length=200)
    division_image = models.CharField(max_length=200)
    conference = models.CharField(max_length=200)
    league = models.CharField(max_length=200)
    sport = models.CharField(max_length=200)
    founded = models.CharField(max_length=200)
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
    team = models.CharField(max_length=200)
    team_image = models.CharField(max_length=400)     
    division = models.ForeignKey(Division) 
    state = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    stadium = models.CharField(max_length=200)
    stadium_image = models.DateField()
    coach = models.CharField(max_length=200)     
    established = models.CharField(max_length=200)
    conference_champs = models.CharField(max_length=200)
    superbowl_champs = models.CharField(max_length=200)


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
    number = models.IntegerField()
    position = models.CharField(max_length=2)
    height = models.CharField(max_length=200)
    weight = models.FloatField()
    age = models.FloatField()
    experience = models.CharField(max_length=200)
    college = models.CharField(max_length=200)
    player_image = models.CharField(max_length=400)

    def __str__(self) :
        return self.name

    
>>>>>>> master
