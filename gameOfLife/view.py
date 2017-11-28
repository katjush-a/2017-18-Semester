from tkinter import *


class Prompt(Frame):
    def __init__(self):
        super().__init__()
        self.master.title("Initialize Grid")


def main():
    root = Tk()
    root.geometry("300x250+300+300")
    window = Prompt()
    root.mainloop()


if __name__ == '__main__':
    main()
