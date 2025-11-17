
#^ --------------------------------------------------------------------------------------------
# addop = lambda a,b : a+b
# a= float(input("enter first value "))
# b= float(input("enter second value "))
# res = addop(a,b)
# print(res)
#^ --------------------------------------------------------------------------------------------
# def arithmenu():
#     print( """
#            1.ADDTION 
#            2.SUBSTRACTION
#            3.MULTIPLICATION
#            4.NORAMAL DIVISION
#            5.FLOORDIVISION
#            6.MODULODIVSION
#            7.EXPONENTION
#            8.EXIT 
#      """)
# sumop = lambda a, b : a+b 
# subop = lambda a, b : a-b 
# mulop = lambda a, b : a*b 
# divop = lambda a, b : a/b 
# floordivop = lambda a, b : a//b
# modulodivop = lambda a, b : a%b
# expop = lambda a,b : a**b 

# arithmenu()
# while(True):
#    ch = int(input("ENTER YOUR CHOICE : "))
#    match(ch):
#           case 1:
#            a = float(input("enter first value : "))
#            b = float(input("enter second value : "))
#            res = sumop(a,b)
#            print("sum : ",res)
           
#           case 2:
#            a = float(input("enter first value : "))
#            b = float(input("enter second value : "))
#            res = subop(a,b)
#            print("sub : ",res)
           
#           case 3:
#            a = float(input("enter first value : "))
#            b = float(input("enter second value : "))
#            res = mulop(a,b)
#            print("mul : ",res)
           
#           case 4:
#            a = float(input("enter first value : "))
#            b = float(input("enter second value : "))
#            res = divop(a,b)
#            print("divop : ",res)
           
#           case 5:
#            a = float(input("enter first value : "))
#            b = float(input("enter second value : "))
#            res = floordivop(a,b)
#            print("floordiv : ",res)
           
#           case 6:
#            a = float(input("enter first value : "))
#            b = float(input("enter second value : "))
#            res = modulodivop(a,b)
#            print("modulodiv : ",res)
   
#           case 7:
#            a = float(input("enter first value : "))
#            b = float(input("enter second value : "))
#            res = expop(a,b)
#            print("exponation : ",res)
   
#           case 8:
#             print("THANKS FOR USING PROGRAM ")
#             break
   
#           case _:
#                 print("INVALID INPUT ! PLEASE ENTER AGAIN  ")
           
#^ --------------------------------------------------------------------------------------------
#! PROGRAM FOR CALCULATING AREA OF DIFFRENT FIGURES LIKE CIRCLES , RECTANGLE ,SQUARES AND TRAINGLE

# def areamenu():
#      print("""
#               1. CIRCLE 
#               2. RECTANGLE 
#               3. SQUARE
#               4. TRAINGLE
#               5. EXIT 
           
# """)
# area_circle = lambda r : 3.14*r*r
# area_rectangle = lambda ln,wd : ln*wd
# area_square  = lambda s :  s*s
# area_triangle = lambda b,h : 0.5*b*h
     
# areamenu()
# while(True):
#        ch = int(input("ENTER YOUR CHOICE : ")) 
#        match(ch):
#             case 1:
#                 r =  float(input("ENTER RADIUS : "))
#                 res = area_circle(r)
#                 print("AREA OF CIRCLE IS : ",res)
#             case 2:
#                  ln = float(input("ENTER LENGTH OF RECTANGLE  : "))
#                  wd = float(input("ENTER WIDTH OF RECTANGLE  : "))
#                  res = area_rectangle(ln,wd)
#                  print("AREA OF RECTANGLE  IS : ",res)
#             case 3:
#                  s = float(input("ENTER SIDE OF SQUARE : "))
#                  res = area_square(s)
#                  print(res)
#             case 4 :
#                  b = float(input("ENTER BASE OF TRIANGEL : "))
#                  h= float(input("ENTER HEIGHT OF SQUARE :  "))
#                  res = area_triangle(b,h)
#                  print("AREA OF TRIANGE IS",res)
#             case 5 :
#                  print("THANKS FOR USING THIS PROGRAM")
#                  break
#             case _ :
#                  print("INVALID INPUT PLEASE ENTER AGAIN ; ")
       
