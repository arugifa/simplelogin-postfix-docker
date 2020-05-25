#!/usr/bin/env sh
set -e

/src/generate_config.py --postfix
postfix reload
