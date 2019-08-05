# -----------------------------------------------------------------------------
# Stage: BUILD
# -----------------------------------------------------------------------------
FROM python:3.7.3-stretch AS BUILD

COPY entrypoint /entrypoint

WORKDIR entrypoint

RUN pip3 install pyinstaller && \
    pyinstaller --onefile init.py

# -----------------------------------------------------------------------------
# Stage: Final
# -----------------------------------------------------------------------------
FROM debian:buster

# make the "en_US.UTF-8" locale so postgres will be utf-8 enabled by default
RUN set -eux; \
	if [ -f /etc/dpkg/dpkg.cfg.d/docker ]; then \
# if this file exists, we're likely in "debian:xxx-slim", and locales are thus being excluded so we need to remove that exclusion (since we need locales)
		grep -q '/usr/share/locale' /etc/dpkg/dpkg.cfg.d/docker; \
		sed -ri '/\/usr\/share\/locale/d' /etc/dpkg/dpkg.cfg.d/docker; \
		! grep -q '/usr/share/locale' /etc/dpkg/dpkg.cfg.d/docker; \
	fi; \
	apt-get update; apt-get install -y locales; rm -rf /var/lib/apt/lists/*; \
	localedef -i en_US -c -f UTF-8 -A /usr/share/locale/locale.alias en_US.UTF-8
ENV LANG en_US.utf8

RUN apt-get update -y && \
    apt-get install -y \
        lsb-release \
        rsyslog \
        wget \
        gnupg2 && \
    export RELEASE=$(lsb_release -cs) && \
    echo "deb http://apt.postgresql.org/pub/repos/apt/ ${RELEASE}"-pgdg main > /etc/apt/sources.list.d/pgdg.list && \
    wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | apt-key add - && \
    apt-get update -y && \
    apt-get install -y \
      postgresql-11 && \
    rm -rf /var/lib/apt/lists/*

RUN runuser -l postgres -c '/usr/lib/postgresql/11/bin/initdb /var/lib/postgresql/11/data'

# Copy database files
COPY postgresql/*.conf /var/lib/postgresql/11/data/
COPY --from=BUILD /entrypoint/dist/init /entrypoint/init

# Change permissions
RUN chown -R postgres:postgres /var/lib/postgresql/11/data && \
    chmod -R 0700 /var/lib/postgresql/11/data

# Execute the service
WORKDIR /entrypoint
ENTRYPOINT ["init"]
