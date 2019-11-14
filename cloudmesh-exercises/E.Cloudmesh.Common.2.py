# -*- coding: utf-8 -*-
"""
E.Cloudmesh.Common.2
fa19-516-168
Example  of program that demonstrates the use of dotdict. 
# dotdist simply notation of . instead od []. Bth notation give same result
"""
from cloudmesh.common.dotdict import dotdict


city = {
"name": "Dallas"
}

city = dotdict(city)
print("Following is city dict-",city)
print("Print city name from dict using . notation -",city.name)
print("Print city name from dict using [] notation -",city["name"])