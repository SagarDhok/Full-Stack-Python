
--  use school;
--  alter table students drop phoneno;

--  insert into students values (10,'karna',9988,'kr@gmailcom');

--  truncate table students;

-- use school;
--  truncate table students;
-- drop table students;

-- drop database office;

-- insert into students values (10,'karna',9988,'kr@gmailcom'),(20,"jay",4444,"jay@gmail.com"),(30,"hanuman",5555,"hmtope@gmail.com");


-- 10-02-2025
-- IMP
-- drop vs truncate
-- PRIMARY KEY AND FOREIGN KEY
-- unique one null values

-- create database office;
 -- use office;
-- create table employees(eid int, ename varchar(30),gender char(1), salary decimal(10,2), doj date); 

-- insert into employees values(112,"karan","M",50000,"2025-01-15");


-- create table employees(eid int auto_increment primary key,ename varchar(30) not null,age int check (age>=18),country varchar(30) default "india",salary decimal(10,2));



-- insert into employees values(101,"rexon",18,"india",20000 );

--  insert into employees(ename , age,salary) values ("kkk",22,200000);

-- alter table employees change eid eid int  AUTO_INCREMENT; 

--  insert into employees(ename,age,salary) values ("jay",20,3000);

-- use school;
-- create table teacher(tid int auto_increment primary key ,tname varchar(30) NOT NULL ,phno bigint not null, country varchar(30) default "india",salary int check(salary>=20000));


-- 11-02-2025

-- UPDATE
 -- use office ;
-- update employees set salary = 2000 where ename = 'karan' ;

-- update employees set country = "usa" where eid = 107

-- DELETE 
-- delete from employees where ename condition;
-- delete from employees where ename = "karan";
-- preference should be given to unique like id 


