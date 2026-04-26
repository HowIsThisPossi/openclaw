"""Command-line interface for OpenClaw."""

import click
from . import __version__

@click.group()
@click.version_option(version=__version__)
def main():
    """OpenClaw - A powerful command-line tool for managing and organizing your projects."""
    pass

@main.command()
@click.option('--name', default='OpenClaw', help='Name to greet.')
def hello(name):
    """Greet with OpenClaw."""
    click.echo(f"Hello from {name}! 🐾")

@main.command()
def version():
    """Show OpenClaw version."""
    click.echo(f"OpenClaw version {__version__}")

@main.command()
@click.option('-v', '--verbose', is_flag=True, help='Verbose output.')
def status(verbose):
    """Check OpenClaw status."""
    click.echo("✅ OpenClaw is running smoothly!")
    if verbose:
        click.echo("📍 Status: Active")
        click.echo(f"📦 Version: {__version__}")

if __name__ == '__main__':
    main()
