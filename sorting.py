import os
import csv

def read_data(file_name):
    """
    Reads csv file and returns numeric data.

    :param file_name: (str), name of CSV file
    :return: (dict), dictionary with numeric data, keys - csv column names, values - numbers in each column
    """
    slovnik = {}
    klice = []
    hodnoty = []
    cwd_path = os.getcwd()
    file_path = os.path.join(cwd_path+ "/lecture11/lecture_sorting/" + file_name)
    with open(file_path, mode="r") as csv_file:
        reader = csv.DictReader(csv_file)
        data = {}
        for row in reader:
            for header,value in row.items():
                if header not in data:
                    data[header] = [int(value)]
                else:
                    data[header].append(int(value))
    return data


def selection_sort(cisla,direction = 1 ):
    for x in range(len(cisla)):
        for k in range(x+1,len(cisla)):
            if direction ==1:
                if cisla[x] > cisla[k]:
                    cisla[x], cisla[k] = cisla[k], cisla[x]
            else:
                    if cisla[x] < cisla[k]:
                        cisla[x], cisla[k] = cisla[k], cisla[x]
    return cisla

def main():
    pass


if __name__ == '__main__':
    main()
