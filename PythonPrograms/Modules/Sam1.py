
#^ --------------------------------------------------------------------------------------------
#! USING "Import" STATEMENT 
#*SYNTAX-1:
# import Fun1
# import Fun2
# print("------------------------")
# Fun1.sumop()
# Fun1.subop()
# Fun2.lcase()
# Fun2.ucase()

#*SYNTAX-2:
# import Fun1 , Fun2
# Fun1.mulop()
# Fun2.ucase()
# Fun2.lcase()

#*SYNTAX-3:
# import Fun1 as f1
# import Fun2 as f2
# f1.subop()
# f2.ucase()


#*SYNTAX-4:
# import Fun1 as f1  , Fun2 as f2
# f1.mulop()
# f2.lcase()
# #^ --------------------------------------------------------------------------------------------
#! USING  "From.....Import"  STATEMENT 

#*SYNTAX-1:
# from Fun1 import subop , mulop
# from Fun2 import lcase

# subop()
# mulop()
# lcase()

#*SYNTAX-2:
# from Fun1 import sumop as sm , subop as sb
# from Fun2 import lcase as l , ucase as u
# sm()
# sb()
# l()
# u()

#*SYNTAX-3:
# from Fun1 import *
# from Fun2 import *
# sumop()
# subop()
# mulop()
# ucase()

# #^ --------------------------------------------------------------------------------------------
