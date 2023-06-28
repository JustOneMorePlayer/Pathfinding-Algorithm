import numpy as np
import random
import matplotlib.pyplot as plt




def createRandomMaze(rows, columns):
    maze = np.matrix([[1 for i in range(columns)] for j in range(rows)])
    stack = [[0,0]]
    maze[0,0] = 0

    while(stack != []):
        #print(stack)
        succ = successors(stack[0], maze, rows, columns)
        if(succ == []):
            stack.pop(0)
            continue
        nextPos = succ[random.randint(0, len(succ) - 1)]
        maze[nextPos[0], nextPos[1]] = 0
        stack.insert(0, nextPos)

    return maze


def successors(_position, maze,rows, columns):
    i = _position[0]
    j = _position[1]
    output = []

    if(i > 0 and maze[i - 1, j] == 1):#casilla arriba
        add = True
        if(j - 1 >= 0 and maze[i - 1, j - 1] != 1):
            add = False
        elif(j + 1 < columns and maze[i - 1, j + 1] != 1):
            add = False
        elif(i - 2 >= 0 and maze[i - 2, j] != 1):
            add = False
        if(add):
            output.append([i - 1, j])
    if(i < rows - 1 and maze[i + 1, j] == 1):#casilla abajo
        add = True
        if(j - 1 >= 0 and maze[i + 1, j - 1] != 1):
            add = False
        elif(j + 1 < columns and maze[i + 1, j + 1] != 1):
            add = False
        elif(i + 2 <= rows - 1 and maze[i + 2, j] != 1):
            add = False
        if(add):
            output.append([i + 1, j])
    if(j > 0 and maze[i, j - 1] == 1):#casilla izquierda
        add = True
        if(j - 2 >= 0 and maze[i, j - 2] != 1):
            add = False
        elif(i - 1 >= 0 and maze[i - 1, j - 1] != 1):
            add = False
        elif(i + 1 < rows and maze[i + 1, j - 1] != 1):
            add = False
        if(add):
            output.append([i, j - 1])
    if(j < columns - 1 and maze[i, j + 1] == 1):#casilla derecha
        add = True
        if(j + 2 < columns and maze[i, j + 2] != 1):
            add = False
        elif(i - 1 >= 0 and maze[i - 1, j + 1] != 1):
            add = False
        elif(i + 1 < rows and maze[i + 1, j + 1] != 1):
            add = False
        if(add):
            output.append([i, j + 1])
    return output




