create database dbAgenda;
use dbAgenda;

drop database dbAgenda;


create table tbContato(
id int not null primary key auto_increment,
nome varchar(12) not null,
email varchar(50) not null,
numero varchar(15) not null
);



select * from tbContato;


