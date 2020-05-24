# Docker Image for SimpleLogin Postfix

No official Postfix image, tailor-made for [SimpleLogin](https://simplelogin.io/),
currently exists.

Let's fix that, by providing to the community something very lightweight,
secure (with [Let's Encrypt](https://letsencrypt.org/) support) and simple to use 💖

Can be configured with the following environment variables:

Setting     | Description
----------- | -------------------------------------------
**ALIASES_DEFAULT_DOMAIN** | Default domain to use for your aliases.
**DB_HOST** | Where is hosted your SimpleLogin PostgreSQL database.
**DB_USER** | User to connect to the database.
**DB_PASSWORD** | User's password to connect to the database.
**DB_NAME** | Name of the database.
**EMAIL_HANDLER_HOST** | Where is hosted your SimpleLogin email handler instance.
**LETSENCRYPT_EMAIL** | Email address used by Let's Encrypt, to send you expiry notices\*.
**POSTFIX_FQDN** | Fully Qualified Domain Name of your Postfix instance (i.e., the MX server address you configured in your DNS zone for your **ALIASES_DEFAULT_DOMAIN**).

\* automatic renewal is managed with [Certbot](https://certbot.eff.org/) and shouldn't fail, unless you have reached Let's Encrypt [rate limits](https://letsencrypt.org/docs/rate-limits/)

Used by and made for [Kloügle](https://github.com/arugifa/klougle), the Google
alternative automated with [Terraform](https://www.terraform.io/).
