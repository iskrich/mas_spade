from agents import CreatorAgent
from city import City, CITIES_DIR
import os

SERVER_NAME = '127.0.0.1'
city = City('small_city.gml')

with open(os.path.join(CITIES_DIR, 'small_city_routes.txt')) as file:
    routes = []
    for line in file:
        routes.append(line.split())
    stock = routes[0][0]
    routes = routes[1:]

if __name__ == '__main__':
    a = CreatorAgent("%s@%s" % ('agent', SERVER_NAME), "secret")
    a.start()

