-- DDL - Data Definition Language

create database db_practice;

-- Create table 

use db_practice;
create table dinner
(
	id int not null, 
    firstname varchar(20) not null, 
    food varchar(100) null
);

-- DQL - Data Query Language 

select * from dinner;

-- DML - Data Manipulation Language
-- insert / update / delete

insert into dinner 
values (2, "Victoria", "Pasta");

update dinner 
set food = "Proper food plus biscuits" 
where id = 2; 