"""
E Practical: Agents 'Agentframework'
Author: Sophie Ray Morrison
"""
import random

class Agent():
    
    def __init__(self):
        """
        Initialises agent with x and y coordinates
        """
        self.x = random.randint(0,99)
        self.y = random.randint(0,99)
        
    def move(self):
        """
        Moves agents
        """
        if random.random() < 0.5:
            self.x = (self.x + 1) % 100
        else:
            self.x = (self.x - 1) % 100

        if random.random() < 0.5:
            self.y = (self.y + 1) % 100
        else:
            self.y = (self.y - 1) % 100