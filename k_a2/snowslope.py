# -*- coding: utf-8 -*-
"""
assignment 2 project:
to the max!(...imum gradient...)
GEOG5995M, september 2022
sophie ray morrison

instructions: Imagine you are an extreme sports holiday company. You've been given raster data of the heights for a hilly area, and you want to find the most extreme gradients on which to set up snowboard runs. The raster data will be text numbers of metres above sea level.
"""

### imports the necessary modules
import matplotlib.pyplot
import csv

### test: to check the file can be read
# f = open("snow.slope")
# print(f.read())
### result: yes!

### test: the file type 
# f = open("snow.slope")
# csv_reader = csv.reader(f) # pass file through csv reader
# for value in f: # selects values in the file
#     print (type(value)) # prints value type
### result: value is string, so needs to be changed to integer     

### create empty rows and add the values in the snow.slope file to those rows
# f = open("snow.slope")
# csv_reader = csv.reader(f)
# for line in csv_reader:
#     rowlist = []
#     for value in line:
#         rowlist.append((int(value))) # change value from string to int
#     print(rowlist)
# f.close()
### this returned an error: "invalid iteral for int() with base 10" - i think this is because there are empty cells within the slope file

### do the same as above, but change values to floats and then integers so it can read them maybe?
# f = open("snow.slope")
# csv_reader = csv.reader(f)
# for line in csv_reader:
#     rowlist = []
#     for value in line:
#         rowlist.append((int(float(value)))) # change to float and then to integer
#     print(rowlist)
# f.close()
### this didn't work, it said 'could not convert string to float'

### this means the data needs cleaning, for this i will use some other tools, imported below
import pandas as pd
import numpy as np

### to read the csv and find missing values
data = pd.read_csv('snow.slope')
# print(data)


df = pd.read_csv('snow.slope')
new_df = df.dropna()

print(new_df.to_string())



# df = pd.read_csv('snow.slope')
# df.head()


























# do the same as above but change values to floats and then integers so it can read them
# f = open("snow.slope")
# csv_reader = csv.reader(f)
# for line in csv_reader:
#     rowlist = []
#     for value in line:
#         rowlist.append((int(float(value)))) # change to float and then to integer
#     print(rowlist)
# f.close()
# this didn't work, it said 'could not convert string to float'

### trying something else!
# f = open("snow.slope")
# csv_reader = csv.reader(f)
# for line in csv_reader:
#     rowlist = []
#     value = f.read().replace('\n', '')
#     for value in line:
#         rowlist.append((int(value))) # change to float and then to integer
#         print(rowlist)
        
# f.close()
### 


### trying something else 2
# f = open("snow.slope")
# value = f.readlines()
# csv_reader = csv.reader(f)
# environment = []
# for line in csv_reader:
#     rowlist = []
#     for value in line:
#         rowlist.append((int(value))) # change to float and then to integer
#     environment.append(rowlist) 
# f.close()
# print(environment)
# ### 

####trying 3
# f = open("snow.slope")
# csv_reader = csv.reader(f, delimiter=',')
# environment = []
# for line in csv_reader:
#     rowlist = []
#     for value in line:
#         # print (type(value)) - to test type that the value is, as it wasn't plotting
#         rowlist.append((int(value))) # change value from string to int
#     # print(rowlist)
#     environment.append(rowlist)
# f.close()
# print(environment)



# f = open('snow.slope','r').read().splitlines()
# csv_reader = csv.reader(f)
# for line in csv_reader:
#     rowlist = []
#     value = f.read().replace('\n', '')
#     for value in line:
#         rowlist.append((int(value))) # change to float and then to integer
#         print(rowlist)

# f.close()

# f = open('snow.slope','r').read().splitlines()
# csv_reader = csv.reader(f)
# for line in csv_reader:
#     if line.isdigit():
#         rowlist = []
#         value = f.read().replace('\n', '')
#         for value in line:
#             rowlist.append((int(value))) # change to float and then to integer
#             print(rowlist)
# f.close()



# f = open("snow.slope")
# csv_reader = csv.reader(f)
# value = f.read().replace('\n', '')
# for line in csv_reader:
#     rowlist = []
#     for value in line:
#         rowlist.append((int(value)))
#     print(rowlist)
# f.close()


# ## do the same as above but use csv reader to fix
# with open('snow.slope', newline='') as f:
#     csv_reader = csv.reader(f)
#     value = f.read().replace('\n', '')
#     for line in csv_reader:
#         rowlist = []
#         for value in line:
#             rowlist.append((int(value)))
#     print(rowlist)
# f.close()
## result: 



# create an environment to put the rows in
# f = open("snow.slope")
# csv_reader = csv.reader(f)
# environment = []
# for line in csv_reader:
#     rowlist = []
#     for value in line:
#         rowlist.append((int(float(value))))
#     environment.append(rowlist)
# f.close()
# print(environment)


# plot = True
# # testing all the rows having the same number of columns (is it rectangular?)
# nrows = len(environment) # how many rows 
# print("nrows", nrows) 
# ncols = len(environment[0]) # set ncols to be number of columns in first row
# print("ncols", ncols)
# for i in range(1, nrows):
#     ncolsini = len(environment[i]) # gives us number of columns in the i'th row
#     if ncols != ncolsini:
#         print("error line", i, ", wrong number of columns, expecting", ncols, "received", ncolsini)
#     plot = False
        
        
# if plot: 
#     matplotlib.pyplot.imshow(environment)
#     matplotlib.pyplot.show()
    

# # change values
# for row in range(nrows):
#     for col in range(ncols):
#         value = environment[row][col]
#         # value2 = value * value #  shortening code
#         environment[row][col] = value * value
    
# # to test the value at a given row and column
# row = nrows-1 # test the very last row
# col = ncols-1 # test last col

# print(environment[row][col]) # i checked in the file



# -------
