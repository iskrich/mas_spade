# -*- coding: utf-8 -*-

from route import Point, PointStatus
import spade
import logging
log = logging.getLogger(__name__)
from templates import PROPOSAL_TEMPLATE

class DriverAgent(spade.Agent.Agent):

    class ProposeBehaviour(spade.Behaviour.Behaviour):
        def onStart(self):
            self.proposals = {}
            super(DriverAgent.ProposeBehaviour, self).onStart()

        def _process(self):
            from main import city
            msg = self._receive()
            if msg:
                offer_from = msg.content
                offer_distance, offer_plan = city.get_optimal_route_to_point(self.myAgent.routes,
                                                                             Point(offer_from.upper(), PointStatus.DROP),
                                                                             after_stock=True)

                self.proposals[offer_from] = (offer_distance, offer_plan)
                diff = offer_distance - self.myAgent.distance

                reply = spade.ACLMessage.ACLMessage()
                reply.setPerformative('inform')
                reply.addReceiver(msg.sender)
                reply.setSender(self.myAgent.getAID())
                reply.setContent(diff)
                self.myAgent.send(reply)

    class RegisterBehaviour(spade.Behaviour.OneShotBehaviour):
        def _process(self):
            driver_service = spade.DF.ServiceDescription()
            driver_service.setName("Driver")
            driver_service.setType("Delivery")
            driver_agent_description = spade.DF.DfAgentDescription()
            driver_agent_description.addService(driver_service)
            driver_agent_description.setAID(self.myAgent.getAID())
            log.info('Registering driver in DF %s' % self.name)
            res = self.myAgent.registerService(driver_agent_description)
            print('Agent registred in DF %s' % res)
            self.myAgent.addBehaviour(self.myAgent.ProposeBehaviour(), PROPOSAL_TEMPLATE)

    def __init__(self, routes, *args, **kwargs):
        from main import city, stock
        self.address = [routes[0]]
        self.routes = [Point(name, PointStatus.ON_ROAD) for name in routes + self.address]
        self.distance, self.routes = city.get_optimal_route_to_point(self.routes, Point(stock, PointStatus.PICK))

        super(DriverAgent, self).__init__(*args, **kwargs)

    def _setup(self):
        self.addBehaviour(self.RegisterBehaviour())
        print('Driver %s started' % self.name)