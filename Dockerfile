FROM alpine:3

VOLUME "/etc/postfix"

RUN apk add --update --no-cache \
    postfix \
    postfix-pgsql

CMD "postfix"

# Idea taken from https://github.com/Mailu/Mailu/blob/master/core/postfix/Dockerfile
HEALTHCHECK --start-period=350s CMD echo QUIT|nc localhost 25|grep "220 .* ESMTP Postfix"
