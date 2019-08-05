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

# Copy from build step
COPY --from=BUILD /entrypoint/dist/init /entrypoint/init

# Install NGINX
RUN apt-get update -y && \
    apt-get install -y \
        nginx

# Execute the service
WORKDIR /entrypoint
ENTRYPOINT ["init"]