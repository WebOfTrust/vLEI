import signal

from hio.base import doing, Doist
from keri import help

logger = help.ogler.getLogger()

class GracefulShutdownDoer(doing.Doer):
    """
    Shuts all Agency agents down before exiting the Doist loop, performing a graceful shutdown.
    Sets up signal handlers in the Doer.enter lifecycle method and exits the Doist scheduler loop in Doer.exit
    Checks for the signals in the Doer.recur lifecycle method.
    """
    def __init__(self, doist, **kwa):
        """
        Parameters:
            doist (Doist): The Doist running this Doer
            kwa (dict): Additional keyword arguments for Doer initialization
        """
        self.doist: Doist = doist
        self.shutdown_received = False

        super().__init__(**kwa)

    def handle_sigterm(self, signum, frame):
        """Handler function for SIGTERM"""
        logger.info(f"Received SIGTERM, initiating graceful shutdown.")
        self.shutdown_received = True

    def handle_sigint(self, signum, frame):
        """Handler function for SIGINT"""
        logger.info(f"Received SIGINT, initiating graceful shutdown.")
        self.shutdown_received = True

    def enter(self):
        """
        Sets up signal handlers.
        Lifecycle method called once when the Doist running this Doer enters the context for this Doer.
        """
        # Register signal handler
        signal.signal(signal.SIGTERM, self.handle_sigterm)
        signal.signal(signal.SIGINT, self.handle_sigint)
        logger.info("Registered signal handlers for SIGTERM and SIGINT")

    def recur(self, tock=0.0):
        """Generator coroutine checking once per tock for shutdown flag"""
        # Checks once per tock if the shutdown flag has been set and if so initiates the shutdown process
        while not self.shutdown_received:
            yield tock # will iterate forever in here until shutdown flag set

        # Once shutdown_flag is set, exit the Doist loop
        return True # Returns a "done" status
        # Causes the Doist scheduler to call .exit() lifecycle method below, killing the doist loop

    def exit(self):
        """
        Exits the Doist loop.
        Lifecycle method called once when the Doist running this Doer exits the context for this Doer.
        """
        logger.info(f"Shutting down main Doist loop")
        self.doist.exit()