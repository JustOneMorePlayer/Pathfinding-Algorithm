from randomMazeWilson import *
from randomMaze import *
import math
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import imageio
import os

rows = 15
columns = 30
bias = [0.7,0.3]
maze = createRandomMaze(rows, columns)

plt.tick_params(axis = 'both', which = 'both',bottom = 'false', top = 'false', left = 'false', right = 'false')

actualmaze = np.copy(maze)

initialPosition = [0,0]

print(maze)

print("dd")

def getGoal(maze, rows, columns):
    i = 0
    while(maze[rows - 1, columns - 1 - i] != 0):
        i = i + 1
    return [rows - 1, columns - 1 - i]

goal  = getGoal(maze, rows, columns)
class entry:
    def __init__(self, _position, _previousPosition, _previousg):
        self.position = _position
        self.g = _previousg + 1
        self.h = math.sqrt((_position[0] - goal[0])**2 + (_position[1] - goal[1])**2)
        self.previousPosition = _previousPosition
    def __str__(self):
        return f"{self.position} {self.g} {self.h} {self.f()} {self.previousPosition}"
    def f(self):
        return bias[0]*self.g + bias[1]*self.h

initialEntry = entry(initialPosition, initialPosition, -1)
openSet = [initialEntry]
table = [initialEntry]

#print(initialEntry.position)

def getPreviousPosition(_position):
    for i in table:
        if(i.position == _position):
            return i.previousPosition
   


def successors(position, _previousPosition):
    output = []
    i = position[0]
    j = position[1]
    if(i > 0):
        if(maze[i - 1, j] == 0 and [i - 1, j] != _previousPosition):
            output.append([i - 1, j])
    if(i < rows - 1):
        if(maze[i + 1, j] == 0 and [i + 1, j] != _previousPosition):
            output.append([i + 1,j])
    if(j > 0):
        if(maze[i, j - 1] == 0 and [i, j - 1] != _previousPosition):
            output.append([i,j - 1])
    if(j < columns - 1):
        if(maze[i, j + 1] == 0 and [i, j + 1] != _previousPosition):
            output.append([i, j + 1])
    return output;
    

def mix(_open, _successors, _actualPosition, _actualg):
    while(_successors != []):
        position = _successors[0]
        _successors.pop(0)

        auxEntry = entry(position, _actualPosition, _actualg)

        table.append(auxEntry)

        i = 0
        while(i < len(openSet) and openSet[i].f() < auxEntry.f()):
            i = i + 1
            if(i == len(openSet) - 1):
                break
        openSet.insert(i, auxEntry)


        
 
    
index = 1
while(openSet != []):
    print(index)
    print("Table")
    for i in table:
        print(i)

    print("Open set")
    for i in openSet:
        print(i)

    actualEntry = openSet[0]
    openSet.pop(0)
    if(actualEntry.position == goal):
        break
    mix(openSet, successors(actualEntry.position, actualEntry.previousPosition), actualEntry.position, actualEntry.g)
 
    actualmaze = np.copy(maze)

    pos = actualEntry.position
    previousPos = getPreviousPosition(pos)
    actualmaze[pos[0], pos[1]] = 2
    actualmaze[pos[0], pos[1]] = 2

    while(previousPos != initialPosition):
        actualmaze[previousPos[0], previousPos[1]] = 2
        previousPos = getPreviousPosition(previousPos)
        
    actualmaze[previousPos[0], previousPos[1]] = 2


    fig, ax = plt.subplots()
    ax.matshow(actualmaze, cmap=plt.cm.PuBu)    
    #plt.show()


    plt.savefig(f'frame {index}')
    plt.close()
    index = index + 1

    


actualmaze = np.copy(maze)
actualmaze[goal[0], goal[1]] = 2
previousPos = getPreviousPosition(goal)
while(previousPos != initialPosition):
    actualmaze[previousPos[0], previousPos[1]] = 2
    previousPos = getPreviousPosition(previousPos)
actualmaze[previousPos[0], previousPos[1]] = 2

fig, ax = plt.subplots()
ax.matshow(actualmaze, cmap=plt.cm.PuBu)    
#plt.show()
plt.savefig(f'frame {index}')
plt.close()
index = index + 1




with imageio.get_writer('line.gif', mode='i') as writer:
    for i in range(1, index):
        image = imageio.imread(f'frame {i}.png')
        writer.append_data(image)

for i in range(1, index):
    os.remove(f'frame {i}.png')




