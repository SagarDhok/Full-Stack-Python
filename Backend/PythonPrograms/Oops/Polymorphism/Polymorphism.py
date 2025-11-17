
# ^---------------------------------------------------------------------------------------
#! Without Polymorphism
# class Circle:
#      def draw(self):
#           print("Draw a circle")

# class Rect:
#      def draw(self):
#           print("Draw a Rectangle")

# co = Circle()
# ro = Rect()
# co.draw()
# ro.draw()
# ^---------------------------------------------------------------------------------------
#! Polymorphism Ex-1

# class Circle:
#      def draw(self):      #* Original Method
#           print("Draw A Circle")
     
# class Rect(Circle):
#      def draw(self):     #* Overridden Method
#           print("Draw A Rectangle")
          
#           super().draw()           #* Calls Immediate Base Class

# ro = Rect()
# ro.draw()
# ^---------------------------------------------------------------------------------------
#! Polymorphism Ex-2
# class Circle:
#      def draw(self):       #* Originlal Method
#           print("Draw A Circle ")
#           # super().draw()   AttributeError: 'super' object has no attribute 'draw'
# class Rect(Circle):
#      def draw(self):   #* Overriden Method
#           print("Draw A Rectangle")
#           super().draw()                  #* Calls Immediate Base Class
# class Square(Rect):
#      def draw(self):   #* Overridden Method
#           print("Draw A Square")
#           super().draw()                  #* Calls Immediate Base Class

# so = Square()
# so.draw()
# ^---------------------------------------------------------------------------------------
#! Polymorphism Ex-3
# class Circle:
#      def draw(self):         #* Original Method
#           print("Draw A Circle")

# class Rect(Circle):
#      def draw(self):        #* Overridden Method
#           print("Draw A Rectangel")

# class Square(Rect):
#      def draw(self):       #* Overridden Method
#           print("Draw A Square")
#           Rect.draw(self)         #*class name syntax can call from anywhere
#           Circle.draw(self)



# so= Square()
# so.draw()

# ^---------------------------------------------------------------------------------------
#! Polymorphism Ex-4
# class Circle:
#      def draw(self):         #* Original Method
#           print("Draw A Circle")

# class Rect(Circle):
#      def draw(self):        #* Overridden Method
#           print("Draw A Rectangle")

# class Square(Rect):
#      def draw(self):       #* Overridden Method
#           print("Draw A Square")
#           super().draw()           #*class name syntax can call from anywhere
#           Circle.draw(self)        #* Calls Immediate Base Class
 
# so= Square()
# so.draw()

# ^---------------------------------------------------------------------------------------
#! Polymorphism Ex-5

# class Circle:
#      def draw(self):         #* Original Method
#           print("Draw A Circle")

# class Rect:
#      def draw(self):        #* Overridden Method
#           print("Draw A Rectangle")

# class Square(Rect,Circle):
#      def draw(self):       #* Overridden Method
#           print("Draw A Square")
#           super().draw()           #*class name syntax can call from anywhere
#           super().draw()           #*class name syntax can call from anywhere
#           # Circle.draw(self)        #* Calls Immediate Base Class
 
# so= Square()
# so.draw()

# ^---------------------------------------------------------------------------------------
#! Finding the area of diffrent figures uisng polymorphism
#* Multilevel Inheritance
# from math import pi
# class Circle:
#      def area(self):
#           self.r = float(input("Enter Radius of Circle : "))
#           self.ac = pi*self.r**2
#           print(f"Area of Circle : {round(self.ac,2)}")
# class Square(Circle):
#      def area(self):
#           self.s = float(input("Enter Side of Square : "))
#           self.asq = self.s*self.s
#           print(f"Area of Square : {self.asq}") 
#           super().area()  
# class Rect(Square):
#      def area(self):
#           self.l = float(input("Enter Lenght of Rectangle : "))
#           self.w = float(input("Enter Width of Rectangle : "))
#           self.ar = self.l*self.w
#           print(f"Area of Rectangle : {self.ar}")
           
#           super().area()
  

# ro =Rect()
# ro.area()

# ^---------------------------------------------------------------------------------------
#! Finding the area of diffrent figures uisng polymorphism
#* Multilevel Inheritance
# from math import pi
# class Circle:
#      def area(self):
#           self.r = float(input("Enter Radius of Circle : "))
#           self.ac = pi*self.r**2
#           print(f"Area of Circle : {round(self.ac,2)}")
#           print("-"*20)
# class Square(Circle):
#      def area(self):
#           self.s = float(input("Enter Side of Square : "))
#           self.asq = self.s*self.s
#           print(f"Area of Square : {self.asq}") 
# class Rect(Square):
#      def area(self):
#           self.l = float(input("Enter Lenght of Rectangle : "))
#           self.w = float(input("Enter Width of Rectangle : "))
#           self.ar = self.l*self.w
#           print(f"Area of Rectangle : {self.ar}")
           
#           print("-"*20)
#           super().area()
#           Circle.area(self)
  

# ro =Rect()
# ro.area()

