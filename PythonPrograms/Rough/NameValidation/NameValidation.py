from Exception import InvalidNameError,ZeroLenghtError,SpaceError

def NameValidation(name):
     if len(name)==0:
          raise ZeroLenghtError
     elif name.isspace():
          raise SpaceError
     else:
          words = name.split()
          for word in words:
               if not word.isalpha():
                    raise InvalidNameError
          else:
               return name


# from Exception import InvalidNameError,ZeroLenghtError,SpaceError

# def NameValidation(name):
#      if len(name)==0:
#           raise ZeroLenghtError
#      elif name.isspace():
#           raise SpaceError
#      else:
#           words = name.split()
#           res = True
#           for word in words:
#                if not word.isalpha():
#                     res = False
#           if res :
#                return name
#           else:
#                raise InvalidNameError