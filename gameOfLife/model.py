# Model for Conway's Game of Life Final Project, Samuel Jensen, 11/20/2017


# Grid class acts as specialized list, only allowing positive indexes
class Grid:
    # Initializing Grid creates a 2D list of height 'height' and width 'width'
    def __init__(self, height, width):
        self.list = [[0 for i in range(width)] for j in range(height)]

    # Get method affirms that indexes are positive and returns value at given x and y positions
    def __get__(self, yPos, xPos):
        if yPos >= 0:
            if xPos >= 0:
                return self.list[yPos][xPos]
            else:
                raise ValueError
        else:
            raise ValueError

    # Set method redefines value at point yPos and xPos
    def __set__(self, yPos, xPos, value):
        self.list[yPos][xPos] = value

    # Scan method checks all 8 surrounding cells, returning the sum of the alive cells
    def __scan__(self, yPos, xPos):
        alive = 0

        # List 'y' represents relative y values of 3 cells above, 2 adjacent cells, and 3 cells below given coordinate
        y = [1, 1, 1, 0, 0, -1, -1, -1]
        # List 'x' represents relative x values of 3 cells above, 2 adjacent cells, and 3 cells below given coordinate
        x = [-1, 0, 1, -1, 1, -1, 0, 1]

        # Loop through each of the 8 adjacent cells around given coordinate
        for i in range(0, 8):
            try:
                # Each value in x and y when put together represent a point adjacent to yPos and xPos
                if self.__get__((yPos + y[i]), (xPos + x[i])) == 1:
                    alive += 1
                else:
                    alive += 0
            # Do nothing if coordinate is on the edge, and therefore adjacent cell is out of range
            except IndexError:
                pass
            # Do nothing if coordinate is on the edge, and therefore adjacent cell is negative
            except ValueError:
                pass

        return alive
    # nextGen method returns whether a cell, given its adjacent cells should be dead or alive in the next generation
    def __nextGen__(self, y, x):
        # Returns 1 (alive) if alive cells is between 2-3
        if 2 <= self.__scan__(y, x) <= 3:
            return 1
        # Otherwise return 0 (dead)
        else:
            return 0
