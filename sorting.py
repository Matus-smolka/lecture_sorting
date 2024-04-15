import os
import csv

def read_data(file_name):
    """
    Reads csv file and returns numeric data.

    :param file_name: (str), name of CSV file
    :return: (dict), dictionary with numeric data, keys - csv column names, values - numbers in each column
    """
    cwd_path = os.getcwd()
    file_path = os.path.join(cwd_path, file_name)
    with open (file_path) as csv_file :
        csv_reader = csv.DictReader(csv_file)
        data = {}
        for row in csv_reader:
            for header,value in row.items():
                if header not  in data:
                    data[header] = [int(value)]
                else:
                    data[header].append(int(value))
            return data
def selection_sort(zoznam):
    for idx in range(0,len(zoznam)):
        min_index = idx
        for idy in range(idx,len(zoznam)):
            if zoznam[idy] < zoznam[idx] and zoznam[idy]<zoznam[min_index]:
                min_index=idy
            else:
                pass
        zoznam[idx], zoznam[min_index] = zoznam[min_index], zoznam[idx]
        print(zoznam)
    return zoznam
ciselka = [5,7,9,1,6,3,4,8]
print(selection_sort(ciselka))


#print(read_data("numbers.csv"))
def main():
    pass


if __name__ == '__main__':
    main()
