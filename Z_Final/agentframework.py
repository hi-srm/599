"""
Final project

Agent Framework for Model
Author: Sophie Ray Morrison
Version: Final
"""
# Import relevant package
import random

# Create an agent class; each agent is characterised by a label i, an environment list, and an agents list
class Agent():
    
    def __init__(self, i, environment, agents):
        """
        This initialises agents

        Paramaters
        ----------
        self.i: Number
            Each agent's identifier
        self.agents: List
            Agents list
        self.environment: List
            Environment list

        Variables
        __________
        self.store: Number
            Initialised to 0
        self.x: Number
            Random number between 0,99
        self.y: Number
            Random number between 0,99
        """
        self.i = i
        self.agents = agents
        self.environment = environment
        self.store = 0
        self.x = random.randint(0,99)
        self.y = random.randint(0,99)

    def __str__(self):
        """
        Generates a string with details of agents
        This can be used to make the output of results more readable by adding text descriptions
        
        Variables
        ------
        self.i: Number
            Agent's identifier
        self.store: Number
            Agent's store
        self.x: Number
            Agent's position on x axis
        self.y: Number
            Agent's position on y axis

        Returns
        ------
        A string with the identifier, store and position [x,y] of agents
        """
        return "i= " + str(self.i) + ", store=" + str(self.store) + ", x=" \
            + str(self.x) \
            + ", y=" + str(self.y)
        
    def move(self):
        """
        Moves agents by generating a random number between 0.0 and 0.9
        If smaller than 0.5, x coordinate of agent is increased by 1
        If larger than 0.5, x coordinate of agent is descreased by 1
        The same applies to the y coordinate

        Paramaters
        ------
        self.x: Number
            X coordinate of agent
        self.y: Number   
            Y coordinate of agent

        Returns
        ------
        Modifies x and y variables of the agent
        """
        if random.random() < 0.5:
            self.x = (self.x + 1) % 100
        else:
            self.x = (self.x - 1) % 100

        if random.random() < 0.5:
            self.y = (self.y + 1) % 100
        else:
            self.y = (self.y - 1) % 100

    def eat(self):
        """
        Makes agents store resources from the environment
        
        If the environment at the position the agent is in is larger than 10, the agent stores those 10 points, taking them from the environment
        Otherwise, (so environment value at that position < 10) the agent only takes what is there and then the environment goes down to 0 (i.e. takes whatever is left). This is to avoid having negative values for the environment.
        If an agent has eaten more than 100 from the environment, the environment takes those points back (so the agents can only store 100 points before returning them to the environment)
        
        Paramaters
        ------
        self.i: Number
            Agent's identifier
        self.store: Number
            Agent's store
        self.environment: List
            y and x coordinates

        Returns
        -----
        Changes the values of environment and store variables
        """
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
        Calculates the distance between self and b (another agent)
    
        Paramaters
        ----------
        b: Object 
            Agent that contains identifier, store, environment, x coordinate, y coordinate, agent list
    
        Returns
        ------
        distance_between: Number
            Distance between self and b
        """
        return (((self.x - b.x)**2) + 
        ((self.y - b.y)**2))**0.5

    def share_with_neighbours(self, neighbourhood):
        """
        Calculates difference between the self and every other agent
        If that distance is smaller than or equal to the neighbourhood parameter:
        - Each agent calculates the average stored value between itself and its neighbour
        - That average becomes the agent's store value (ie if you're near other agents you have less environment to eat)
        - And also the store of the neighbours' sets it to that average

        Parameters
        ------
        neighbourhood: Number
            Paramater set in model that determines the neighbourhood radius

        Returns
        ------
        Modifies agents' store     
        """
        for i in range(len(self.agents)): # get length of agents list and loop through agents
            distance = self.distance_between(self.agents[i])# calculate distance between self and every other agent
            if distance <= neighbourhood:
                # add 2 stores together and calculate average
                average = (self.store + self.agents[i].store) /2
                self.store = average
                self.agents[i].store = average
