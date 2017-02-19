# Passman CLI

A CLI to access data from a [Passman](https://github.com/nextcloud/passman) instance.

## Installation

- Install `pip` with `[sudo] easy_install pip`, in case you don't have it yet.
- Run `[sudo] pip install passman_cli`

## Usage

To learn more about the usage please run `passman_cli --help`.

## Config File

Passman CLI supports a [TOML]() config file to save the base url of the instance
and your username and password. You can send a path to the config file using the
`--config` option of the command-line. It also looks for a config named
`passman_cli.toml` at the current working dir and at `~/.config/`, in this exact
order.

Here's an example of configuration:

```toml
base_url = "https://my.nextcloud/apps/passman/api/v2"
auth = ["admin", "password"]
```
