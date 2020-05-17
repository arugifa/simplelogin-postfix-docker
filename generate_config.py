"""Generate Postfix configuration files for SimpleLogin."""

import re
import sys
from os import environ
from pathlib import Path

from jinja2 import Environment, FileSystemLoader, StrictUndefined
from jinja2.exceptions import UndefinedError

POSTFIX_DIR = Path('/etc/postfix')
TEMPLATES_DIR = Path('/src/templates')

templates = Environment(loader=FileSystemLoader(TEMPLATES_DIR), undefined=StrictUndefined)  # noqa: E501

for config in ['main.cf', 'pgsql-relay-domains.cf', 'pgsql-transport-maps.cf']:
    with (POSTFIX_DIR / config).open('w') as f:
        template = templates.get_template(config)

        try:
            f.write(template.render(env=environ))
        except UndefinedError as exc:
            missing = re.match(r"'.+' .+ '(.+)'", exc.message)[1]

            print("Impossible to generate Postfix configuration files")
            sys.exit(f"You forgot to define the following environment variable: {missing}")  # noqa: E501
