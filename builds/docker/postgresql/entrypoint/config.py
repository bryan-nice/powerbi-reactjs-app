import subprocess
import logging

class Setup:
    def __init__(self, arguments):
        self._dbDirectory = arguments.dbDirectory
        self._port = arguments.port

    def _run(self, *args, **kwargs):
        logging.info('running: {}'.format(args))
        subprocess.check_call(*args, **kwargs)

    def arguments(self):
        args = []
        if self._dbDirectory is not None:
            args += [ "-D %s" % self._dbDirectory ]
        if self._port is not None:
            args += [ "-p %s" % self._port ]

        return " ".join(args)