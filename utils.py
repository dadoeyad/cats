import json
import random

from station import Station
from cat import Cat
from owner import Owner


def set_init_positions(number, stations):
    cats = []
    owners = []

    for i in range(number):
        cat_added = False
        owner_added = False

        # if not added, add it to another station
        while not cat_added:
            cat_station = random.choice(stations)
            cat = Cat(i, cat_station)
            cat_added = cat_station.add_init_cat(cat)

        cats.append(cat)

        while not owner_added:
            owner_station = random.choice(stations)
            owner = Owner(i, owner_station)
            owner_added = owner_station.add_init_owner(owner)

        owners.append(owner)

    return cats, owners


def _find_station_by_id(station_id, stations):
    for station in stations:
        if station.id == station_id:
            return station


def find_cat_owner_by_id(objects, id):
    for obj in objects:
        if obj.id == id:
            return obj


def load_stations():
    stations_dict = _load_stations_file()
    connections_dict = _load_connections_file()
    stations = []

    for station_id, station_name in stations_dict.items():
        connections = connections_dict.get(station_id, [])
        connections = [int(connection) for connection in connections]
        station_obj = Station(station_id, station_name, connections)
        stations.append(station_obj)
    # convert connections to station objects
    for station in stations:
        station.connections = [_find_station_by_id(connection, stations) for connection in station.connections]
    return sorted(stations, key=lambda station: station.id)


def _load_json_file(file_name):
    file = open(file_name).read()
    return json.loads(file)


def _load_stations_file():
    stations_list = _load_json_file('tfl_stations.json')
    return {station[0]: station[1] for station in stations_list}


def _load_connections_file():
    connections_list = _load_json_file('tfl_connections.json')
    connections_dict = {}
    for connection in connections_list:
        if connection[0] not in connections_dict:
            connections_dict[connection[0]] = [connection[1]]
        else:
            connections_dict[connection[0]].append(connection[1])

        # Connections go both ways
        if connection[1] not in connections_dict:
            connections_dict[connection[1]] = [connection[0]]
        else:
            connections_dict[connection[1]].append(connection[0])
    return connections_dict
