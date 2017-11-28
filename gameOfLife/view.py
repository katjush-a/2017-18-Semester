from tkinter import *


class Prompt(Frame):
    def __init__(self):
        Frame.__init__(self)
        self.master.title("Initialize Grid")

        header = Label(text="Input Grid Dimensions")
        header.grid(row=0)

        # Horizontal cells label
        horizontal = Label(text="Horizontal Cells: ")
        horizontal.grid(row=1)

        # Horizontal cells textbox
        self.hInput = Entry()
        self.hInput.grid(row=1, column=1)

        # Vertical cells label
        vertical = Label(text="Vertical Cells:")
        vertical.grid(row=2)

        # Vertical cells textbox
        self.vInput = Entry()
        self.vInput.grid(row=2, column=1)

        submit = Button(text="Submit", command=self.__getCoords__)
        submit.grid(row=3)

    def __getCoords__(self):
        print(self.hInput)
        print(self.vInput)


def main():
    root = Tk()
    root.geometry("325x100+300+300")
    window = Prompt()
    root.mainloop()


if __name__ == '__main__':
    main()
