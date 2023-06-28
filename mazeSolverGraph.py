from randomMazeWilson import *
from randomMaze import *
import math
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import imageio
import os

rows = 15
columns = 30
bias = [0,1]
frames = [1]
maze = randomMazeWillson(rows, columns, frames)
goal  = [rows - 1, columns - 1]

plt.tick_params(axis = 'both', which = 'both',bottom = False, top = False, left = False, right = False, labelleft = False, labeltop = False)


c = mpl.colors.ListedColormap(['lightcyan', 'lightseagreen', 'paleturquoise', 'turquoise'])
n = mpl.colors.Normalize(vmin=0,vmax=3)

actualmaze = np.copy(maze)

initialPosition = [0,0]

print(maze)

print("dd")



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



#print(initialEntry.position)

def inTable(_position):
    for i in table:
        if(i.position == _position):
            return True
    return False

#if the element is in the open set it gets removed
#True if the element was on the list False otherwise
def removeOpenSet(_position):
    output = False
    index = 0
    for i in openSet:
        if(i == _position):
            openSet.pop(index)
            return True
    return False


def getEntry(_position):
    for i in table:
        if(i.position == _position):
            return i

def getPreviousPosition(_position):
    for i in table:
        if(i.position == _position):
            return i.previousPosition
def getf(_position):
    for i in table:
        if(i.position == _position):
            return i.f()

def updateTable(_newEntry):
    inTable = False#if the new entry is put in the table
    for i in table:
        if(i.position == _newEntry.position):
            print("\tCoincidence in table")
            print(f"\t new {_newEntry}")
            print(f"\t old {i}")
            if(i.g > _newEntry.g):
                i = _newEntry
                inTable = True
            else:
                inTable = False
            return inTable
    table.append(_newEntry)
    inTable = True
    return inTable

##CAMBIAR EL OPEN SET TAL QUE SUS ELEMENTOS
##SEAN SOLO PARES [X,Y] Y NO ESNTRIES

def updateOpenSet(_newPosition):
    index = 0
    removeOpenSet(_newPosition)
    for i in openSet:
        if(getf(i) >= getf(_newPosition)):
            openSet.insert(index,_newPosition)
            return
        index = index + 1
    openSet.append(_newPosition)

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

        
        #table.append(auxEntry)

        if(updateTable(auxEntry)):
            updateOpenSet(auxEntry.position)
        #i = 0
        #while(i < len(openSet) and openSet[i].f() <= auxEntry.f()):
        #    i = i + 1
        #    if(i == len(openSet) - 1):
        #        break
        #openSet.insert(i, auxEntry)

auxIndex = frames[0]
maxIndex = auxIndex
for j in range(10):
    initialEntry = entry(initialPosition, initialPosition, -1)
    openSet = [initialEntry.position]
    table = [initialEntry]
    
    if(frames[0] > maxIndex):
        maxIndex = frames[0]
    frames[0] = auxIndex
    bias[0] = bias[0] + 0.1
    bias[1] = bias[1] - 0.1
    auxMaze = np.copy(maze)

    index = 1
    while(openSet != []):


        actualEntry = getEntry(openSet[0])
        

        print(index)
        print(f"Current Entry {actualEntry}")

        
        openSet.pop(0)
            
        if(actualEntry.position == goal):
            break
        succ = successors(actualEntry.position, actualEntry.previousPosition)
        if(succ != []):
            mix(openSet, succ, actualEntry.position, actualEntry.g)

        print("Table")
        for i in table:
            print(i)

        print("Open set")
        for i in openSet:
            print(f"{i} {getf(i)}")

        actualmaze = np.copy(auxMaze)

        pos = actualEntry.position
        previousPos = getPreviousPosition(pos)
        actualmaze[pos[0], pos[1]] = 3

        while(previousPos != initialPosition):
            actualmaze[previousPos[0], previousPos[1]] = 3
            previousPos = getPreviousPosition(previousPos)
            
        actualmaze[previousPos[0], previousPos[1]] = 3



        fig, ax = plt.subplots()
        ax.matshow(actualmaze, cmap=c, norm = n)    
        #plt.show()

        plt.tick_params(axis = 'both', which = 'both',bottom = False, top = False, left = False, right = False, labelleft = False, labeltop = False)
        plt.savefig(f'frame {frames[0]}')
        plt.close()
        frames[0] = frames[0] + 1
        index = index + 1

        auxMaze[pos[0], pos[1]] = 2

        while(previousPos != initialPosition):
            auxMaze[previousPos[0], previousPos[1]] = 2
            previousPos = getPreviousPosition(previousPos)
            
        auxMaze[previousPos[0], previousPos[1]] = 2


    if(inTable(goal)):
        actualmaze = np.copy(auxMaze)
        actualmaze[goal[0], goal[1]] = 3
        previousPos = getPreviousPosition(goal)
        while(previousPos != initialPosition):
            actualmaze[previousPos[0], previousPos[1]] = 3
            previousPos = getPreviousPosition(previousPos)
        actualmaze[previousPos[0], previousPos[1]] = 3
    else:
        print("There's no solution")


    fig, ax = plt.subplots()
    #cmap=plt.cm.PuBu
    ax.matshow(actualmaze, cmap = c, norm  = n) 
    plt.tick_params(axis = 'both', which = 'both',bottom = False, top = False, left = False, right = False, labelleft = False, labeltop = False)   
    #plt.show()
    plt.savefig(f'frame {frames[0]}')
    plt.close()
    frames[0] = frames[0] + 1
    index = index + 1




    with imageio.get_writer(f'line{j}.gif', mode='i') as writer:
        for i in range(1, frames[0]):
            image = imageio.imread(f'frame {i}.png')
            writer.append_data(image)

    


for i in range(1, maxIndex):
        os.remove(f'frame {i}.png')

