import click


@click.group("vault")
@click.pass_context
def entry_point(ctx):
    pass


@entry_point.command("get")
@click.argument("guid")
@click.pass_context
def get_vault(ctx, guid):
    print ctx.obj["passman"].get_vault(guid)


@entry_point.command("list")
@click.pass_context
def get_vaults(ctx):
    print ctx.obj["passman"].get_vaults()
