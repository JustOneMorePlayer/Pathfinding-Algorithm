# Pathfinding-Algorithm
Implementation of the random generation of a maze and its solution using the A* algorithm

## Maze Generation

To create the maze I used the Willson's algorithm based on the [wikipedia page](https://en.wikipedia.org/wiki/Maze_generation_algorithm). Basically, we begin with a matrix with just walls and initiliaze the algorithm stablishing the top-left and bottom-right corners as path, these two correspond to the initial and goal position respectively. Then, until there are no cells left, we pick a random cell in the matrix and begin a random path until it hits a path cell. In this case the random path gets stablished as part of the path. To this random path a condition is imposed, it can not create loops. Or, in other words, the random pathn can not hit itself. Therefore, a backtracking algorithm is used to back up if it can not continue to move forward.


<p align="center">
  <img src="https://github.com/JustOneMorePlayer/Pathfinding-Algorithm/blob/main/READMEImages/line.gif">
</p>

 ## Pathfinding

For the pathfinding algorithm I implemented the A* algorithm where the following successor minimazes the function $f(x) = g(x) + h(x)$ where $g(x)$ is the minimal longitud from the cell $x$ to the starting cell and $f(x)$ is the euclidean distance between the cell $x$ and the goal cell.

To this function we can add a bias such that it prioritizes minimazing the actual longitud of the path from the starting cell to the cell $x$ or the distance between $x$ and the goal cell considering $f(x) = \alpha * g(x) + \beta * h(x)$. The gifs line0, ..., line9 show the trace of the algorithm for different values of $\alpha$ and $\beta$.

<p align="center">
  <img src="https://github.com/JustOneMorePlayer/Pathfinding-Algorithm/blob/main/READMEImages/line0.gif">
</p>
