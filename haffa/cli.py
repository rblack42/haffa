import click

import click


@click.group()
@click.version_option()
def cli():
    """HAFFA SVG Builder.
    This program generates SVG files for club use.
    At present you can build a basic logo, a badge,
    or a membership card"""


@cli.group()
def logo():
    """Create bare logo file"""


@logo.command("new")
@click.argument("name")
@click.option("--name", default="logo.svg", help="Output file name")
@click.option("--size", default=500, help="Size of logo in pixels.")
def logo_new(name):
    """Creates a new ship."""
    click.echo(f"Created logo file {name}")

@cli.group("badge")
def badge():
    """Manages mines."""

@badge.command()
@click.argument("name")
@click.option("--name", default="Fred Flintstone", help="Name on card.")
def single(name):
    """Create a badge file."""
    click.echo("Creating badge file: %s" % name)


@cli.group("card")
def card():
    """Creates membership cards"""

@card.command("single")
@click.argument("name")
def single(name):
    """Generate a single membership card."""
    click.echo("Create a card for the given name: %s" % name)

@card.command("list")
def list():
    """Generate cards from membership list."""
    click.echo("Create cards from the current membership list")
