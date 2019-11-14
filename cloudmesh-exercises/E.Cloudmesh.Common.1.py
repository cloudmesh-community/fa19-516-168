# -*- coding: utf-8 -*-
"""
E.Cloudmesh.Common.1
fa19-516-168
Example  of banner, HEADING, and VERBOSE in cloudmesh 
"""
from cloudmesh.common.util import HEADING
from cloudmesh.common.util import banner
from cloudmesh.common.debug import VERBOSE

# Use of banner
banner("This is my banner using CM");
#Use of heading
HEADING(txt="Heading example using CM", c='$$', color='RED')
#use of verbose
m = {"deepak": "007","dd":"008"}
VERBOSE(m)                              

