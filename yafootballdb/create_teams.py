from yafbdb.models import *
import json

with open('../json_data/teams2.json') as f:
	teams_cache = json.load(f)
	assert hasattr(teams_cache,'__iter__')
	print (len(teams_cache))

assert(len(teams_cache) != 0)

for team_cache in teams_cache:
    print(team_cache)
    q = 0
    q =Team(team=team_cache["team"].replace(".","").replace("'","").replace("-",""),
        division=Division.objects.get(division=team_cache["division"]),
        timage=team_cache["timage"],
        state=team_cache["state"],
        city=team_cache["city"],
        stadium=team_cache["stadium"],
        simage=team_cache["simage"],
        coach=team_cache["coach"],
        established=team_cache["established"],
        cchamps=team_cache["cchamps"],
        schamps=team_cache["schamps"],
        twitter=team_cache["twitter"])
    q.save()

#for team_cache in teams_cache:
 #   print(team_cache)
#    q = 0
 #   q =Team(team=team_cache["team"],
 #   	division=Division.objects.get(division=team_cache["division"]),
 #   	timage=team_cache["timage"],
  #  	state=team_cache["state"],
 #   	city=team_cache["city"],
 #   	stadium=team_cache["stadium"],
 #   	simage=team_cache["simage"],
 #   	coach=team_cache["coach"],
 #   	established=team_cache["established"],
 #   	cchamps=team_cache["cchamps"],
 #   	schamps=team_cache["schamps"])
 #   q.save()
    
# save()
