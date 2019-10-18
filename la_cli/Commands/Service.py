from la_cli.Commands import command, assert_in_project
import click

import os

def new_service(path, name):
    # Create the python file
    python = open("{0}/{1}.py".format(path, name), 'w')

    # Save the data
    python.write(PYTHON_TEMPLATE.replace("MyService", name))
    python.close()

@command
@click.argument("name")
def service(name):
    # Only run if we are in a project
    assert_in_project("create a new service")

    # Create the service in the default place
    new_service("Services", name)


PYTHON_TEMPLATE = """
from LibApplication.Service import Service
from LibApplication.Loop.Queue import QueueLoop
from LibApplication.Loop.AsTask import AsTask

@Service
class MyServiceService:

    # Define a loop for tasks to run on
    processLoop = QueueLoop()

    def __init__(self):
        # Start the loop
        self.processLoop.begin_new_thread()

    @AsTask(processLoop)
    def do_processing(self, data):
        # Do work here that wont block the UI
        return data
"""