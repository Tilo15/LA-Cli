from la_cli.Commands import command
import click

from la_cli.Commands.Window import new_window

import sys
import os
import re


PATHS = [
    "/Views",
    "/Data",
    "/Services",
]

@command
@click.argument("name")
@click.argument("namespace")
def new(name, namespace):
    # Make sure name is valid
    if(re.match('^[\w]+$', name) is None):
        print("Name may only contain alphnumeric characters")
        exit()

    # Make sure namespace is valid
    if(re.match('^[\w.]+$', namespace) is None):
        print("Namespace may only contain alphnumeric characters and periods")
        exit()

    # Create file structure
    os.mkdir(name)
    for path in PATHS:
        os.mkdir(name + path)

    # Create main window
    new_window("{0}/Views".format(name), "MainWindow")

    # Create the app file
    app = open("{0}/__main__.py".format(name), 'w')

    # Save the data
    app.write(APP_TEMPLATE.replace("MyApplication", name))
    app.close()


    
APP_TEMPLATE = """
from LibApplication.App import Application
from LibApplication.App.AppInfo import AppInfo

from MyApplication.Views.MainWindow import MainWindow

class MyApplication(Application):

    app_info = AppInfo("MyApplicationNamespace", 0.1, "MyApplication")

    def start(self):
        self.main_window = MainWindow()
        self.main_window.show()


if __name__ == "__main__":
    MyApplication()

"""
    