from la_cli.Commands import command, assert_in_project
from la_cli.Util import GetApp

from LibApplication.Stock.Services.Data import DataService
from LibApplication.Stock.Views.DataWindow import DataWindow
from LibApplication.Stock.Views.MessageBox import MessageBox

import click

@command
def browse():
    # Can only check info if we are in the project
    assert_in_project("browse data")

    # Get the app
    app = GetApp.get_app()

    # Declare the data window variable
    data_window = None

    def error(exception):
        MessageBox("Unable to retreive data", "The database may not be initialised, or there may not be a root object to inspect.").show_modal(data_window)

    # Extend the app to run the data viewer instead of the main window
    class viewer_app(app):
        def prepare(self):
            # Nothing to prepare
            pass

        def start(self):
            nonlocal data_window
            print("start")

            # Construct the data window
            data_window = DataWindow()
            data_window.show()

        def ready(self):
            nonlocal data_window

            print("ready")
            # Query data service for root object
            DataService.get_instance().get().subscribe(data_window.set_root, error)


    # Run the app
    viewer_app()


