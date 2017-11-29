# Controller for Conway's Game of Life Final Project, Samuel Jensen, 11/20/2017

import view
import model
import tkinter


def simLoop():
    root = tkinter.Tk()
    root.geometry("325x100+300+300")

    prompt = view.Prompt()
    root.mainloop()

    currentGen = model.Grid(prompt.verticalCells, prompt.horizontalCells)

    print(currentGen.list)
