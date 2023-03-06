-- DDL - Data Definition Language

create database db_practice;

-- Create table 

use db_practice;
create table dinner
(
	id int not null auto_increment primary key, 
    firstname varchar(20) not null, 
    food varchar(100) null
);

-- delete the table 

drop table dinner;

-- DQL - Data Query Language 

select * from dinner;

-- DML - Data Manipulation Language
-- insert / update / delete

insert into dinner (firstname, food)
values ("Victoria", "Pasta"), ("Indie", "Stir Fry"), ("Aisha", "Biscuits"), ("Saynab", null);

update dinner 
set food = "Proper food plus biscuits" 
where id = 2; 

update dinner 
set food = "Stir fry" 
where id = 1; 

delete from dinner
where id = 1;

-- This will delete everything from the table "dinner"
delete from dinner; 