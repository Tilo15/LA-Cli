import click
import os


def command(func):
    def constructor(group):
        return group.command()(func)

    return constructor


def assert_in_project(action):
    if(not os.path.exists("__main__.py")):
        print("Could not detect a __main__.py in the current directiory. Your working directiory must contain a project to {0}.".format(action))
        exit()