''' Samuel Jensen, OOP Rectangle project, 11/1/2017
    Creates rectangle and returns attributes'''

class Rectangle:                                            # Create class 'Rectangle'
    def __init__(self, height=1, width=1):                  # Give it a constructor with params self, height, width, with default values of 1
        self.height = height                                # set height and width attributes to
        self.width = width                                  # their respoective params

    def area(self):                                         # Define method 'area' with param self
        return self.height * self.width                     # return the product of height and width attributes

    def perimeter(self):                                    # Define method 'perimeter' with param self
        return 2 * self.height + 2 * self.width             # return the perimeter based on height and width attributes

    def getStats(self):                                     # Define method 'getStats'
        return("Width:     {}\n"                            # Return the values of the previously defined attributes and methods
               "Height:    {}\n"                            # formatted into a string
               "Area:      {}\n"
               "Perimeter: {}\n".format(self.width, self.height, self.area(), self.perimeter()))


def main():
    print("Rectangle a:")
    a = Rectangle(5, 7)
    print("area:      {}".format(a.area()))
    print("perimeter: {}".format(a.perimeter()))

    print("")
    print("Rectangle b:")
    b = Rectangle()
    b.width = 10
    b.height = 20
    print(b.getStats())


if __name__ == "__main__":
    main()
