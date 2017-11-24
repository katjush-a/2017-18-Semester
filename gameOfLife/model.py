class Grid:
    def __init__(self, height, width):
        self.list = [[0 for i in range(height)] for j in range(width)]

    def __get__(self, yPos, xPos):
        if yPos >= 0:
            if xPos >= 0:
                return self.list[yPos][xPos]
            else:
                raise ValueError
        else:
            raise ValueError

    def __set__(self, yPos, xPos, value):
        self.list[yPos][xPos] = value

    def __scan__(self, yPos, xPos):
        alive = 0

        try:
            if self.__get__(yPos, (xPos + 1)) == 1:
                alive += 1
            else:
                alive += 0
        except IndexError:
            pass

        try:
            if self.__get__(yPos, (xPos - 1)) == 1:
                alive += 1
            else:
                alive += 0
        except IndexError:
            pass

        return alive


currentGen = Grid(1, 4)
currentGen.__set__(0, 2, 1)
currentGen.__set__(0, 3, 1)

'''
def scan(array, y, x):
    alive = 0

    try:
        if array[(x + 1)] == 1:
            alive += 1
        else:
            alive += 0
    except IndexError:
        pass

    try:
        if array[(x - 1)] == 1:
            alive += 1
        else:
            alive += 0
    except IndexError:
        pass

    return alive


print(currentGen[-1])
'''
