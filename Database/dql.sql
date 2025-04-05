
-- select * from students;

-- select age, email from students;

-- select first_name , address from students;

-- select * from students where age>20

-- select first_name , phone_number from students where age<=20;

-- select first_name from students where gender = "female";

-- select * from students where address is null;

-- select * from students where address is not null;

-- write people name whose name start with b
-- select * from students where first_name like "B%";

-- select * from students where phone_number like "1%";  --first

-- write a query to show all people names endswith execute
-- select * from students where first_name like "%a";   -- last


-- waq to show all people whose second name is a

-- select * from students where first_name like "_a%";


-- waq to show all people whose Last third  letter is i
-- select * from students where first_name like "%i__";

-- 12-02-2025

-- use office;
-- select * from employee where age is not null;

-- print all employee whose second letter is a 
-- select * from employee where ename like "_a%";

-- printing whose name is rahul neha arjun
-- select * from employee where ename in ("Rahul Sharma","Neha Joshi","Arjun Mehta");


-- select * from employee where country = "india" order by  ename;
 -- select * from employee where country = "india" order by  ename Desc limit 2 offset 1;

-- select  * from employee where country = "india" order by ename; 
-- select  * from employee where country = "india" order by ename limit 2 offset 2;



-- 13-02-2025
use office;
-- select * from employee order by country  = "India" desc; 


-- select * from employee 
-- order by esal desc 
-- limit 1 offset 1; 

use school;
-- Create table students 
-- (sno int primary key auto_increment ,
-- sname varchar(20) not null,
-- smarks int, gender char(1));


-- INSERT INTO students VALUES
-- (1, "Aarav", 90, 'M'),
-- (2, "Anika", 85, 'F'),
-- (3, "Vivaan", 78, 'M'),
-- (4, "Adhira", 92, 'F'),
-- (5, "Ishaan", 65, 'M'),
-- (6, "Siya", 88, 'F'),
-- (7, "Reyansh", 72, 'M'),
-- (8, "Dhriti", 95, 'F'),
-- (9, "Kabir", 80, 'M'),
-- (10, "Avyaan", 75, 'M'),
-- (11, "Samaira", 89, 'F'),
-- (12, "Raj", 55, 'M'),
-- (13, "Diya", 91, 'F'),
-- (14, "Arjun", 68, 'M'),
-- (15, "Aanya", 82, 'F'),
-- (16, "Vihaan", 70, 'M'),
-- (17, "Navya", 93, 'F'),
-- (18, "Atharv", 77, 'M'),
-- (19, "Anaya", 87, 'F'),
-- (20, "Shaurya", 62, 'M');

-- select gender,count(gender)
--  from students group by gender;



-- write a query to print how many people from each country using customers table

-- write a query to print how many items sold per catogory 

-- write a query to print total marks achieved by students based on there gender

-- use school;
-- select gender, sum(smarks)
-- from students group by gender;

-- waq to print avg marks of students based on there gender 
-- select gender , avg(smarks)
-- from students group by gender;

-- write a query to print maximum marks of students based on genders

-- select max(smarks)
-- from students group by gender;

-- select gender,max(smarks)
-- from students group by gender;

-- select gender , min(smarks)
-- from students group by gender;

-- write a query to print total number of gender 
select distinct gender from students;
-- select count(distinct gender) from students; 

-- waq to print names of employees from different countries along with total country count
-- use office;
-- select country

,count(country), group_concat(ename) from employee group by country;