from la_cli.Commands import command, assert_in_project
from la_cli.Util import GetApp
import click

@command
def info():
    # Can only check info if we are in the project
    assert_in_project("view info")

    # Get the app
    app = GetApp.get_app()

    print("\n")
    print("Namespace: {0}".format(app.app_info.namespace))
    print("Version: {0}".format(app.app_info.version))
    print("Name: {0}".format(app.app_info.name))
    print("Authors: {0}".format(", ".join(app.app_info.authors)))
    print("Licence: {0}".format(app.app_info.licence))
    print("Short Description: {0}".format(app.app_info.short_description))
    print("Description: {0}".format(app.app_info.description))
    print("\n")


