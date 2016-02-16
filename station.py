class Station(object):
    def __init__(self, station_id, name, connections):
        self.id = int(station_id)
        self.name = name
        self.connections = connections
        self.cats = []
        self.owners = []

    def __repr__(self):
        return self.name

    def add_init_cat(self, cat):
        if cat not in self.owners:
            self.cats.append(cat)
            return True
        else:
            return False

    def add_init_owner(self, owner):
        if owner not in self.cats:
            self.owners.append(owner)
            return True
        else:
            return False

    def add_cat(self, cat):
        self.cats.append(cat)

    def add_owner(self, owner):
        self.owners.append(owner)

    def remove_cat(self, cat):
        self.cats.remove(cat)

    def remove_owner(self, owner):
        self.owners.remove(owner)

    def owners_found_cats_in_station(self):
        cats_ids = [cat.id for cat in self.cats]
        owners_ids = [owner.id for owner in self.owners]
        return set(cats_ids).intersection(owners_ids)

    def close_station(self, stations):
        owners_found_cats = self.owners_found_cats_in_station()
        # remove/close station
        for station in stations:
            if self in station.connections:
                station.connections.remove(self)
        stations.remove(self)

        # Move cats out
        for cat in self.cats:
            if cat.id not in owners_found_cats:
                cat.move(stations)
            else:
                self.remove_cat(cat)

        # Move owners out
        for owner in self.owners:
            if owner.id not in owners_found_cats:
                owner.move(stations)
            else:
                self.remove_owner(owner)

        return stations
