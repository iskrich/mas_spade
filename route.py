# -*- coding: utf-8 -*-

from enum import Enum

class PointStatus(Enum):
    DROP = 'drop'
    PICK = 'pick'
    ON_ROAD = 'on road'


class Point:
    def __init__(self, name, status):
        self.name = name
        self.status = status

    def __str__(self):
        return '%s(%s)' % (self.name, self.status)

class Route:
    def __init__(self, points):
        self.points = points

    def add_point(self, point):
        # перестроить маршрут с новой точкой
        # оптимальный - перебор во все промежутки пихаешь склад
        # AFBC f - skald, DE: AFDEBCA, AFBDCEA, AFEDBC - перебрать все варианты маршрутов

        # По ближайшим соседям: куда вставляем склад сначала
        # Смотреть какая точка ближайшая, следующая основная или доставки. в противном случае разносим в конце
        pass

    def remove_point(self, point_name):
        pass

    def change_status(self, point_name, status):
        pass