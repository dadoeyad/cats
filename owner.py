import random


class Owner(object):
    def __init__(self, owner_id, init_station):
        self.id = owner_id
        self.current_station = init_station
        self.stations_visited = [init_station]
        self.moves = 0

    def __repr__(self):
        return 'owner: {id}, current_station: {current_station}'.format(
            id=self.id,
            current_station=self.current_station)

    def move(self, stations):
        self.moves = self.moves + 1

        if not self.can_move():
            return self.current_station

        # if visited all connections
        # get random
        next_station = None
        for station in self.current_station.connections:
            if station not in self.stations_visited:
                    next_station = station
                    break
        if not next_station:
            next_station = random.choice(self.current_station.connections)

        # can't move to a closed station
        if next_station not in stations:
            return self.current_station

        self.current_station.remove_owner(self)
        next_station.add_owner(self)
        self.current_station = next_station
        if next_station not in self.stations_visited:
            self.stations_visited.append(next_station)

        return next_station

    def can_move(self):
        return bool(self.current_station.connections)
