-- labels.sql
/*
"id": 76811,
    "url": "https://api.github.com/repos/pandas-dev/pandas/labels/Bug",
    "name": "Bug",
    "color": "e10c02",
    "default": false
*/

create or replace table labels(
cnt int auto_increment primary key,
id int not null,
url varchar(1000) not null,
name varchar(50) not null,
color varchar(100) not null,
def char(5) not null
);