# # ^---------------------------------------------------------------------------------------
# #! Finding the area of diffrent figures uisng polymorphism
# #* Multiple Inheritance
# from math import pi
# class Circle:
#      def area(self):
#           self.r = float(input("Enter Radius of Circle : "))
#           self.ac = pi*self.r**2
#           print(f"Area of Circle : {round(self.ac,2)}")
#           print("-"*20)
# class Square():
#      def area(self):
#           self.s = float(input("Enter Side of Square : "))
#           self.asq = self.s*self.s
#           print(f"Area of Square : {self.asq}")
#           print("-"*20) 
# class Rect(Square,Circle):
#      def area(self):
#           self.l = float(input("Enter Lenght of Rectangle : "))
#           self.w = float(input("Enter Width of Rectangle : "))
#           self.ar = self.l*self.w
#           print(f"Area of Rectangle : {self.ar}")
           
#           print("-"*20)
#           super().area()       #! only super calls accordinf to  priority like in this square is priority
#           # Circle.area(self)      #* Instance method ahe pan polymorphism madhi self n call kl ki infinite call karte
  

# ro =Rect()
# ro.area()

# ^---------------------------------------------------------------------------------------
#! Finding the area of diffrent figures uisng polymorphism
#* Multilevel Inheritance - with parameters - with super()
# from math import pi
# class Circle:
#      def area(self,r):
#           self.ac = pi*r**2
#           print("------------------------------------------")
#           print(f"Area of Circle : {round(self.ac,2)}")
# class Square(Circle):
#      def area(self,s):
#           self.asq = s*s
#           print(f"Area of Square : {self.asq}") 
#           print("------------------------------------------")
#           super().area(float(input("Enter Radius of Circle : ")))  
# class Rect(Square):
#      def area(self,l,w):                                                                 # noqa: E741
#           self.ar = l*w
#           print(f"Area of Rectangle : {self.ar}")
#           print("------------------------------------------")
#           super().area(float(input("Enter Side Of Square ---: ")))

# l = float(input("Enter Length of Rectangle : "))                                              # noqa: E741
# w = float(input("Enter Width of Rectangle : "))
# ro =Rect()
# ro.area(l,w)
# # ^---------------------------------------------------------------------------------------
# #! Finding the area of diffrent figures uisng polymorphism
# #* Multilevel Inheritance - with parameters - with clasname()
# from math import pi
# class Circle:
#      def area(self,r):
#           self.ac = pi*r**2
#           print(f"Area of Circle : {round(self.ac,2)}")
#           print("-------------- ----------------------------")
# class Square(Circle):
#      def area(self,s):
#           self.asq = s*s
#           print(f"Area of Square : {self.asq}") 
#           print("------------------------------------------")
# class Rect(Square):
#      def area(self,l,w):                                                                 # noqa: E741
#           self.ar = l*w
#           print(f"Area of Rectangle : {self.ar}")
#           print("------------------------------------------")
#           Circle.area(self,float(input("Enter Radius of Circle : : ")))
#           Square.area(self,float(input("Enter Side Of Square : :  ")))

# l = float(input("Enter Length of Rectangle : "))                                              # noqa: E741
# w = float(input("Enter Width of Rectangle : "))
# ro =Rect()
# ro.area(l,w)
# # ^---------------------------------------------------------------------------------------
# #! Finding the area of diffrent figures uisng polymorphism
#* Multiple Inheritance - with parameters - with clasname()
# from math import pi
# class Circle:
#      def area(self,r):
#           self.ac = pi*r**2
#           print(f"Area of Circle : {round(self.ac,2)}")
#           print("-------------- ----------------------------")
# class Square:
#      def area(self,s):
#           self.asq = s*s
#           print(f"Area of Square : {self.asq}") 
#           print("------------------------------------------")
# class Rect(Circle,Square):
#      def area(self,l,w):                                                                 # noqa: E741
#           self.ar = l*w
#           print(f"Area of Rectangle : {self.ar}")
#           print("------------------------------------------")
#           Square.area(self,float(input("Enter Side Of Square : :  ")))
#           Circle.area(self,float(input("Enter Radius of Circle : : ")))

# l = float(input("Enter Length of Rectangle : "))                                              # noqa: E741
# w = float(input("Enter Width of Rectangle : "))
# ro =Rect()
# ro.area(l,w)
# # ^---------------------------------------------------------------------------------------
#! Polymorphism with constructor 
#* Multilevel inheritance
# class C1 :
#      def __init__(self):
#           print("C1 - Default Constructor")
# class C2 (C1):
#      def __init__(self):
#           print("C2 - Default Constructor")
#           super().__init__()
# class C3(C2):
#      def __init__(self):
#           print("C3 - Default Constructor")
#           super().__init__()

# co = C3()
# # ^---------------------------------------------------------------------------------------
#! Polymorphism with constructor 
#* Multiple inheritance
# class C1 :
#      def __init__(self):
#           print("C1 - Default Constructor")
# class C2 (C1):
#      def __init__(self):
#           print("C2 - Default Constructor")
# class C3(C2,C1):
#      def __init__(self):
#           print("C3 - Default Constructor")
#           super().__init__()       #* C2 call krel cause of priority
#           C1.__init__(self)
          
