create database if not exists db_library;

use db_library;
create table author
(
	author_id int not null auto_increment primary key, 
    author_name varchar(100) null
);

create table genre
(
	genre_id int not null auto_increment primary key, 
    genre_name varchar(100) null
);

create table publisher
(
	publisher_id int not null auto_increment primary key, 
    publisher_name varchar(100) null
);

create table book
(
	book_id int not null auto_increment primary key, 
    title varchar(255) not null, 
    ISBN int not null, 
    quantity int not null, 
    genre_id int, 
    publisher_id int, 
    published_date date,
    added_date date,
    price float,
    CONSTRAINT genre_id FOREIGN KEY (genre_id) references genre(genre_id), 
    CONSTRAINT publisher_id FOREIGN KEY (publisher_id) references publisher(publisher_id)
);

create table book_author
(
	author_id int,
	book_id int,
	CONSTRAINT author_id FOREIGN KEY (author_id) references author(author_id), 
	CONSTRAINT book_id FOREIGN KEY (book_id) references book(book_id) 
);

