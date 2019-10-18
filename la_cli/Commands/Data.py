from la_cli.Commands import command, assert_in_project
import click

import os

def new_data(path, name):
    # Create the python file
    python = open("{0}/{1}.py".format(path, name), 'w')

    # Save the data
    python.write(PYTHON_TEMPLATE.replace("MyData", name))
    python.close()

@command
@click.argument("name")
def data(name):
    # Only run if we are in a project
    assert_in_project("create a new data model")

    # Create the service in the default place
    new_data("Data", name)


PYTHON_TEMPLATE = """
from LibApplication.Stock.Services.Data import Persistable
from LibApplication.Stock.Services.Data.DataModel import DataModel

@Persistable
class MyData(DataModel):
    def __init__(self):
        # Some example fields
        self.name = "Billy"
        self.country = "New Zealand"
"""