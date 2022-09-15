# -*- coding: utf-8 -*-
"""
Created on Tue Sep 13 15:52:32 2022

@author: gysmo
"""

import matplotlib.pyplot


# # import csv
# # with open('in.txt', newline='') as f:
# #     reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)
# #     for row in reader:
# #         for value in row:

            

# # import csv
# # with open('in.txt', newline='') as f:
# #     reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)
# #     rowlist = []
# #     environment = []
# #     for row in reader:
# #         for value in row:
# #             rowlist.append(value)
# #             environment.append(rowlist)


# import csv


# with open('in.txt', newline='') as f:
    
    
# f = open("in.txt")
# reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)
# rowlist = []
# environment = []
# for value in f:
#     rowlist.append(f)
#     for row in reader:
#         for value in row:
#             environment.append(rowlist)
    


    # reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)

    # rowlist.append(f)
    # environment = []
    # for value in f:
    #     print(value)
    # for row in reader:
    #     for value in row:
    #         environment.append(rowlist)

# # rowlist = []
# # rowlist.append(value)
# # environment = []
# # environment.append(rowlist)
            



import csv

f = open("bfi.txt")
csv_reader = csv.reader(f)
environment = []
for line in csv_reader:
    rowlist = []
    for value in line:
        # print (type(value)) - to test type that the value is, as it wasn't plotting
        rowlist.append((int(value))) # change value from string to int
    # print(rowlist)
    environment.append(rowlist)
f.close()
print(environment)




plot = True
# testing all the rows having the same number of columns (is it rectangular)
nrows = len(environment) # how many rows 
print("nrows", nrows) 
ncols = len(environment[0]) # set ncols to be number of columns in first row
print("ncols", ncols)
for i in range(1, nrows):
    ncolsini = len(environment[i]) # gives us number of columns in the i'th row
    if ncols != ncolsini:
        print("error line", i, ", wrong number of columns, expecting", ncols, "received", ncolsini)
        plot = False
        
        
# if plot: 
#     matplotlib.pyplot.imshow(environment)
#     matplotlib.pyplot.show()
    

# change values
for row in range(nrows):
    for col in range(ncols):
        value = environment[row][col]
        # value2 = value * value #  shortening code
        environment[row][col] = value * value
    
# to test the value at a given row and column
row = nrows-1 # test the very last row
col = ncols-1 # test last col

print(environment[row][col]) # i checked in the file


# with open('in.txt', newline='') as f:
    
    
    # value = f.read().replace('\n', '')
    # rowlist = []
    # environment = []
    # for row in f:
    #     rowlist.append([])
    #     environment.append(rowlist)
    #     print(value[4])
        
  
    # # f = csv.reader(f, delimiter=' ', quotechar='|')      
        
        
# environment.append(rowlist)
# print(environment)

# import csv
# with open('in.txt', newline='') as f:
    
    
# f = open("in.txt")
# for line in f:
#     print(line)
#     rowlist = []
#     rowlist.append()
#     environment = []
#     for row in reader:
#         for value in row:
#             environment.append(rowlist)







# with open('in.txt') as csv_file:
#     csv_reader = csv.reader(csv_file, delimiter=',')
#     line_count = 0
#     for row in csv_reader:
#         if line_count == 0:
#             print(f'Column names are {", ".join(row)}')
#             line_count += 1
#         else:
#             print(f'\t{row[0]}{row[1]}{row[2]}.')
#             line_count += 1
#     print(f'Processed {line_count} lines.')]