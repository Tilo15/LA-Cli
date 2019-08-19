from la_cli.Commands.New import new
from la_cli.Commands.Run import run
from la_cli.Commands.View import view
from la_cli.Commands.Info import info

import click

@click.group()
def main():
    pass

new(main)
run(main)
view(main)
info(main)

if __name__ == "__main__":
    main()