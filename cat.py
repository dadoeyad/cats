import random


class Cat(object):
    def __init__(self, cat_id, init_station):
        self.id = cat_id
        self.current_station = init_station

    def __repr__(self):
        return 'cat: {id}, current_station: {current_station}'.format(
            id=self.id,
            current_station=self.current_station)

    def move(self, stations):
        if not self.can_move():
            return self.current_station

        next_station = random.choice(self.current_station.connections)

        # can't move to a closed station
        if next_station not in stations:
            return self.current_station

        self.current_station.remove_cat(self)
        next_station.add_cat(self)
        self.current_station = next_station

        return next_station

    def can_move(self):
        return bool(self.current_station.connections)
