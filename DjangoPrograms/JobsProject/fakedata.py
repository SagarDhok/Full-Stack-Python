import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'JobsProject.settings')
import django
django.setup()


from faker import Faker
from random import *
from Jobsapp.models import Hydjobs,Punejobs,Bangjobs

fake = Faker()

def fphonenumber():
   d1 = randint(6,9)
   nums = ""+str(d1)
   for i in range(9):
      nums += str(randint(0,9))
   return int(nums)
   

 
n = int(input('Enter records for hyd : '))
for i in range(n):
  fdate =  fake.date()
  fcompany =  fake.company()
  ftitle =  fake.job()
  feligibility= fake.random_element(elements=["BTech", "MCA", "BSc", "Diploma"])
  fadress =  fake.address()
  femail =  fake.email()  
  Hydjobs.objects.get_or_create(date = fdate,company = fcompany,   title = ftitle, eligibility = feligibility,address  = fadress,email= femail,phonenumber = fphonenumber())  

print(f"{n} Records inserted Succesfully ")



 
n = int(input('Enter records for pune : '))
for i in range(n):
  fdate =  fake.date()
  fcompany =  fake.company()
  ftitle =  fake.job()
  feligibility= fake.random_element(elements=["BTech", "MCA", "BSc", "Diploma"])
  fadress =  fake.address()
  femail =  fake.email()  
  Punejobs.objects.get_or_create(date = fdate,company = fcompany,   title = ftitle, eligibility = feligibility,address  = fadress,email= femail,phonenumber = fphonenumber())  

print(f"{n} Records inserted Succesfully ")



n = int(input('Enter records for bang : '))
for i in range(n):
  fdate =  fake.date()
  fcompany =  fake.company()
  ftitle =  fake.job()
  feligibility= fake.random_element(elements=["BTech", "MCA", "BSc", "Diploma"])
  fadress =  fake.address()
  femail =  fake.email()  
  Bangjobs.objects.get_or_create(date = fdate,company = fcompany,   title = ftitle, eligibility = feligibility,address  = fadress,email= femail,phonenumber = fphonenumber())  

print(f"{n} Records inserted Succesfully ")