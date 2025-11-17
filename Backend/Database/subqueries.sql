
use office;

-- select country , max(esal)
-- from employee where country = "india"

-- select ename,esal
-- from employee 
-- where esal >(select country , max(esal)
-- from employee where country = "india"
-- ) ;
 
-- use school;
-- select sname,smarks 
-- from students 
-- where smarks>(
-- select avg(smarks)
-- from students group by gender
-- having gender = "m");



-- select avg(smarks)
-- from students where gender = "m" group by gender
-- ;

