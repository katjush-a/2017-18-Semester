def scan(array, x, y):
    alive = 0

    for i in range(-1, 1):
        for j in range(-1, 1):
            try:
                if array[x+i][y+j] == 1:
                    alive += 1
                else:
                    alive += 0
            except IndexError:
                alive += 0

    return alive
