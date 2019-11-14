# -*- coding: utf-8 -*-
"""
E.Cloudmesh.Common.4
fa19-516-168
Example  of demonstrates the use of cloudmesh.common.Shell
"""

from cloudmesh.common.Shell import Shell

result = Shell.execute('pwd')
print(result)

r=Shell.command_exists('pwd')
print(r)
