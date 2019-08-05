#!/usr/bin/env python

import sys
import subprocess
import config
import logging
import parser
import time

logging.basicConfig(stream=sys.stdout, level=logging.DEBUG, format="%(message)s")

try:
    arguments = parser.parse()
    setup = config.Setup(arguments)

    # Start nginx
    nginx_service_cmd = "nginx -g 'daemon off;'"
    nginx_check = subprocess.Popen(nginx_service_cmd,stdout=subprocess.PIPE,stderr=subprocess.PIPE,shell=True)
    while nginx_check.poll() is None:
        # Process hasn't exited yet, let's wait some
        time.sleep(0.5)
    if nginx_check.returncode != 0:
        logging.exception("NGINX could not be initialized.")
except:
    logging.exception("failed!")
