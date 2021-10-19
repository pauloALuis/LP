"""
pc8.py
22/08/2021
"""

import datetime
import random
import csv
import xlsxwriter
import pickle

csv_file_name = "data.csv"
csv_file_name2 = "data2.csv"
csv_file_name3 = "data3.csv"

#8.a)
def gen_random_date_list(n: int = 10):
    """
    method that generates a list with random dates
    @param n : the length of the list
    @return a list with n random dates
    """
    l = []
    start_date = datetime.date(2010, 1, 1)
    end_date = datetime.date(2020, 1, 1)

    time_between_dates = end_date - start_date
    days_between_dates = time_between_dates.days
    for _ in range(n):
        random_number_of_days = random.randrange(days_between_dates)
        date = start_date + datetime.timedelta(days=random_number_of_days)
        l.append(str(date.day) + "/" + str(date.month) + "/" + str(date.year))
    return l


def gen_nested_lists(date_list: list = gen_random_date_list()):
    """
    create a list of list with a random date in the first index and a random number in the second index
    @param date_list : list of random dates
    @return a list of list with dates and numbers
    """
    l = []
    [l.append([date_list[i], random.randint(0, 100)]) for i in range(10)]
    return l


def gen_xlsx_file(l : list = gen_nested_lists()):
    """
    method that generates a xlsx file with dates and numbers
    @param l : list with the data to import to the xlsx file
    """
    workbook = xlsxwriter.Workbook('data1.xlsx')
    worksheet = workbook.add_worksheet()
    for i in range(0, len(l)):
        worksheet.write('A' + str(i), l[i][0])
        worksheet.write('B' + str(i), l[i][1])
    workbook.close()

def gen_csv_file(l : list = gen_nested_lists()):
    with open(csv_file_name, 'w') as f:
        write = csv.writer(f)
        for el in l:
            write.writerow(el)

#gen_csv_file()

def f1(file_name: str = csv_file_name):
    sum = 0
    with open(file_name) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            print(row)
            sum += int(row[1])
    return sum

print("soma = ", f1())

#8.b)
def f2(file_name: str = csv_file_name2):
    """
    method that saves 100 random numbvers in a csv file
    """
    l = []
    [l.append(random.uniform(0, 100)) for _ in range(100)]

    file = open(file_name, "w")
    writer = csv.writer(file)
    writer.writerow(l)

#f2()

#8.c)
def f3(file_name: str = csv_file_name3, l : list = [("string", 100), ("aa", 1), ("bb", 2), ("cc", 3)]):
    file = open(file_name, "w+")
    writer = csv.writer(file)

    for el in l:
        writer.writerow(el)
#f3()

#8.d)
def f4(file_name: str = csv_file_name3, pickle_name: str = "pickle-file4.pkl"):
    l = []
    counter = 0
    with open(file_name, 'r') as file:
        reader = csv.reader(file, delimiter = ',')
        for row in reader:
            l.append(row)
        file.close()

    file2 = open(pickle_name, "wb")
    pickle.dump(l, file2)
    file2.close()
f4()