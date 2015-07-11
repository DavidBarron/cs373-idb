from yafbdb.models import *
import json

with open('../json_data/divisions.json') as f:
	divisions_cache = json.load(f)
	assert hasattr(divisions_cache,'__iter__')
	print (len(divisions_cache))

assert(len(divisions_cache) != 0)

for div_cache in divisions_cache:
    print(div_cache)
    q = 0
    q =Division(division=div_cache["division"], dimage=div_cache["dimage"], conference=div_cache["conference"], cimage=div_cache["cimage"], founded=div_cache["founded"], rchamp=div_cache["rchamp"], mchamps=div_cache["mchamps"], cnum=div_cache["cnum"])
    q.save()
    
# save()
