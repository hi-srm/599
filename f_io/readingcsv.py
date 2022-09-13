# -*- coding: utf-8 -*-
"""
Created on Tue Sep 13 15:52:32 2022

@author: gysmo
"""

import matplotlib.pyplot


# import csv
# with open('in.txt', newline='') as f:
#     reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)
#     for row in reader:
#         for value in row:

            

# import csv
# with open('in.txt', newline='') as f:
#     reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)
#     rowlist = []
#     environment = []
#     for row in reader:
#         for value in row:
#             rowlist.append(value)
#             environment.append(rowlist)


import csv
with open('in.txt', newline='') as f:
    reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)
    rowlist = []
    environment = []
    for row in reader:
        for value in row:
            rowlist.append(value)
environment.append(rowlist)

rowlist = []
rowlist.append(value)
environment = []
environment.append(rowlist)
            
matplotlib.pyplot.imshow(environment)
matplotlib.pyplot.show()