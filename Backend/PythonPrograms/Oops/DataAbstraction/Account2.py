
#^-----------------------------------------------------------------------------------------
#! Data Encapsulation 
#*At Data Member Level  - Through instance method 

# class Account:
#      def getval(self):
#           self.__acno = 149849320
#           self.name = "Akshay"
#           self.__bal = 1000
#           self.__pin = 1234
#           self.bank = "SBI"
#^-----------------------------------------------------------------------------------------
#! Data Encapsulation - Possible but not recommended 
#* At Data Member Level  - Through ClassLevel method
# class Account:
#      @classmethod
#      def getval(cls):
#           cls.__acno = 429708
#           cls.name = "karan"
#           cls.__bal = 2000
#           cls.__pin = 1234
#           cls.bank = "SBI"
#^-----------------------------------------------------------------------------------------
#! Data Encapsulation - possible but not recommended
#*  At Data Member Level  - Through Static method
# class Account:
#      @staticmethod
#      def getval(obj):
#           obj.__acno = 429708
#           obj.name = "karan"
#           obj.__bal = 2000
#           obj.__pin = 1234
#           obj.bank = "SBI"
#^-----------------------------------------------------------------------------------------