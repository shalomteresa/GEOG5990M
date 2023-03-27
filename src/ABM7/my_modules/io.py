# -*- coding: utf-8 -*-
"""
Created on Wed Mar  8 09:44:24 2023

@author: gy22stp
"""

import csv

# Read input data
def read_data():
    f = open('../../data/input/in.txt', newline='')
    data = []
    for line in csv.reader(f, quoting=csv.QUOTE_NONNUMERIC):
        row = []
        for value in line:
            row.append(value)
            #print(value)
        data.append(row)
    f.close()
    # Check there are the same number of columns in each row of data
    n_rows = len(data)
    print("n_rows", n_rows)
    n_cols0 = len(data[0])
    print("n_cols", n_cols0)
    for row in range(1, n_rows):
        n_cols = len(data[row])
        if n_cols != n_cols0:
            print("Warning")
    #print(data)
    return data, n_rows, n_cols
    f.close()
    print(data)
    

def write_Data(filename, environment):
    f = open('../../data/output/out7.txt', 'w', newline='')
    writer = csv.writer(f,delimiter=',',quoting=csv.QUOTE_NONNUMERIC)
    for row in environment:
        writer.writerow(row)
        