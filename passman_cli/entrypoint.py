import json
import click
import toml
from cli import vault, credential
from api import PassmanApi
from config import find_config


@click.group()
@click.option("--config", "-c", type=click.Path(),  help="Path to config file")
@click.option("--base_url", required=False, help="Url to the Passman API")
@click.option("--user", "-u", required=False, help="Passman user")
@click.option("--password", "-p", required=False, help="Passman password")
@click.pass_context
def entrypoint(ctx, config, base_url, user, password):
    config_file = find_config(config)
    if config_file:
        ctx.obj["passman"] = PassmanApi(**toml.load(config_file))
    else:
        ctx.obj["passman"] = PassmanApi(base_url, (user, password))


def main():
    entrypoint.add_command(vault.entry_point)
    entrypoint.add_command(credential.entry_point)
    entrypoint(obj={})


if __name__ == '__main__':
    main()
