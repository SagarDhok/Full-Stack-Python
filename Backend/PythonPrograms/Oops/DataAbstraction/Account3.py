
#^-----------------------------------------------------------------------------------------
#! Data Encapsulation 
#* At Method level - Instance method
# class Account:
#      def __getval(self):
#           self.acno = 429708
#           self.name = "karan"
#           self.bal = 2000
#           self.pin = 1234
#           self.bank = "SBI"
#^-----------------------------------------------------------------------------------------
#! Data Encapsulation - Possible but not recommended 
#* At Method level - ClassLevel method
# class Account:
#      @classmethod
#      def __getval(cls):
#           cls.acno = 429708
#           cls.name = "karan"
#           cls.bal = 2000
#           cls.pin = 1234
#           cls.bank = "SBI"
#^-----------------------------------------------------------------------------------------
#! Data Encapsulation - possible but not recommended
#* At Method level - Staticmethod method
# class Account:
#      @staticmethod
#      def __getval(obj):
#           obj.acno = 429708
#           obj.name = "karan"
#           obj.bal = 2000
#           obj.pin = 1234
#           obj.bank = "SBI"
#^-----------------------------------------------------------------------------------------