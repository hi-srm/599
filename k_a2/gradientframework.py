# -*- coding: utf-8 -*-
"""
Created on Fri Sep 16 14:38:28 2022

@author: gysmo
"""

import random

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

class Gradient():
    
    def __init__(self, name):
        self.name = "height " + name
        self.x = random.randint(0,99)
        self.y = random.randint(0,99)
        
    def __str__(self):
        return self.name + ", " + str(self.x) + ", " + str(self.y)
        
        
        
    def move(self):
        if random.random() < 0.5:
            self.x = (self.x + 1) % 100
        else:
            self.x = (self.x - 1) % 100

        if random.random() < 0.5:
            self.y = (self.y + 1) % 100
        else:
            self.y = (self.y - 1) % 100
