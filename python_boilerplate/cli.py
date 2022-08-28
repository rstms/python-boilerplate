"""Console script for python_boilerplate."""

import sys

import click

from .version import __version__, __timestamp__
from .exception_handler import ExceptionHandler

header = f"{__name__.split('.')[0]} v{__version__} {__timestamp__}"


@click.command("python_boilerplate")
@click.version_option(message=header)
@click.option("-d", "--debug", is_flag=True, help="debug mode")
@click.pass_context
def cli(ctx, debug):

    ctx.obj = dict(ehandler = ExceptionHandler(debug))

    """cli for python_boilerplate."""
    raise RuntimeError("Add application code to python_boilerplate/cli.py")
    return 0


if __name__ == "__main__":
    sys.exit(cli())  # pragma: no cover
