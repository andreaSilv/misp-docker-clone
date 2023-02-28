#!/bin/bash

python3 ./proxy.py > proxy_console 2>&1 &

/usr/bin/supervisord -c /etc/supervisor/conf.d/supervisord.conf