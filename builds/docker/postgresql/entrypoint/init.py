#!/usr/bin/env python

import sys
import os
import subprocess
import config
import logging
import parser
import time

logging.basicConfig(stream=sys.stdout, level=logging.DEBUG, format="%(message)s")

try:
    arguments = parser.parse()
    setup = config.Setup(arguments)
    # Start container logging so it is exposed
    syslog_service_cmd = "service rsyslog start"
    syslog_check = subprocess.Popen(syslog_service_cmd,stdout=subprocess.PIPE,stderr=subprocess.PIPE,shell=True)
    while syslog_check.poll() is None:
        # Process hasn't exited yet, let's wait some
        time.sleep(0.5)
    if syslog_check.returncode == 0:
        # Start Postgres Database as postgres user
        postgresql = "runuser -l postgres -c '/usr/lib/postgresql/11/bin/postgres %s' &" % setup.arguments()
        postgresql_check = subprocess.Popen(postgresql,stdout=subprocess.PIPE,stderr=subprocess.PIPE,shell=True)
        while postgresql_check.poll() is None:
            # Process hasn't exited yet, let's wait some
            time.sleep(0.5)
        if postgresql_check.returncode == 0:
            # Execute database init for g2
            initdb_cmd = "runuser -l postgres -c 'psql -c \"CREATE DATABASE \\\"G2\\\"\"; psql -d \"G2\" -f /var/lib/postgresql/11/g2-db-init-files/g2core-schema-postgresql-create.sql'"
            initdb_check = subprocess.Popen(initdb_cmd,stdout=subprocess.PIPE,stderr=subprocess.PIPE,shell=True)
            while initdb_check.poll() is None:
                # Process hasn't exited yet, let's wait some
                time.sleep(0.5)

            # Verify initdb for G2 succeeded
            if initdb_check.returncode == 0:
                # Output syslog to container logging
                os.system("tail -f /var/log/syslog")
            else:
                logging.exception("Unable to initialize postgresql with G2 definition.")
        else:
            logging.exception("Postgresql was not able to start.")
    else:
        logging.exception("System logging could not be initialized.")
except:
    logging.exception("failed!")
