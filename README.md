Mars Rover Kata
===============

Develop an api that moves rover around a grid

*********
Rules
*********

1. You are given initial starting point (0,0,N) of a rover.
2. 0,0 are X,Y coordinates on a grid of (10,10)
3. N is the direction it is facing (N, S, E ,W)
4. L and R allow rover to rotate left or right
5. M allows rover to move one point in the current direction.
6. Rover receives a char array of commands eg. (RMMLM) and returns the finishing point eg (2:1:N)
7. Rover wraps around if it reaches end of the grid.
8. Grid may have obstacles. If a given sequence of commands encounters an obstacle , the rover moves up to the last possible point 
and reports the obstacle eg: 0:2:2:N