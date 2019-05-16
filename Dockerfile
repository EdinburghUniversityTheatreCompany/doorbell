FROM alpine:latest

RUN apk add --update pjsua python3 \
&&  rm -rf /var/cache/apk/* /tmp/* /var/tmp/*

COPY pjsua.conf           /pjsua.conf
COPY docker-entrypoint.sh /docker-entrypoint.sh
COPY autocaller.py /autocaller.py
COPY /short.wav /tmp/message.wav

CMD ["/usr/bin/python3", "autocaller.py"]
HEALTHCHECK --interval=1m CMD /usr/bin/python3 healthcheck.py
