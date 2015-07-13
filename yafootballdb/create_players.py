from yafbdb.models import *
import json

with open('../json_data/players.json') as f:
	players_cache = json.load(f)
	assert hasattr(players_cache,'__iter__')
	print (len(players_cache))

assert(len(players_cache) != 0)

for player_cache in players_cache:
    
    print(player_cache)
    w = player_cache["team"]
    print(w)
    q = 0
    q =Player(name=player_cache["pname"],
        team=Team.objects.get(team=player_cache["team"]),
        #team=player_cache["team"],
        number=player_cache["number"],
        position=player_cache["position"],
        height=player_cache["height"],
        weight=player_cache["weight"],
        age=player_cache["age"],
        experience=player_cache["experience"],
        college=player_cache["college"],
        pimage=player_cache["pimage"])
    q.save()
    