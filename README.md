# Pathfinding-Algorithm
Implementation of the random generation of a maze and its solution using the A* algorithm

## Maze Generation

To create the maze I used the Willson's algorithm based on the [wikipedia page](https://en.wikipedia.org/wiki/Maze_generation_algorithm). Basically, we begin with a matrix with just walls and initiliaze the algorithm stablishing the top-left and bottom-right corners as path, these two correspond to the initial and goal position respectively. Then, until there are no cells left, we pick a random cell in the matrix and begin a random path until it hits a path cell. In this case the random path gets stablished as part of the path. To this random path a condition is imposed, it can not create loops. Or, in other words, the random pathn can not hit itself. Therefore, a backtracking algorithm is used to back up if it can not continue to move forward.


<p align="center">
  <img src="https://github.com/JustOneMorePlayer/Pathfinding-Algorithm/blob/main/READMEImages/line.gif">
</p>




<p align="center">
  <img src="[https://github.com/JustOneMorePlayer/Pathfinding-Algorithm/blob/main/READMEImages/line0.gif">
</p>
