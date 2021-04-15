#!/usr/bin/env sh
set -e

CERTIFICATE="/etc/letsencrypt/live/$POSTFIX_FQDN/fullchain.pem"
PRIVATE_KEY="/etc/letsencrypt/live/$POSTFIX_FQDN/privkey.pem"

if [ -f $CERTIFICATE -a -f $PRIVATE_KEY ]; then
    certbot -q renew
else
    certbot -q certonly
fi
