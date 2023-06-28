import random
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

plt.tick_params(axis = 'both', which = 'both',bottom = False, top = False, left = False, right = False, labelleft = False, labeltop = False)


test = np.matrix([[1,1],[2,1],[2,1]])
c = mpl.colors.ListedColormap(['lightcyan', 'lightseagreen', 'paleturquoise', 'turquoise'])
n = mpl.colors.Normalize(vmin=0,vmax=3)

def isValid(_maze, _pos, _rows, _columns):#al elegir una casilla inicial esta no puede generar un cuadrado en el laberinto
    i = _pos[0]
    j = _pos[1]

    if(i > 0):
        if(j > 0 and ((_maze[i, j - 1] == 0 or _maze[i, j - 1] == 2) and (_maze[i - 1, j - 1] == 0 or _maze[i - 1, j - 1] == 2 ) and (_maze[i - 1, j] == 0 or _maze[i - 1, j] == 2))):
            return False
        if(j < _columns - 1 and ((_maze[i, j + 1] == 0 or _maze[i, j + 1] == 2) and (_maze[i - 1, j] == 0 or _maze[i - 1, j] == 2) and (_maze[i - 1, j + 1] == 0 or _maze[i - 1, j + 1] == 2))):
            return False
    if(i < _rows - 1):
        if(j > 0 and ((_maze[i, j - 1] == 0 or _maze[i, j - 1] == 2) and (_maze[i + 1, j - 1] == 0 or _maze[i + 1, j - 1] == 2) and (_maze[i + 1, j] == 0 or _maze[i + 1, j] == 2))):#esquina abajo izq
            return False
        if(j < _columns - 1 and ((_maze[i, j + 1] == 0 or _maze[i, j + 1] == 2) and (_maze[i + 1, j] == 0 or _maze[i + 1, j] == 2) and (_maze[i + 1, j + 1] == 0 or _maze[i + 1, j + 1] == 2))):
            return False
    return True


def successors(_maze, _pos, _rows, _columns):
    output = []
    i = _pos[0]
    j = _pos[1]
    if(i > 0 and isValid(_maze, [i - 1, j], _rows, _columns) and _maze[i - 1, j] != 2):
        output.append([i - 1, j])
    if(i < _rows - 1 and isValid(_maze, [i + 1, j], _rows, _columns) and _maze[i + 1, j] != 2):
        output.append([i + 1, j])
    if(j > 0 and isValid(_maze, [i, j - 1], _rows, _columns) and _maze[i, j - 1] != 2):
        output.append([i, j - 1])
    if(j < _columns - 1 and isValid(_maze, [i, j + 1], _rows, _columns) and _maze[i, j + 1] != 2):
        output.append([i, j + 1])
    return output

#print(successors(test, [1,0], 3, 2))
def randomPath(_maze, _position, inde, rows, columns):
    
    succ = successors(_maze, _position, rows, columns)
    if(succ == []):
        return [_position]
    
    randomInt = random.randint(0, len(succ) - 1)
    position = succ[randomInt]
    _maze[position[0], position[1]] = 2
    succ.pop(randomInt)
    stack = [[_position, succ]]
    
    #while(_maze[_position[0], _position[1]] != 0):
    while(True):


        if((stack[0])[0] == position):
            succ = (stack[0])[1]
            stack.pop(0)
        else:
            succ = successors(_maze, position, rows, columns)

        if(succ == []):
            
            #remainingCells.pop(randomInt)
            _maze[position[0], position[1]] = 1
            position = (stack[0])[0]
            
            fig, ax = plt.subplots()
            ax.matshow(_maze,  cmap = c, norm  = n)    
            #plt.show()

            plt.tick_params(axis = 'both', which = 'both',bottom = False, top = False, left = False, right = False, labelleft = False, labeltop = False)
            plt.savefig(f'frame {inde[0]}')
            plt.close()
            inde[0] = inde[0] + 1
            continue
        randomInt = random.randint(0, len(succ) - 1)
        aux = position
        position = succ[randomInt]

        if(_maze[position[0], position[1]] == 0):
            stack.insert(0, [aux, []])
            stack.insert(0, [position, []])
            break;

        _maze[position[0], position[1]] = 2
        succ.pop(randomInt)
        stack.insert(0,[aux, succ] )
        
        fig, ax = plt.subplots()
        ax.matshow(_maze,  cmap = c, norm  = n)    
        #plt.show()

        plt.tick_params(axis = 'both', which = 'both',bottom = False, top = False, left = False, right = False, labelleft = False, labeltop = False)
        plt.savefig(f'frame {inde[0]}')
        plt.close()
        inde[0] = inde[0] + 1

    output = []
    for i in stack:
        output.append(i[0])

    return output



        
    

def randomMazeWillson(rows, columns, frames):

    print(rows)
    print(columns)

    maze = np.matrix([[1 for i in range(columns)] for j in range(rows)])
    selectedCell = np.matrix([[False for i in range(columns)] for j in range(rows)])
    remainingCells = [[i,j] for i in range(rows) for j in range(columns)]
    maze[0,0] = 0
    maze[rows - 1, columns - 1] = 0

    randomInt = random.randint(0, len(remainingCells) - 1)
    initialPos = remainingCells[randomInt]
    remainingCells.pop(randomInt)
    maze[initialPos[0], initialPos[1]] = 0
    selectedCell[initialPos[0], initialPos[1]] = True

    index = 1

    fig, ax = plt.subplots()
    ax.matshow(maze,  cmap = c, norm  = n)    
    #plt.show()

    plt.tick_params(axis = 'both', which = 'both',bottom = False, top = False, left = False, right = False, labelleft = False, labeltop = False)
    plt.savefig(f'frame {frames[0]}')
    plt.close()
    frames[0] = frames[0] + 1

    while(remainingCells != []):
        randomInt = random.randint(0, len(remainingCells) - 1)
        position = remainingCells[randomInt]
        remainingCells.pop(randomInt)
        if(maze[position[0], position[1]] == 0):
            continue;
        if(not isValid(maze, position, rows, columns)):
            print(f"{position} Not valid")
            continue
        maze[position[0], position[1]] = 2
        
        if(selectedCell[position[0],position[1]]):
            print(f"{position} Already selected")
            continue

        path = randomPath(maze, position, frames, rows, columns)
        print(path)
        for i in path:
            maze[i[0], i[1]] = 0

        fig, ax = plt.subplots()
        ax.matshow(maze,  cmap = c, norm  = n)    
        #plt.show()

        plt.tick_params(axis = 'both', which = 'both',bottom = False, top = False, left = False, right = False, labelleft = False, labeltop = False)
        plt.savefig(f'frame {frames[0]}')
        plt.close()
        frames[0] = frames[0] + 1


        index = index + 1

    return maze
