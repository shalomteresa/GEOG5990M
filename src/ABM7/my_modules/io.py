# -*- coding: utf-8 -*-
"""
Created on Wed Mar  8 09:44:24 2023

@author: gy22stp
"""
# Modules imported
import csv

# Read input data
def read_data():
    """
    The function to read the input data
    -------
    This function reads the input data from a CSV file and returns a list of rows,
    the number of rows,and the number of columns in each row.
    
    Returns
    -------
    data : a list of rows, where each row is a list of floating-point values.
    n_rows : an integer representing the number of rows in the data.
    n_cols : an integer representing the number of columns in each row of data.

    """
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
    
    
# Write the output into files
def write_Data(filename, environment):
    """
    The function to write data into a file
    ---------
    write environment array to a txt file 
    

    Parameters
    ----------
    filename :str
        Name of the output file.
    environment : list of list
        A 2D list of values representing the environment.

    Returns
    -------
    None.

    """
    f = open('../../data/output/out7.txt', 'w', newline='')
    writer = csv.writer(f,delimiter=',',quoting=csv.QUOTE_NONNUMERIC)
    for row in environment:
        writer.writerow(row)
        