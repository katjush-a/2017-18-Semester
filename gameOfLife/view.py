# View for Conway's Game of Life Final Project, Samuel Jensen, 11/20/2017

from tkinter import *
from model import *


# Create prompt window of type frame
class Prompt(Frame):
    # Define constructor with parameter self
    def __init__(self):
        # Call the Frame constructor as constructor for Prompt
        Frame.__init__(self)
        # Set title of object
        self.master.title("Initialize Grid")

        # Create header label and draw in grid row 0
        header = Label(text="Input Grid Dimensions")
        header.grid(row=0)

        # Create horizontal cells label and draw in grid row 1
        horizontal = Label(text="Horizontal Cells: ")
        horizontal.grid(row=1)

        # Create horizontal input textbox and draw in grid row 1, column 1
        self.hInput = Entry()
        self.hInput.grid(row=1, column=1)

        # Create vertical cells label and draw in grid row 2
        vertical = Label(text="Vertical Cells:")
        vertical.grid(row=2)

        # Create vertical input textbox and draw in grid row 2, column 1
        self.vInput = Entry()
        self.vInput.grid(row=2, column=1)

        # Create submit button with command .__submitCoords__ and draw in grid row 3
        submit = Button(text="Submit", command=self.__submitCoords__)
        submit.grid(row=3)

    # Define submitCoords method which opens new window with inputs given from textboxes
    def __submitCoords__(self):
        # Get data from hInput and vInput Entries
        horizontalCells = self.hInput.get()
        verticalCells = self.vInput.get()
        # Close Prompt instance
        self.master.destroy()

        # instantiate new window, gridDisplay with params of inputted dimensions
        gridDisplay = GridDisplay(horizontalCells, verticalCells)


class GridDisplay(Frame):
    def __init__(self, hCells, vCells):
        Frame.__init__(self)
        self.master.title("Conway's Game of Life")
