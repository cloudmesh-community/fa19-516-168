# -*- coding: utf-8 -*-
"""
E.Cloudmesh.Common.3
fa19-516-168
Example  of demonstrates the use of FlatDict
# FlatDict flatten out dictionaries that contain dicts within dicts
"""
from cloudmesh.common.FlatDict import FlatDict


city = {
"cityid": "DFW",
"city":{
        "name":"Dallas",
        "stateID":"TX",
        "State":"Texas"
        }
        }

flat = FlatDict(city, sep=".")
print("Print city dict - \n",city,"\n")
print("pring flat city dict using .sep -\n",flat)
