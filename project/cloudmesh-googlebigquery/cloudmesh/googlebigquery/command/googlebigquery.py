from __future__ import print_function
from cloudmesh.shell.command import command
from cloudmesh.shell.command import PluginCommand
from cloudmesh.googlebigquery.api.manager import Manager
from cloudmesh.common.console import Console
from cloudmesh.common.util import path_expand
from pprint import pprint
from cloudmesh.common.debug import VERBOSE

class GooglebigqueryCommand(PluginCommand):

    # noinspection PyUnusedLocal
    @command
    def do_googlebigquery(self, args, arguments):
        """
        ::

        Usage:
        bigquery create dataset
        bigquery list dataset
        bigquery create table
        bigquery list tables
        bigquery delete table
        bigquery insert into table
        bigquery load table
        bigquery runquery
        bigquery create job
        bigquery list jobs
        bigquery schedule job
        bigquery run job
        """
        arguments.FILE = arguments['--file'] or None

        VERBOSE(arguments)

        m = Manager()

        if arguments.FILE:
            print("option a")
            m.list(path_expand(arguments.FILE))

        elif arguments.list:
            print("option b")
            m.list("just calling list without parameter")

        Console.error("This is just a sample")
        return ""
