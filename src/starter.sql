DROP DATABASE IF EXISTS tower_of_hanoi;

CREATE DATABASE IF NOT EXISTS tower_of_hanoi;
USE tower_of_hanoi;

CREATE TABLE players (
    id int auto_increment primary key,
    username varchar(100) unique not null,
    password varchar(100) not null
);

CREATE TABLE scores (
    id int auto_increment primary key,
    score varchar(100) not null,
    moves varchar(100) not null,
    CONSTRAINT fk_score FOREIGN KEY (id) REFERENCES players(id) ON DELETE CASCADE
)