#!/usr/bin/env python3
"""Generate configuration files for SimpleLogin Postfix and Certbot.

Greatly inspired by:
https://aoeex.com/phile/postfix-dovecot-and-lets-encrypt-certificates/
"""

import re
import sys
from os import environ
from pathlib import Path

from jinja2 import Environment, FileSystemLoader, StrictUndefined
from jinja2.exceptions import UndefinedError

# Certbot
CERTBOT_CONFIG_DIR = Path('/etc/letsencrypt')
CERTBOT_CONFIG_FILENAME = 'cli.ini'

# Let's Encrypt
LETSENCRYPT_CONFIG_DIR = CERTBOT_CONFIG_DIR / 'live'
LETSENCRYPT_CERTIFICATE = 'fullchain.pem'
LETSENCRYPT_PRIVATE_KEY = 'privkey.pem'

# Postfix
POSTFIX_CONFIG_DIR = Path('/etc/postfix')
POSTFIX_CONFIG_FILENAMES = ['main.cf', 'pgsql-relay-domains.cf', 'pgsql-transport-maps.cf']  # noqa: E501

# Templates
TEMPLATES_DIR = Path('/src/templates')

templates = Environment(
    loader=FileSystemLoader(TEMPLATES_DIR),
    undefined=StrictUndefined,
    trim_blocks=True,  # To not show empty lines in place of block statements
)


def generate_certbot_config():
    """Generate Certbot's configuration file."""
    with (CERTBOT_CONFIG_DIR / CERTBOT_CONFIG_FILENAME).open('w') as f:
        template = templates.get_template(f'certbot/{CERTBOT_CONFIG_FILENAME}')
        f.write(template.render(env=environ))


def generate_postfix_config():
    """Generate Postfix's configuration files."""
    for config in POSTFIX_CONFIG_FILENAMES:
        with (POSTFIX_CONFIG_DIR / config).open('w') as f:
            template = templates.get_template(f'postfix/{config}')

            # Check if Certbot generated a TLS certificate.
            postfix_fqdn = environ['POSTFIX_FQDN']
            cert_file = LETSENCRYPT_CONFIG_DIR / postfix_fqdn / LETSENCRYPT_CERTIFICATE
            key_file = LETSENCRYPT_CONFIG_DIR / postfix_fqdn / LETSENCRYPT_PRIVATE_KEY

            enable_tls = cert_file.is_file() and key_file.is_file()

            # Generate config file.
            f.write(template.render(
                env=environ,
                tls=enable_tls,
                tls_cert=cert_file,
                tls_key=key_file,
            ))


def main():
    """Generate Certbot and/or Postfix's configuration files."""
    try:
        if '--certbot' in sys.argv or len(sys.argv) == 1:
            generate_certbot_config()

        if '--postfix' in sys.argv or len(sys.argv) == 1:
            generate_postfix_config()

    except (KeyError, UndefinedError) as exc:
        if isinstance(exc, KeyError):
            missing = exc.args[0]
        else:
            missing = re.match(r"'.+' .+ '(.+)'", exc.message)[1]

        print("Impossible to generate Postfix configuration files")
        sys.exit(f"You forgot to define the following environment variable: {missing}")


if __name__ == '__main__':
    main()
