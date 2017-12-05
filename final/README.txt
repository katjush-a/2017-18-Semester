Final project submission from Samuel (Alex) Jensen, 12/4/2017

To run, run 'python3 GameOfLife'
Generally a grid size of 30x20 to 60x40 is reccomended, grid sizes
above ~100x100 crashed TKinter on my machine but results may vary.

The Game of Life is a simluation of a grid of cells, which iterates
indefinitely, generating or deleting cells with each iteration. The
simulation has 4 rules:
	1. Any live cell with fewer than 2 live neighbors dies, as if 
	   by underpopulation
	2. Any live cell with 2 or 3 live neighbors lives on to next
	   generatoin
	3. Any live cell with more than 3 neighbors dies, as if by 
	   overpopulation
	4. Any dead cell with exactly 3 live neighbors becomes a live 
	   cell, as if by reproduction
	   
The program consists of 3 main files, Model.py, Controller.py, and
View.py. Model contains the algorithm and logic behind live and dead
cells, Controller contains the event loop and drawing the GUI, and 
View contains the GUI itself and respective methods.

User is first prompted to input a height and width of the grid, and
upon sumbission the window is closed and this data is immediately sent 
to the Model which returns 2, 2-Dimensional lists containing all 0's 
to the Controller. These lists are then used as parameters for drawing
the main window, which is a large grid, with size corresponding to the
inputted dimensions. This grid is a tkinter object which also contains
'pause', 'play', 'step', 'clear', and 'quit' buttons. The controller 
then enters into its main loop, which runs provided the 'quit' button 
is not activated. This loop contains another loop, which will only run
if the  simulation is not paused, which it is by default. Provided 
the 'play' button has been activated, meaning the simulation is not
paused, the 'step' method, which iterates the grid through to the next 
generation, will be executed every 0.4 seconds. While the simulation
is paused however, the GUI will await user input and the grid model
will be updated accordingly, which will in turn update the view via 
the controller.

modelTest.py contains the unit tests which were used to create Model.py.
GameOfLife.py does not depend on this file in any way and the program 
can be run without it.


Credit where credit is due:

Libraries Used:
	* TKinter

Resources Used:

The book "An Introduction to TKinter" (http://effbot.org/tkinterbook/)
and website https://www.tutorialspoint.com/python/python_gui_programming.htm
were both critical in my understanding of the TKinter syntax and how to
create my own event loop.

JetBrains PyCharm (https://www.jetbrains.com/pycharm/) gave me a lot of 
syntax and linting hints