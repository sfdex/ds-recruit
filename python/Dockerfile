FROM python:3.9-alpine

WORKDIR /srv

# python:3.9-alpine未内置make，下面的改动是将make添加进去
RUN apk add --no-cache make