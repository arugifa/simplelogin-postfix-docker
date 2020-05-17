# Docker Image for SimpleLogin Postfix

No official Postfix image, tailor-made for [SimpleLogin](https://simplelogin.io/),
currently exists.

Let's fix that, by providing to the community something very lightweight and simple to use 💖

Can be configured with the following environment variables:

Setting     | Description
----------- | -------------------------------------------
**ALIASES_DOMAIN** | Default domain to use for your aliases.
**DB_HOST** | Where is hosted the PostgreSQL database.
**DB_USER** | User to connect to the PostgreSQL database.
**DB_PASSWORD** | User's password to connect to the PostgreSQL database.
**DB_NAME** | Name of the PostgreSQL database.
**EMAIL_HANDLER_HOST** | Where is hosted your SimpleLogin email handler instance.
**SIMPLELOGIN_HOST** | Where is hosted your SimpleLogin instance.

Used by and made for [Kloügle](https://github.com/arugifa/klougle), the Google
alternative automated with [Terraform](https://www.terraform.io/).
