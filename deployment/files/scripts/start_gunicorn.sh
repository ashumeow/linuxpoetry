#!/usr/bin/env sh
cd /var/projects/linuxpoetry/code
../env/bin/gunicorn poetry:application -b 0.0.0.0:80
