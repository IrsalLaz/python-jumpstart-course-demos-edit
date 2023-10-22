import csv
import os


def main():
    print("-------------------------")
    print("REAL ESTATE ANALYZER".center(25, " "))
    print("-------------------------")

    # get file path
    file_name = get_csv_location()
    get_csv_data(file_name)

    # get csv header
    # get most expensive house
    # get the least expensive house
    # get average house
    # get average house price of 2-bedroom house


def get_csv_location():
    base_folder = os.path.dirname(__file__)
    return os.path.join(base_folder, 'data',
                        'SacramentoRealEstateTransactions2008.csv')


def get_csv_data(file_name):
    try:
        with open(file_name, 'r') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            # get csv header
            csv_header = next(csv_reader)
            print(csv_header)
    except FileNotFoundError as err:
        print(err)


if __name__ == '__main__':
    main()
