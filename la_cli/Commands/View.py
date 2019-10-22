from la_cli.Commands import command, assert_in_project
import click

import os

def new_view(path, name):
    # get the folder that we will put everything in
    folder = os.path.join(path, name)

    # Create the folder
    os.mkdir(folder)

    # Create the python file
    python = open("{0}/__init__.py".format(folder, name), 'w')

    # Save the data
    python.write(PYTHON_TEMPLATE.replace("MyView", name))
    python.close()

    # Create the ui file
    glade = open("{0}/{1}.glade".format(folder, name), 'w')

    # Save the data
    glade.write(GLADE_TEMPLATE.replace("MyView", name))
    glade.close()

@command
@click.argument("name")
def view(name):
    # Only run if we are in a project
    assert_in_project("create a new view")

    # Create the view in the default place
    new_view("Views", name)



PYTHON_TEMPLATE = """
from LibApplication.View.Window import View
from LibApplication.View.Binding import Binding
from LibApplication.Stock.Services.Application import ApplicationService

@View("MyView.glade", "MyView")
class MyView:

    application_service = ApplicationService
    heading = Binding("title", "text")

    def __init__(self):
        self.heading = "MyView Works!"
        self.subheading = self.application_service.application.app_info.name

    @Binding("subtitle", "text")
    def subheading(self, appname):
        return "MyView is a view in the application {0}".format(appname)

"""

GLADE_TEMPLATE = """<?xml version="1.0" encoding="UTF-8"?>
<!-- Generated with glade 3.22.1 -->
<interface>
  <requires lib="gtk+" version="3.20"/>
  <object class="GtkBox" id="MyView">
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
</interface>
"""