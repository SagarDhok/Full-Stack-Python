

use office;
-- create table customers
-- (customer_id int auto_increment primary key ,
-- first_name varchar(30) not null,
-- last_name varchar(30) not null,
-- age int not null, 
-- country varchar(10) not null);

-- insert into customers (first_name,last_name,age,country) values 
-- ('John', 'Doe', 25, 'USA'),
-- ('Alice', 'Smith', 30, 'UK'),
-- ('Bob', 'Johnson', 22, 'Canada'),
-- ('Mary', 'Williams', 28, 'Australia'),
-- ('James', 'Brown', 35, 'India');

-- create table orders (order_id int auto_increment primary key ,
-- item varchar(20) not null,
-- amount int not null,
-- customer_id int not null,
-- foreign key (customer_id) references 
-- customers(customer_id));

-- insert into orders (item,amount,customer_id) values 
-- ('Laptop', 1000, 1),
-- ('Smartphone', 500, 2),
-- ('Headphones', 150, 3),
-- ('Tablet', 300, 4),
-- ('Monitor', 400, 5);

-- write the first name of the customers and item they bought
-- select t1.first_name,t2.item
-- from customers as t1
-- inner join 
-- orders as t1
-- on t1.customer_id = t2.customer_id

-- select t1.first_name,t2.item
-- from customers as t1
-- inner join 
-- orders as t2
-- on t1.customer_id = t2.customer_id



-- select t1.first_name, sum(t2.amount)
-- from customers as t1
-- inner join 
-- orders as t2
-- on 
-- t1.customer_id = t2.customer_id
-- group by t1.first_name;


-- select t1.first_name, sum(t2.amount)
-- from customers as t1
-- left join 
-- orders as t2
-- on 
-- t1.customer_id = t2.customer_id
-- group by t1.first_name;


-- select t2.first_name, sum(t1.amount)
-- from customers as t2
-- right join 
-- orders as t1
-- on 
-- t2.customer_id = t1.customer_id
-- group by t2.first_name;


-- waq to print every cusotmer name with products they bought 
-- use office;

-- select t1.first_name,t2.item
-- from customers as t1
-- right join
-- orders as t2
-- on 
-- t1.customer_id = t2.customer_id;


-- divide student based gender
 -- avg there mark
 -- print only there averae is greater than 85
--  use school;
--  select gender ,avg(smarks)
--  from students group by gender having avg(smarks)>85;


