from logging import getLogger
import networkx as nx
from os import path
import matplotlib.pyplot as plt

log = getLogger(__file__)

CITIES_DIR = path.join(path.dirname(path.abspath(__file__)), 'cities')


class City(object):
    def __init__(self, city_name):
        self.gml = nx.read_gml(path=path.join(CITIES_DIR, city_name), label='id')

    def show(self):
        pos = nx.spring_layout(self.gml)
        nx.draw_networkx(self.gml, pos=pos)
        labels = nx.get_edge_attributes(self.gml, 'weight')
        nx.draw_networkx_edge_labels(self.gml, pos=pos, edge_labels=labels)
        nx.draw_networkx_edges(self.gml, pos, width=4, edge_color='g', arrows=False)
        plt.show()
