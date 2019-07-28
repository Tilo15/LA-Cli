from la_cli.Commands import command
import click

import os


def new_window(path, name):
    # get the folder that we will put everything in
    folder = os.path.join(path, name)

    # Create the folder
    os.mkdir(folder)

    # Create the python file
    python = open("{0}/__init__.py".format(folder, name), 'w')

    # Save the data
    python.write(PYTHON_TEMPLATE.replace("MyWindow", name))
    python.close()

    # Create the ui file
    glade = open("{0}/{1}.glade".format(folder, name), 'w')

    # Save the data
    glade.write(GLADE_TEMPLATE.replace("MyWindow", name))
    glade.close()


PYTHON_TEMPLATE = """
from LibApplication.View.Window import WindowView
from LibApplication.View.Binding import Binding, FormattedBinding
from LibApplication.Stock.Services.Application import ApplicationService

@WindowView("MyWindow.glade", "MyWindow")
class MyWindow:

    application_service = ApplicationService
    heading = Binding("title", "text")

    def __init__(self):
        self.heading = "MyWindow Works!"
        self.subheading = self.application_service.application.app_info.name

    @FormattedBinding("subtitle", "text")
    def subheading(self, appname):
        return "MyWindow is a toplevel view in the application {0}".format(appname)

"""

GLADE_TEMPLATE = """
<?xml version="1.0" encoding="UTF-8"?>
<interface>
  <requires lib="gtk+" version="3.20"/>
  <object class="GtkWindow" id="MyWindow">
    <property name="width_request">600</property>
    <property name="height_request">200</property>
    <property name="can_focus">False</property>
    <property name="title" translatable="yes">MyWindow</property>
    <child>
      <placeholder/>
    </child>
    <child>
      <object class="GtkBox">
        <property name="visible">True</property>
        <property name="can_focus">False</property>
        <property name="halign">center</property>
        <property name="valign">center</property>
        <property name="margin_left">18</property>
        <property name="margin_right">18</property>
        <property name="margin_top">18</property>
        <property name="margin_bottom">18</property>
        <property name="orientation">vertical</property>
        <child>
          <object class="GtkLabel" id="title">
            <property name="visible">True</property>
            <property name="can_focus">False</property>
            <property name="halign">start</property>
            <property name="margin_bottom">6</property>
            <property name="label" translatable="yes">Title</property>
            <attributes>
              <attribute name="weight" value="bold"/>
              <attribute name="scale" value="1.2"/>
            </attributes>
          </object>
          <packing>
            <property name="expand">False</property>
            <property name="fill">True</property>
            <property name="position">0</property>
          </packing>
        </child>
        <child>
          <object class="GtkLabel" id="subtitle">
            <property name="visible">True</property>
            <property name="can_focus">False</property>
            <property name="halign">start</property>
            <property name="label" translatable="yes">Subtitle</property>
          </object>
          <packing>
            <property name="expand">False</property>
            <property name="fill">True</property>
            <property name="position">1</property>
          </packing>
        </child>
      </object>
    </child>
  </object>
</interface>
"""