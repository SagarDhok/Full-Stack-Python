def lcase():
   text = input("ENTER A LINE OF TEXT : ")
   lst = []
   for i in text:
      if "A" <= i <= "Z":
         lst.append(chr(ord(i)+32))
      else:
          lst.append(i)
   x = "".join(lst)
   print(f"LOWERCASE OF GIVEN TEXT : {x}")


def ucase():
   text = input("ENTER A LINE OF TEXT : ")
   lst = []
   for i in text:
      if "a" <= i <= "z":
         lst.append(chr(ord(i)-32))
      else:
          lst.append(i)

   y = "".join(lst)
   print(f"UPPERCASE OF GIVEN TEXT : {y}")


lcase()
ucase()


# MY NAME IS SAGAR SANTOSH DHOK  