from spade.Agent import Agent
from driver import DriverAgent
from pedestrian import PedestrianAgent

class CreatorAgent(Agent):

    def _setup(self):
        from main import platform_server, routes
        self.agents = []
        for route in routes:
            if len(route) == 1:
                self.agents.append(PedestrianAgent(agentjid='pedestrian-%s@%s' % (route[0].lower() , platform_server),
                                                   password='secret'))
            else:
                self.agents.append(DriverAgent(routes=route[1:],
                                               agentjid='driver-%s@%s' % (route[0].lower() , platform_server),
                                               password='secret'))
        for agent in self.agents:
            agent.start()
