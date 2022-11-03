# GEOG5995M: Assessment 1

Contains workthroughs of the practical exercises, as well as a final agent-based model, including agent framework.

## Dependencies

[Matplotlib](https://matplotlib.org)

## Contents
- A: Agent based modelling
- B: Code shrinking I
- C: Code shrinking II
- D: Building tools
- E: Agents
- F: I/O
- G: Communicating
- H: Animation/behaviour
- Z_Final: Final model

## Final model

The most up-to-date work for assessment can be found in the 'Z' folder. This is based on the latest H animation practical, but contains the correct documentation etc and removes a lot of the 'workings-out'. 

I ran into a lot of trouble using Tkinter and, though, I could get the GUI working at times, it was very buggy. I therefore did not implement a GUI and chose instead to focus on ensuring high quality code.

The final model I have made:
- Reads in data from a text file and plots this to an environment
- Creates agents that move around and eat the environment
- Lets agents know about each other
- Creates neighbourhoods that affect how agents interact with each other
- Generates an animated visualisation that shows the iterations of this process, as well as a .txt file that outputs the final eaten environment after the iterations have completed
