from la_cli.Commands import command
from la_cli.Util import GetApp
import click

import os

@command
def run():
    # Where are we?
    working_dir = os.getcwd()

    # What is the app called?
    app = os.path.basename(working_dir)

    # Move up one
    up = os.path.dirname(working_dir)

    # Run program
    #os.system("cd {0}; python3 -m {1}".format(up, app))

    app = GetApp.get_app()
    app()

