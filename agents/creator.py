from spade.Agent import Agent
from driver import DriverAgent
from pedestrian import PedestrianAgent
from uuid import uuid4

class CreatorAgent(Agent):
    def _setup(self):
        from main import SERVER_NAME, routes
        self.drivers = []
        self.pedestrians = []
        for route in routes:
            if len(route) == 1:
                self.pedestrians.append(PedestrianAgent(address=route[0].lower(),
                                                        agentjid='pedestrian-%s@%s' % (str(uuid4())[:4], SERVER_NAME),
                                                        password='secret'))
            else:
                self.drivers.append(DriverAgent(routes=route,
                                                agentjid='driver-%s@%s' % (str(uuid4())[:4], SERVER_NAME),
                                                password='secret'))

        for driver in self.drivers:
            driver.start()

        for pedestrian in self.pedestrians:
            pedestrian.start()
