import csv
import os
import statistics

from data_types import Purchase


def main():
    print_header()
    file_name = get_data_file()

    print('File: {}'.format(file_name))

    data = load_file(file_name)
    query_data(data)


def print_header():
    print('---------------------------------------')
    print('    Real Estate data analysis App')
    print('---------------------------------------')
    print()


def get_data_file():
    base_folder = os.path.dirname(__file__)
    return os.path.join(base_folder, 'data', 'RealEstateTransactions.csv')


def load_file(file_name):
    with open(file_name, 'r', encoding='utf-8') as fin:

        reader = csv.DictReader(fin)
        purchases = []

        for row in reader:
            # print('Type: {} Row: {}'.format(type(row), row))
            # print('Beds #: {}'.format(row['Beds']))
            p = Purchase.create_from_dict(row)
            purchases.append(p)

        print(purchases[0].__dict__)

        # header = fin.readline().strip()
        # reader = csv.reader(fin, delimiter=',')
        # for row in reader:
        #    print('Row: {}'.format(row))

    return purchases


def query_data(data):

    data.sort(key=lambda p: p.Sale_price)

    # most expensive house
    high_purchase = data[-1]    # LAST item in the list
    print('The most expensive property price is ${} with {} beds and {} baths'.format(
        high_purchase.Sale_price, high_purchase.Beds, high_purchase.Bathrooms
    ))

    # Least expensive house
    low_purchase = data[0]     # FIRST item in the list
    print('The least expensive property price is ${} with {} beds and {} baths'.format(
        low_purchase.Sale_price, low_purchase.Beds, low_purchase.Bathrooms
    ))

    # Average house price
    # prices = []
    # for pur in data:
    #    prices.append(pur.Sale_price)

    prices = [
        p.Sale_price    # projection or items
        for p in data   # the set to process
    ]

    ave_price = 0
    # ave_price = statistics.mean(prices)
    print('The average price of homes is {:,}'.format(int(ave_price)))

    # Average house price of 2 bed houses
    # prices = []
    # for pur in data:
    #    if pur.Beds == 2:
    #        prices.append(pur.Sale_price)

    two_bed_homes = (   # generator expressions "()"
        p               # projection or items
        for p in data   # the set to process
        if announce(p, '2 bedrooms, found {}'.format(p.Beds)) and p.Beds == 2  # test / condition
    )

    homes = []
    for h in two_bed_homes:
        if len(homes) > 5:
            break
        homes.append(h)

    ave_price = 0
    # ave_price = statistics.mean(announce[p.Sale_price, 'price') for p in homes]) with declarative statement "[]"
    ave_price = statistics.mean(announce(p.Sale_price, 'price') for p in homes)   # with inline yield "()"
    ave_baths = statistics.mean((p.Bathrooms for p in homes))
    ave_squares = statistics.mean((p.Squares for p in homes))
    print('Two bedroom homes: average price {:,} baths {} squares {}'
          .format(int(ave_price), ave_baths, ave_squares))


def announce(item, msg):
    print('Pulling item {} for {}'.format(item, msg))
    return item


if __name__ == '__main__':
    main()

