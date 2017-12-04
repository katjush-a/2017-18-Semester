# View for Conway's Game of Life Final Project, Samuel Jensen, 11/20/2017

from tkinter import *

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
        submit = Button(text="Submit", command=lambda: self.__submitCoords__())
        submit.grid(row=3)

    # Define submitCoords method which closes prompt and sets dimension data
    def __submitCoords__(self):
        # Get data from hInput and vInput Entries and convert to integers
        self.verticalCells = int(self.vInput.get())
        self.horizontalCells = int(self.hInput.get())
        # Close Prompt instance
        self.master.destroy()


# Create GridDisplay window of type Frame
class GridDisplay(Frame):
    # Define constructor with parameters for height and width of grid
    def __init__(self, height, width, currentGrid, nextGrid):
        # Call Frame constructor as constructor for GridDisplay
        Frame.__init__(self)
        # Set page title
        self.master.title("Conway's Game of Life")

        # Set height and width parameters to be accessible from any method of GridDisplay
        self.height = height
        self.width = width

        # Create 2D array of buttons with y and x variables for reference
        self.buttons = [[Button(width=2, command=lambda y=row, x=column: self.__toggle__(currentGrid, y, x))
                        for column in range(self.width)]
                        for row in range(self.height)]

        # Draw each index in said 2D array
        for row in range(self.height):
            for column in range(self.width):
                self.buttons[row][column].grid(row=row, column=column, sticky=NSEW)

        # Draw buttons for controls
        pauseButton = Button(text="Pause").grid(row=(height + 1), columnspan=width)
        playButton = Button(text="Play").grid(row=(height + 2), columnspan=width)
        stepButton = Button(text="Step", command=lambda: self.__step__(currentGrid, nextGrid)).grid(row=(height + 3), columnspan=width)

    def __update__(self, grid):
        # Iterate through each cell and update the color
        for row in range(self.height):
            for column in range(self.width):
                self.buttons[row][column].config(bg=colors[grid.__get__(row, column)])
                self.buttons[row][column].grid(row=row, column=column)

    # Define toggle class, given coordinate, changes data in Grid object and updates display
    def __toggle__(self, grid, y, x):
        # If list index is 0 change to 1 and vice versa
        if grid.__get__(y, x) == 0:
            grid.__set__(y, x, 1)
        elif grid.__get__(y, x) == 1:
            grid.__set__(y, x, 0)

        self.__update__(grid)

    def __step__(self, currentGrid, nextGrid):
        for row in range(self.height):
            for column in range(self.width):
                nextGrid.__set__(row, column, currentGrid.__nextGen__(row, column))

        for row in range(self.height):
            for column in range(self.width):
                currentGrid.__set__(row, column, nextGrid.__get__(row, column))

        self.__update__(currentGrid)
