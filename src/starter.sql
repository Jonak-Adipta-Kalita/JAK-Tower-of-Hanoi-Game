DROP DATABASE IF EXISTS tower_of_hanoi;

CREATE DATABASE IF NOT EXISTS tower_of_hanoi;
USE tower_of_hanoi;

CREATE TABLE players (
    id int auto_increment primary key,
    username varchar(100) unique not null,
    password varchar(100) not null
);