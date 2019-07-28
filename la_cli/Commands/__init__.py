import click


def command(func):
    def constructor(group):
        return group.command()(func)

    return constructor