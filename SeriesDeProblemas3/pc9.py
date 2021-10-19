"""
pc9.py
23/08/2021
"""

import sqlite3
import csv

conn = sqlite3.connect('teste.db') #creates a db connection
c = conn.cursor() # creates a cursor to db

#9.a)
def create_table(name : str):
    """
    method that creates the table familia
    """
    #creates a table
    c.execute('''CREATE TABLE '''+ name + '''( 
        id INTEGER PRIMARY KEY,
        nome text,
        nome_familia text, 
        idade INTEGER
    )''')
    conn.commit()

#9.b)
def insert_data(file_name: str = "familia_db.csv"):
    """
    method that inserts data into a table from a csv file
    @param file_name : name of the csv file with the data
    """
    csv_file = open(file_name)
    rows = csv.reader(csv_file)
    l = []
    counter = 0
    for row in rows:
        if counter > 0:
            l.append([int(row[0]), row[1], row[2], int(row[3])])
        counter += 1

    c.executemany("insert into familia values (?, ?, ?, ?)", l)
    c.execute("select * from familia")
    print(c.fetchall())

def delete_data_of_table(table : str):
    """
    method that eles data from a table
    @param table: name of the table
    """
    c.execute("delete * from" + table + "")

def drop_table(table: str):
    """
    method that drop a table
    @param table : name of the table
    """
    c.execute("DROP TABLE " + table)


drop_table("familia")
create_table("familia")
insert_data()

#9.c)
def select_by_age(age : int = 19):
    """
    method that makes and prints the select did on db depending on the age
    @param age : the age to sleect 
    """
    print(c.execute("select * from familia where idade > "
         + str(age).c.fetchall()))

#select_by_age()

#9.d)
def select_by_age_family_name(age: int = 19, name: str = "marques"):
    """
    method that makes and prints the select did on db depending 
    on the age and the family name
    @param age : the age to seelct
    @param name : the family name to select
    """
    c.execute("select * from familia where idade > " + str(age) + 
            " and familia.nome_familia = \"" + name + "\"")
    print(c.fetchall())

select_by_age_family_name()

conn.commit() # aply/commit changes
conn.close() # close connection to db
