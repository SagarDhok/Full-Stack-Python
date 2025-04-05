
use school;


-- create index stdindex on students(sname); 
CREATE INDEX stdindx ON students (sname);

-- create view stdinfo as select sname,smarks 
-- from students where gender = "m";


-- select * from stdinfo;
SELECT stdindx FROM students;