# co = C3()
# ^---------------------------------------------------------------------------------------
#! Finding the area of diffrent figures uisng polymorphism
#* Multiple Inheritance - using constructors 
# from math import pi
# class Circle:
#      def __init__(self):
#           self.r = float(input("Enter Radius of Circle : "))
#           self.ac = pi*self.r**2
#           print(f"Area of Circle : {round(self.ac,2)}")
#           print("-"*20)
# class Square():
#      def __init__(self):
#           self.s = float(input("Enter Side of Square : "))
#           self.asq = self.s*self.s
#           print(f"Area of Square : {self.asq}")
#           print("-"*20) 
# class Rect(Square,Circle):
#      def __init__(self):
#           self.l = float(input("Enter Lenght of Rectangle : "))
#           self.w = float(input("Enter Width of Rectangle : "))
#           self.ar = self.l*self.w
#           print(f"Area of Rectangle : {self.ar}")
           
#           print("-"*20)
#           super().__init__()       #! only super calls accordinf to  priority like in this square is priority
#           Circle.__init__(self)
  

# ro =Rect()
# ^---------------------------------------------------------------------------------------
#! Finding the area of diffrent figures uisng polymorphism
#* Multilevel Inheritance - with parameters - with super()
# from math import pi
# class Circle:
#      def __init__(self,r):
#           self.ac = pi*r**2
#           print("------------------------------------------")
#           print(f"Area of Circle : {round(self.ac,2)}")
# class Square(Circle):
#      def __init__(self,s):
#           self.asq = s*s
#           print(f"Area of Square : {self.asq}") 
#           print("------------------------------------------")
#           super().__init__(float(input("Enter Radius of Circle : ")))  
# class Rect(Square):
#      def __init__(self,l,w):                                                                 # noqa: E741
#           self.ar = l*w
#           print(f"Area of Rectangle : {self.ar}")
#           print("------------------------------------------")
#           super().__init__(float(input("Enter Side Of Square ---: ")))

# l = float(input("Enter Length of Rectangle : "))                                              # noqa: E741
# w = float(input("Enter Width of Rectangle : "))
# ro =Rect(l,w)
# # ^---------------------------------------------------------------------------------------
# #! Finding the area of diffrent figures uisng polymorphism
# #* Multilevel Inheritance - with parameters - with clasname()
# from math import pi
# class Circle:
#      def __init__(self,r):
#           ac = pi*r*r
#           print(f"Area Of Circle : {round(ac,2)}")

# class Square(Circle):
#      def __init__(self,s):
#           sa = s*s
#           print(f"Area of Circle : {sa}")

# class Rect(Square):
#      def __init__(self,l,w):
#           ar = l*w
#           print(f"Area of Rectangle : {ar}")
#           print("-----------------------------")
#           Square.__init__(self,float(input("Enter Side Of Square : ")))
#           print("-----------------------------")
         
 
#           Circle.__init__(self,float(input("Enter Radius of Circel : ")))
#           print("-----------------------------")
         
# l = float(input("Enter Length of Rectangle : "))                                              # noqa: E741
# w = float(input("Enter Width of Rectangle : "))
# ro =Rect(l,w)
       
# # ^---------------------------------------------------------------------------------------
# #! PolyExStrong15.py
# from math import pi
# class Circle:
#      def __init__(self,r):
#           ac = pi*r*r
#           print(f"Area Of Circle : {round(ac,2)}")

# class Square(Circle):
#      def __init__(self,s):
#           sa = s*s
#           print(f"Area of Circle : {sa}")

# class Rect(Square):
#      def __init__(self,s=0):pass

#      def area(self,l,w):  # noqa: E741
#           ar = l*w
#           print(f"Area of Rectangle : {ar}")


#           print("-----------------------------")
#           Square.__init__(self,float(input("Enter Side Of Square : ")))
#           print("-----------------------------")
#           Circle.__init__(self,float(input("Enter Radius of Circel : ")))
#           print("-----------------------------")
         
# ro =Rect()
# l = float(input("Enter Length of Rectangle : "))                                              # noqa: E741
# w = float(input("Enter Width of Rectangle : "))
# ro.area(l,w)
# # ^---------------------------------------------------------------------------------------
#! PolyExStrong15.py
# from math import pi
# class Circle:
#      def __init__(self,r):
#           self.ac = pi*r*r
#           print(f"Area Of Circle : {round(self.ac,2)}")

# class Square(Circle):
#      def __init__(self,s):
#           self.sa = s*s
#           print(f"Area of Circle : {self.sa}")

# class Rect(Square):
#      def __init__(self,s=0):
#           print("-----------------------------")
#           Square.__init__(self,float(input("Enter Side Of Square : ")))
#           print("-----------------------------")
#           Circle.__init__(self,float(input("Enter Radius  : ")))
#           print("-----------------------------")

#      def area(self,l,w):  # noqa: E741
#           self.ar = l*w
#           print(f"Area of Rectangle : {self.ar}")


          
         
# ro =Rect()
# l = float(input("Enter Length : "))                                              # noqa: E741
# w = float(input("Enter Width : "))
# ro.area(l,w)