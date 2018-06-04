from spade.Agent import Agent
import logging

log = logging.getLogger(__name__)
log.setLevel(logging.INFO)


class PedestrianAgent(Agent):

    def _setup(self):
        log.info('Agent %s started' % self.name)