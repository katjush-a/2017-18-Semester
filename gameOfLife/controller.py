# Controller for Conway's Game of Life Final Project, Samuel Jensen, 11/20/2017

import view
import model
import tkinter

# Variable representing the state of the simulation, 0 - paused, 1 - running
simState = 0

# Function encapsulating the event loop
def simLoop():
    # Instantiate the Tk class as the main window
    root = tkinter.Tk()
    # Set window dimensions and position
    root.geometry("325x100+300+300")

    # Instantiate the Prompt window
    prompt = view.Prompt()
    # Start the Tk main loop
    root.mainloop()
    # Once data is submitted and window is closed, generate array from inputted data
    currentGen = model.Grid(prompt.verticalCells, prompt.horizontalCells)

    print(currentGen.list)

    grid = tkinter.Tk()
    gridDisplay = view.GridDisplay(prompt.horizontalCells, prompt.verticalCells, currentGen)

    grid.mainloop()

    print(currentGen.list)
