import click

from utils import load_stations, set_init_positions, find_cat_owner_by_id


@click.command()
@click.argument('number', type=click.INT)
def cat_me(number):
    stations = load_stations()

    # set init positions
    cats, owners = set_init_positions(number, stations)
    number_cats_found = 0
    owners_moves = []

    # look for cats
    for i in range(100000):
        for obj_id in range(len(cats)):
            cat_found_in_station = False

            cat = find_cat_owner_by_id(cats, obj_id)
            owner = find_cat_owner_by_id(owners, obj_id)
            if not cat:
                continue

            current_owner_station = owner.move(stations)
            cat.move(stations)
            for pair in current_owner_station.owners_found_cats_in_station():
                cat_found_in_station = True
                number_cats_found = number_cats_found + 1
                print 'Owner {} found cat {} - {} is now closed.'.format(
                    pair, pair, current_owner_station)

            # close station
            if cat_found_in_station:
                owners_moves.append(owner.moves)
                stations = current_owner_station.close_station(stations)
                cats.remove(cat)
                owners.remove(owner)

    print 'Total number of cats: {}'.format(number)
    print 'Number of cats found: {}'.format(number_cats_found)
    print 'Average number of movements required to find a cat: {}'.format(
        float(sum(owners_moves))/max(len(owners_moves), 1))


if __name__ == '__main__':
    cat_me()
