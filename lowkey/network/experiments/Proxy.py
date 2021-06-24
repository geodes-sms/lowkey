#!/usr/bin/env python
import logging
import sys

from zmq import Context
import zmq 

__author__ = "Istvan David"
__copyright__ = "Copyright 2021, GEODES"
__credits__ = "Eugene Syriani"
__license__ = "GPL-3.0"

"""
Proxy facility providing XSUB/XPUB interfaces.
"""


class Proxy:

    def __init__(self, address="127.0.0.1", xsubPort="5566", xpubPort="5567", loggingLevel=logging.DEBUG):
        logging.basicConfig()
        logging.getLogger().setLevel(loggingLevel)
        
        self.context = Context.instance()
        self.xsubUrl = "tcp://{}:{}".format(address, xsubPort)
        self.xpubUrl = "tcp://{}:{}".format(address, xpubPort)

        self.xpub_xsub_proxy()

    # N publishers to 1 sub; proxy 1 sub to 1 pub; publish to M subscribers
    def xpub_xsub_proxy(self):
        logging.info("Initializing proxy.")

        # Socket subscribing to publishers
        frontend_pubs = self.context.socket(zmq.XSUB)  # @UndefinedVariable
        frontend_pubs.bind(self.xsubUrl)

        # Socket publishing to subscribers
        backend_subs = self.context.socket(zmq.XPUB)  # @UndefinedVariable
        backend_subs.bind(self.xpubUrl)

        logging.info("Proxy established.")
        zmq.proxy(frontend_pubs, backend_subs)  # @UndefinedVariable


if __name__ == "__main__":
    logging.info("Running with arguments: {}.".format(sys.argv))
    if len(sys.argv) == 1:
        Proxy()
    elif len(sys.argv) == 2:
        level_config = {"critical": logging.CRITICAL, "error": logging.ERROR,
                        "warning": logging.WARNING, "debug": logging.DEBUG,
                        "info": logging.INFO, "notset": logging.NOTSET}
        log_level = level_config[''.join(sys.argv[1]).lower()]
        Proxy(loggingLevel=log_level)
    else:
        Proxy()
