# -*- coding: utf-8 -*-
"""
E.Cloudmesh.Common.5
fa19-516-168
Example  of demonstrates the use of cloudmesh.common.StopWatch
"""

from cloudmesh.common.StopWatch import StopWatch
from time import sleep

print("Start stopwatch t1 and stop after 5 seconds", )
StopWatch.start("t1")
sleep(5)
StopWatch.stop("t1")
print ("Stopwatch stopped",StopWatch.get("t1"))
