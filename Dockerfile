FROM alpine:3

EXPOSE 25

RUN apk add --update --no-cache \
    postfix postfix-pgsql \
    python3

ADD templates /src/templates
ADD generate_config.py /src/

RUN python3 -m ensurepip
RUN pip3 install jinja2

WORKDIR /src
CMD python3 generate_config.py && postfix start-fg

# Idea taken from https://github.com/Mailu/Mailu/blob/master/core/postfix/Dockerfile
HEALTHCHECK --start-period=350s CMD echo QUIT|nc localhost 25|grep "220 .* ESMTP Postfix"
