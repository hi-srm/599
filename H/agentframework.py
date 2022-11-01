"""
agent framework for model
"""
# import relevant package
import random

# create an agent class; each agent is characterised by a label i, an environment list, and an agents list
class Agent():
    
    def __init__(self, i, environment, agents):
        """
        This initialises agents

        Paramaters
        ----------
        self.i: each agent's identifier
        self.agents: agents list
        self.environment: environment list

        Variables
        __________
        self.store: initialised to 0
        self.x: random number between 0,99
        self.y: random number between 0,99

        Returns
        ------
        nothing as initialise just initialises
        """
        self.i = i
        self.agents = agents
        self.environment = environment
        self.store = 0
        self.x = random.randint(0,99)
        self.y = random.randint(0,99)

    def __str__(self):
        """
        This creates a string with the identifier, store and position [x,y] of agents
        """
        return "i= " + str(self.i) + ", store=" + str(self.store) + ", x=" \
            + str(self.x) \
            + ", y=" + str(self.y)
        
    def move(self):
        """
        Moving agents by generating a random number between 0 and 1
        If smaller than 0.5, x coordinate of agent is increased by 1%
        If larger than 0.5, x coordinate of agent is descreased by 1%
        (Half of the time the x coordinate is increased and half it is being decreased)
        Always change by 1% but it's 50/50 whether it is increasing or decreasing on each coordinate

        Variables
        self.x: x coordinate of agent
        self.y: y coordinate of agent

        """
        if random.random() < 0.5:
            self.x = (self.x + 1) % 100
        else:
            self.x = (self.x - 1) % 100

        if random.random() < 0.5:
            self.y = (self.y + 1) % 100
        else:
            self.y = (self.y - 1) % 100

    def eat(self): # making it eat what is left
        """
        If environment at the position the agent is in is larger than 10, the agent stores those 10 points from the environment and takes them away from the environment
        Otherwise, (so environment value at that position < 10) the agent only takes what is there and then the environment goes down to 0 (i.e. takes whatever is left)
        If each agent has eaten more than 100 from the environment, the environment takes those points back (so the agents can only store 100 points before returning them to the environment)
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
        """
        Calculates difference between the self and every other agent
        If that distance is smaller than or equal to the neighbourhood parameter:
            Each agent calculates the average stored value between itself and its neighbour
            That average becomes the agent's store value (ie if you're near other agents you have less environment to eat)
            And also the store of the neighbours' sets it to that average
            So for all agents within a neighbourhood, the store is redistributed so each agent has the average

        Parameters
        self: agent
        neighbourhood: integer
        """
        for i in range(len(self.agents)): # get length of agents list and loop through agents
            distance = self.distance_between(self.agents[i])# calculate distance between self and every other agent
            if distance <= neighbourhood:
                # add 2 stores together and calculate average
                average = (self.store + self.agents[i].store) /2
                self.store = average
                self.agents[i].store = average
                # print("sharing " + str(distance) + " " + str(average)) # to see what is being shared - this returns some sharing but also regularly returns 'sharing 0.0 10.0' why is that? - ok i realised it's because i didn't have enough agents!