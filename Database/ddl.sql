-- 06-02-2025
 create database school;
 use school;
 create table teachers(tid int , tname varchar(100),gender char(1),
 doj date);
 rename table teachers to faculty;
 alter table faculty add tsalary decimal(10,2);
 alter table faculty add(tage int);
 alter table faculty change tsalary salary decimal(10.2);
 alter table faculty drop column salary; 
 alter table faculty add tsalary decimal(10.2) after tname;
 alter table faculty drop tsalary;



-- 07-02-2025
 create database school;
 use school;
 create table students(sid int, sname varchar(30),email varchar(50),phoneno int);




-- add column students
alter table students add gender char(1);

-- add phno after sname
 alter table students add phno int after sname ;

-- rename column name 
alter table students change phno phonno int;

-- drop  column name
 alter table students drop gender; 

-- drop table faculty;
 drop table faculty; 

-- drop database
drop database school;
