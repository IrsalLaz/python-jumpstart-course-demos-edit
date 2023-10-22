import csv
import os


def main():
    print("-------------------------")
    print("REAL ESTATE ANALYZER".center(25, " "))
    print("-------------------------")

    # get file path
    file_name = get_csv_location()

    # get data from csv file and store it in a list of dictionary
    data = get_csv_data(file_name)

    # print data header

    # analyze data
    analyze_data(data)


def get_csv_location():
    base_folder = os.path.dirname(__file__)
    return os.path.join(base_folder, 'data',
                        'SacramentoRealEstateTransactions2008.csv')


def get_csv_data(file_name):
    # open the file in read mode
    try:
        with open(file_name, 'r') as csv_file:
            dict_reader = csv.DictReader(csv_file)
            list_of_dict = list(dict_reader)
            return list_of_dict

    except FileNotFoundError as err:
        return err


def analyze_data(house_list):
    # Print house_list column names
    header_string = ', '.join(house_list[0].keys())
    print("Headers: {}".format(header_string))

    # sort the list by price low to high
    house_list.sort(key=lambda house: int(house['price']))

    # get max and min price
    prices = []
    for h in house_list:
        prices.append(int(h['price']))

    most_expensive = house_list[-1]
    print("Most expensive house : {}-bed, {}-bath, house for ${:,} in {}".format(
        most_expensive['beds'],
        most_expensive['baths'],
        int(most_expensive['price']),
        most_expensive['city']))

    # get the least expensive house
    least_expensive = house_list[0]
    print("Least expensive house : {}-bed, {}-bath, house for ${:,} in {}".format(
        least_expensive['beds'],
        least_expensive['baths'],
        int(least_expensive['price']),
        least_expensive['city']))

    # get average price
    print("Average price : ${:,.0f}".format(sum(prices) / len(prices)))

    # get the average price of the house that has 2-beds
    two_bed_houses = []
    for h in house_list:
        if h['beds'] == '2':
            two_bed_houses.append(int(h['price']))

    average_price_two_bed = sum(two_bed_houses) / len(two_bed_houses)
    print("Average price of the house with 2-beds : ${:,}".format(int(average_price_two_bed)))


if __name__ == '__main__':
    main()
