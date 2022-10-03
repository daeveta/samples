import pymysql

CREATE TABLE 'students' (
    id_student int,
    name varchar(45),
    last name varchar(45),
    marks int,
)

CREATE TABLE 'classes' (
    id_class int,
    number int,
    lesson varchar(45),
)

LEFT JOIN number n ON student.id_student = n.id_student