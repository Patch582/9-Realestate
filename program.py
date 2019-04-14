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


def load_file(file_name):
    return []


def get_data_file():
    base_folder = os.path.dirname(__file__)
    return os.path.join(base_folder, 'data', 'RealEstateTransactions.csv')


def query_data(data):
    pass


if __name__ == '__main__':
    main()
