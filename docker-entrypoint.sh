#!/bin/sh

( sleep 12; echo q) | exec /usr/bin/pjsua \
  --log-level 0 --app-log-level 0 \
  --config-file pjsua.conf \
  sip:DOORBELL_EXTENSION@SIP_SERVER_IP
