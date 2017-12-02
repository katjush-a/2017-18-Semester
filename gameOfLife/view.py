# View for Conway's Game of Life Final Project, Samuel Jensen, 11/20/2017

from tkinter import *
from model import *

colors = ['white', 'grey']

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

    # Define submitCoords method which closes prompt and sets dimension data
    def __submitCoords__(self):
        # Get data from hInput and vInput Entries and convert to integers
        self.horizontalCells = int(self.hInput.get())
        self.verticalCells = int(self.vInput.get())
        # Close Prompt instance
        self.master.destroy()


# Create GridDisplay window of type Frame
class GridDisplay(Frame):
    # Define constructor with parameters for height and width of grid
    def __init__(self, hCells, vCells, grid):
        # Call Frame constructor as constructor for GridDisplay
        Frame.__init__(self)
        # Set page title
        self.master.title("Conway's Game of Life")

        self.gridDisplay = [[Button(command=self.__toggle__(grid, row, column))
                             for row in range(hCells)] for column in range(vCells)]

        for row in range(len(self.gridDisplay)):
            for column in range(len(self.gridDisplay[row])):
                self.gridDisplay[row][column].configure(bg=colors[grid.__get__(row, column)])
                self.gridDisplay[row][column].grid(row=row, column=column)


    # Given a grid and position, toggles value of grid at that position
    def __toggle__(self, grid, yPos, xPos):
        # if value of grid.list at (yPos, xPos) is 1 change it to 0
        if grid.__get__(yPos, xPos) == 1:
            grid.__set__(yPos, xPos, 0)
        # if value of grid.list at (yPos, xPos) is 0 change it to 1
        elif grid.__get__(yPos, xPos) == 0:
            grid.__set__(yPos, xPos, 1)
