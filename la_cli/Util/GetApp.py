import importlib
import os
import sys
import inspect

from LibApplication.App import Application


def get_app():
    # Where are we?
    working_dir = os.getcwd()

    # What is the app called?
    module_name = os.path.basename(working_dir) + ".__main__"

    # Move up one
    up = os.path.dirname(working_dir)

    sys.path.insert(1, up)

    module = importlib.import_module(module_name)

    direct_members = [x[1] for x in inspect.getmembers(module) if hasattr(x[1], "__module__") and x[1].__module__ == module_name]

    app = None

    for member in direct_members:
        if(issubclass(member, Application)):
            if(app != None):
                print("An application's __main__.py file must not contain more than one class inheriting from LibApplication.App.Application.")
                exit()

            app = member

    return app