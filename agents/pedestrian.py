# -*- coding: utf-8 -*-

import spade
import logging
from templates import BID_TEMPLATE

log = logging.getLogger(__name__)
log.setLevel(logging.INFO)


class PedestrianAgent(spade.Agent.Agent):
    def __init__(self, address, *args, **kwargs):
        self.address = address
        self.driver_dialogs = {}
        super(PedestrianAgent, self).__init__(*args, **kwargs)


    class ChooseBest(spade.Behaviour.Behaviour):
        def _process(self):
            msg = self._receive()
            if msg:
                pass


    class SendingBehaviour(spade.Behaviour.OneShotBehaviour):
        def _process(self):
            description = spade.DF.DfAgentDescription()
            service = spade.DF.ServiceDescription()
            service.setName('Driver')
            service.setType('Delivery')
            description.addService(service)
            search = self.myAgent.searchService(description)

            for agent in search:
                msg = spade.ACLMessage.ACLMessage()
                msg.setPerformative('cfp')
                msg.addReceiver(agent.name)
                msg.setSender(self.myAgent.getAID())
                msg.setContent(self.myAgent.address)
                self.myAgent.send(msg)
                self.myAgent.driver_dialogs[msg.getConversationId()] = agent.name

            self.myAgent.drivers_count = len(search)
            self.myAgent.addBehaviour(self.myAgent.ChooseBest(), BID_TEMPLATE)

    def _setup(self):
        log.info('Agent %s started' % self.name)
        self.addBehaviour(self.SendingBehaviour())