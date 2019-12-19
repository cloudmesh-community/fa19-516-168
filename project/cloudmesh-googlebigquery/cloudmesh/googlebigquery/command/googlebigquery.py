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
        bigquery create [DATASET_ID]
        bigquery list [PROJECT_ID]
        bigquery delete [DATASET_ID]
        bigquery listtables PROJECT_ID DATASET_ID
        #bigquery deletetable PROJECT_ID DATASET_ID [TABLE_ID]
        #bigquery insert into table
        bigquery loadtable SOURCE PROJECT_ID DATASET_ID [TABLE_ID]
        bigquery exporttable SOURCE PROJECT_ID DATASET_ID [TABLE_ID]
        bigquery runquery PROJECT_ID DATASET_ID [TABLE_ID]
        bigquery listjob [PROJECT_ID]


        Arguments:
            DATASET_ID              The Google bigquery dataset id.
            PROJECT_ID              The google big query project id
            TABLE_NAME              The name of the table
            JOB_ID                  The job id in bigquery
            SOURCE                  Local file which need to be load into bigquery table
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
