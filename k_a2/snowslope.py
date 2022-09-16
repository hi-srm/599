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
# csv_reader = csv.reader
# for line in csv_reader:
#     rowlist = []
#     for value in line:
#         rowlist.append((int(value))) # change value from string to int
#     print(rowlist)
# f.close()
### this returned an error: "invalid iteral for int() with base 10"




### define delimiters and replace them to fix the error
# f = open("snow.slope")
# csv_reader = csv.reader(f, delimiter=' ')
# for line in csv_reader:
#     rowlist = []
#     line = line.replace('\n', '')
#     for value in line:
#         print(value)
#         rowlist.append((int(value))) # change value from string to int
#     print(rowlist)
# f.close()
### this did not work


### make the file only read values and not spaces
# f = open("snow.slope")
# csv_reader = csv.reader(f, delimiter=' ')
# for line in csv_reader:
#     rowlist = []
#     for value in line:
#         if not value:
#             continue
#         rowlist.append((int(value))) # change value from string to int
# f.close()
### this worked!



### create the environment and add the rows to that
# f = open("snow.slope")
# csv_reader = csv.reader(f, delimiter=' ')
# environment = []
# for line in csv_reader:
#     rowlist = []
#     for value in line:
#         if not value:
#             continue
#         rowlist.append((int(value)))
#     environment.append(rowlist)
# f.close()
###


### create the environment and add the rows to that
f = open("snow.slope")
csv_reader = csv.reader(f, delimiter=' ')
environment = []
for line in csv_reader:
    rowlist = []
    for value in line:
        if not value: 
            continue
        rowlist.append((int(value)))
    environment.append(rowlist)
f.close()
###

num_heights = 300
heights = []

nrows = len(environment)

for i in range(1, nrows):
    rowpos = len(environment[i]) # gives us number of columns in the i'th row

print(rowpos)


# for i in environment:
#     row = 1
#     col = 2
#     heights.append([row][col])
#     print(heights)


# range(num_heights):
#     row = 
#     heights.append(environment[row][col])
#     print(heights)

# row = nrows-1 # test the very last row
# col = ncols-1 # test last col

# print(environment[row][col])

# height = environment[i][i]



# nrows = len(environment) # how many rows 
# print("nrows", nrows) 
# ncols = len(environment[0]) # set ncols to be number of columns in first row
# print("ncols", ncols)
# for i in range(1, nrows):
#     ncolsini = len(environment[i]) # gives us number of columns in the i'th row
#     if ncols != ncolsini:
#         print("error line", i, ", wrong number of columns, expecting", ncols, "received", ncolsini)
#         plot = False
        
        
# for row in range(nrows):
#     print(row[value])


    
    # for col in range(ncols):
    #     height = value[row][col]
#         value = environment[row][col]
#         # value2 = value * value #  shortening code
#         environment[row][col] = value       


# print(value[1][0])




# def distance_between(a, b):
#     """
    

#     Parameters
#     ----------
#     a : TYPE
#         DESCRIPTION.
#     b : TYPE
#         DESCRIPTION.

#     Returns
#     -------
#     TYPE
#         DESCRIPTION.

#     """
#     return (((a.x - b.x)**2) + ((a.y - b.y)**2))**0.5   

# heights = 300)
# gradients = []

# for i in range(heights):
#     gradient.append(str(i))

# for h in heights:
#     environment.append(rowlist + h)
   

# maxheight = 300
# heights = []

# ### define function

# def gradient(a, b):
#     '''
    

#     Parameters
#     ----------
#     a : TYPE
#         DESCRIPTION.
#     b : TYPE
#         DESCRIPTION.

#     Returns
#     -------
#     TYPE
#         DESCRIPTION.

#     '''
#     return (((a[0] - b[0])**2) + ((a[1] - b[1])**2))**0.5


# grad = gradient(a[0],a[b])




# ### plot it
# matplotlib.pyplot.imshow(environment)
# matplotlib.pyplot.show()










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

