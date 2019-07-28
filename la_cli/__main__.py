from la_cli.Commands.New import new
from la_cli.Commands.Run import run

import click

@click.group()
def main():
    pass

new(main)
run(main)

if __name__ == "__main__":
    main()