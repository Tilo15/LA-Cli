from la_cli.Commands.New import new
from la_cli.Commands.Run import run
from la_cli.Commands.View import view
from la_cli.Commands.Info import info
from la_cli.Commands.Data import data
from la_cli.Commands.Service import service

import click

@click.group()
def main():
    pass

new(main)
run(main)
view(main)
info(main)
service(main)
data(main)

if __name__ == "__main__":
    main()