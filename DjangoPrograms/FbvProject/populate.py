import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'FbvProject.settings')
import django
django.setup()

from faker import Faker
from testapp.models import Employee
from random import *
fake = Faker()

def populate(n):
                for i in range(n):
                        feno = randint(1000,2000)
                        fename = fake.name()
                        fesal = randint(10000,20000)
                        feddr = fake.city()
                        emp_record = Employee.objects.get_or_create(
                        eno = feno,
                        ename = fename,
                        esal = fesal,
                        eaddr =feddr 
                        )


n = int(input('Enter Number of Employees : '))
populate(n)
print(f'{n} Records inserted successfully.....')