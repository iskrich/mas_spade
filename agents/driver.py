from spade.Agent import Agent
import logging

log = logging.getLogger(__name__)
log.setLevel(logging.INFO)

class DriverAgent(Agent):
    def __init__(self, routes, *args, **kwargs):
        self.routes = routes
        super(DriverAgent, self).__init__(*args, **kwargs)

    def _setup(self):
        log.info('Agent %s started' % self.name)