#^ --------------------------------------------------------------------------------------------
#! PROGRAM FOR CALCULATING DIFFRENT TEMPRATURE CONVERSION USING ANONYMOUS FUNCTION 
# def temerature_menu():
#       print(
#         """
#         1. Celsius to Fahrenheit 
#         2. Fahrenheit to Celsius
#         3. Celsius to Kelvin
#         4. Kelvin to Celsius
#         5. Fahrenheit to Kelvin:
#         6. Kelvin to Fahrenheit
#         7. EXIT
#         """)
      
# c_f = lambda c :  (9/5) * c + 32
# f_c = lambda f :  (5/9) * (f - 32)
# c_k = lambda c : c + 273.15
# k_c = lambda k :  k - 273.15
# f_k = lambda f : (5/9) * (f - 32) + 273.15
# k_f = lambda k : (9/5) * (k - 273.15) + 32

      
# temerature_menu()
# while(True):
#     ch = int(input("ENTER YOUR CHOICE : "))
#     match(ch):
#        case 1:
#               c = float(input("ENTER TEMPERATURE IN CELCIUS : "))
#               res = c_f(c)
#               print("Celsius to Fahrenheit ",res)
#        case 2 :
#               f = float(input("ENTER TEMPERATURE IN FAHRENHEIT : "))
#               res = f_c(f)
#               print("Fahrenheit to Celsius",res)
#        case 3 :
#               c = float(input("ENTER TEMPERATURE IN CELCIUS : "))
#               res = c_k(c)
#               print("Celsius to Kelvin",res)
#        case 4 :
#               k = float(input("ENTER TEMPERATURE IN KELVIN : "))
#               res = k_c(k)
#               print(" Kelvin to Celsius",res)
#        case 5 :
#               f = float(input("ENTER TEMPERATURE IN FAHRENHEIT : "))
#               res = f_k(f)
#               print("Fahrenheit to Kelvin",res)
#        case 6:
#               k = float(input("ENTER TEMPERATURE IN KELVIN : "))
#               res = k_f(k)
#               print("Kelvin to Fahrenheit",res)
#        case 7 :
#                 print("THANKS FOR USING THIS PROGRAM ")
#                 break
#        case _ :
#                   print("INVALID INPUT PLEASE ENTER AGAIN ! ")     
#^ --------------------------------------------------------------------------------------------
#! PROGRAM FOR FINDING SMLLEST OF THREE NUMERICAL VALUES 
# sv =lambda a,b,c : a if  b>=a<c else b if a>b<=c else c if a>=c< b else "ALL VALUES ARE SAME "

# a = float(input("ENTER FIRST VALUE : "))
# b = float(input("ENTER SECOND VALUE : "))
# c = float(input("ENTER THIRD VALUE : "))
# res = sv(a,b,c)
# print(res)

#^ --------------------------------------------------------------------------------------------
#! PROGRAM FOR FINDING BIGGEST AND SMALLEST OF TWO NUMERICAL VALUES 
# bv = lambda a,b :a if a>b else b if b>a else " BOTH VALUES ARE SAME "
# sv = lambda a,b :a if a<b else b if b<a else " BOTH VALUES ARE SAME "


# a = float(input("ENTER FIRST VALUE : "))
# b = float(input("ENTER SECOND VALUE : "))
# res_bv = bv(a,b)
# res_sv = sv(a,b)
# print("BIGGEST VALUE IS",res_bv,type(res_bv))
# print("SMALLEST VALUE IS",res_sv,type(res_sv))

#^ --------------------------------------------------------------------------------------------

     



       
       
       