import csv
import os


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
        for row in reader:
            print('Type: {} Row: {}'.format(type(row), row))
            print('Beds #: {}'.format(row['Beds']))

        # header = fin.readline().strip()
        # reader = csv.reader(fin, delimiter=',')
        # for row in reader:
        #    print('Row: {}'.format(row))


    return []


def query_data(data):

    # TODO: most expensive house
    # TODO: Least expensive house
    # TODO: Average house price
    # TODO: Average house price of 2 bed houses
    pass


if __name__ == '__main__':
    main()
