from logging import getLogger
import networkx as nx
from route import Point, PointStatus
from os import path
import matplotlib.pyplot as plt
import sys

log = getLogger(__file__)

CITIES_DIR = path.join(path.dirname(path.abspath(__file__)), 'cities')

class City:
    def __init__(self, city_name):
        self.gml = nx.read_gml(path=path.join(CITIES_DIR, city_name), label='id')
        self.floyd_warshall = nx.floyd_warshall(self.gml)

    def get_distance(self, a, b):
        if isinstance(a, Point):
            a = a.name
        if isinstance(b, Point):
            b = b.name
        return self.floyd_warshall[a][b]

    def get_routes_distance(self, routes):
        distance = 0
        from itertools import izip, islice
        for current_item, next_item in izip(routes, islice(routes, 1, None)):
            distance += self.get_distance(current_item, next_item)

        distance += self.get_distance(routes[-1], routes[-2])
        return distance

    def get_optimal_route_to_point(self, routes, point, after_stock=False):
        if after_stock:
            stock_index = routes.index(filter(lambda point: point.status == PointStatus.PICK, routes)[0])
            before_stock = routes[:stock_index]
            routes = routes[stock_index:]

        possible_routes = []
        for i in [x + 1 for x in range(len(routes))]:
            route = routes[:]
            route.insert(i, point)
            possible_routes.append(route)

        optimal = sys.maxint
        optimal_plan = None
        for plan in possible_routes:
            dist = self.get_routes_distance(plan)
            if self.get_routes_distance(plan) < optimal:
                optimal = dist
                optimal_plan = plan

        if after_stock:
            optimal_plan_plan = before_stock + optimal_plan
            optimal = self.get_routes_distance(optimal_plan_plan)
            return optimal, optimal_plan

        return optimal, optimal_plan


    def show(self):
        pos = nx.spring_layout(self.gml)
        nx.draw_networkx(self.gml, pos=pos)
        labels = nx.get_edge_attributes(self.gml, 'weight')
        nx.draw_networkx_edge_labels(self.gml, pos=pos, edge_labels=labels)
        nx.draw_networkx_edges(self.gml, pos, width=4, edge_color='g', arrows=False)
        plt.show()