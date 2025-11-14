# PolyEx15.py
from math import pi
class Circle:
    def __init__(self, r):  # Original Constructor
        self.ac = pi * r ** 2
        print("Area of Circle={}".format(round(self.ac, 2)))
class Square:
    def __init__(self, s):  # Oeverriden Constructor
        self.sa = s ** 2
        print("Area of Square={}".format(self.sa))
class Rect(Square,Circle):
    def __init__(self, L, B):  # Overridden Constructor
        self.ar = L * B
        print("Area of Rect={}".format(self.ar))
        print("--------------------------------")
        Circle.__init__(self,float(input("Enter Radius:")))
        super().__init__(float(input("Enter Side Value of Square:")))
        print("--------------------------------")


# Main Program
# accept Length and Breadth from Key Board
L = float(input("Enter Length:"))
B = float(input("Enter Breadth:"))
r = Rect(L, B)





