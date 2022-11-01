# -*- coding: utf-8 -*-
"""
Created on Tue Sep 13 14:29:17 2022

@author: gysmo
"""
import random

class Agent():
    
    def __init__(self, i, environment, agents):
        self.i = i
        self.agents = agents
        self.environment = environment
        self.store = 0
        self.x = random.randint(0,99)
        self.y = random.randint(0,99)

    def __str__(self):
        return "i= " + str(self.i) + ", store=" + str(self.store) + ", x=" \
            + str(self.x) \
            + ", y=" + str(self.y)
        
    def move(self):
        if random.random() < 0.5:
            self.x = (self.x + 1) % 100
        else:
            self.x = (self.x - 1) % 100

        if random.random() < 0.5:
            self.y = (self.y + 1) % 100
        else:
            self.y = (self.y - 1) % 100

    def eat(self): # making it eat what is left
        if self.environment[self.y][self.x] > 10:
            self.environment[self.y][self.x] -= 10
            self.store += 10
        else:
            self.store += self.environment[self.y][self.x]
            self.environment[self.y][self.x] = 0
        if self.store >= 100:
            self.environment[self.y][self.x] += self.store
            self.store=0

    def distance_between(self, b):
        """
        This calculates the distance between self and b

        Paramaters
        ----------
        self:   agent
        b   :   

        Returns
        ------
            distance : Number
            distance between self and b
        """
        return (((self.x - b.x)**2) + 
        ((self.y - b.y)**2))**0.5

    def share_with_neighbours(self, neighbourhood):
        for i in range(len(self.agents)): # get length of agents list and loop through agents
            distance = self.distance_between(self.agents[i])# calculate distance between self and agent
            if distance <= neighbourhood:
                # add 2 stores together and caluclate average
                average = (self.store + self.agents[i].store) /2
                self.store = average
                self.agents[i].store = average
                # print("sharing " + str(distance) + " " + str(average)) # to see what is being shared - this returns some sharing but also regularly returns 'sharing 0.0 10.0' why is that? - ok i realised it's because i didn't have enough agents!