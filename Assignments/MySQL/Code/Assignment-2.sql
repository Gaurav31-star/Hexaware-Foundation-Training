show databases;
create database SISDB;
use SISDB;

create table Students(student_id int,first_name text,last_name text,date_of_birth date,email text,phone_number
 int,primary key(student_id));
 desc students;
 
 create table Teacher(teacher_id int,first_name text,last_name text,email text,primary key(teacher_id));
 desc teacher;
 
create table courses(course_id int,course_name text,credits int,teacher_id int,primary key(course_id), 
foreign key(teacher_id) references teacher(teacher_id));
desc courses;

create table enrollments(enrollment_id int,student_id int,course_id int,enrollemnt_date date,primary key(enrollment_id),
foreign key(student_id) references Students(student_id),
foreign key(course_id) references courses(course_id));
desc enrollments;

create table Payments(payment_id int primary key,student_id int, amount int,payment_date date,
foreign key(student_id) references Students(student_id));
desc students;

INSERT INTO Students VALUES (1, "Rahul", "Gupta", "2000-03-15", "rahul.gupta@email.com", 1234567890),
(2, "Priya", "Sharma", "1999-07-20", "priya.sharma@email.com", 1234567890),
(3, "Amit", "Patel", "2001-05-10", "amit.patel@email.com", 1234567890),
(4, "Sneha", "Singh", "2002-02-25", "sneha.singh@email.com", 1234567890),
(5, "Riya", "Verma", "1998-12-08", "riya.verma@email.com", 1234567890),
(6, "Kunal", "Yadav", "2000-11-12", "kunal.yadav@email.com", 1234567890),
(7, "Swati", "Das", "1999-09-05", "swati.das@email.com", 1234567890),
(8, "Raj", "Kumar", "2001-08-18", "raj.kumar@email.com", 1234567890),
(9, "Neha", "Chopra", "1997-06-22", "neha.chopra@email.com", 1234567890),
(10,"Vikram", "Saxena","2002-04-30", "vikram.saxena@email.com", 1234567890);
select * from students;

INSERT INTO Teacher VALUES (1, "Dr. Anand", "Sharma", "anand.sharma@email.com"),
(2, "Prof. Deepa", "Patil", "deepa.patil@email.com"),
(3, "Mrs. Priya", "Singh", "priya.singh@email.com"),
(4, "Mr. Karthik", "Rao", "karthik.rao@email.com"),
(5, "Dr. Nisha", "Verma", "nisha.verma@email.com"),
(6, "Prof. Amit", "Khanna", "amit.khanna@email.com"),
(7, "Mrs. Shweta", "Kumar", "shweta.kumar@email.com"),
(8, "Mr. Rahul", "Kumar", "rahul.kumar@email.com"),
(9, "Mr. Shyam", "Ranjan", "shyam.ranjan@email.com"),
(10, "Mrs. Shweta", "Rao", "shweta.rao@email.com");
select * from teacher;

INSERT INTO Courses VALUES (1, "Advanced Programming Concepts", 4, 7),
(2, "Cybersecurity Fundamentals", 4, 1),
(3, "Database Management Systems", 2, 7),
(4, "Data Visualization Techniques", 2, 6),
(5, "Environmental Science Fundamentals", 3, 5),
(6, "History of Art and Culture", 3, 4),
(7, "Introduction to Computer Science", 3, 2),
(8, "Machine Learning Basics", 3, 6),
(9, "Mobile App Development Fundamentals", 2, 1),
(10,"Software Engineering Principles", 3, 1);
select * from courses;

INSERT INTO Enrollments VALUES (1, 1, 3, '2023-01-05'),
(2, 2, 8, '2023-02-10'),
(3, 3, 4, '2023-03-15'),
(4, 4, 10, '2023-04-20'),
(5, 5, 7, '2023-05-25'),
(6, 6, 1, '2023-06-01'), 
(7, 7, 2, '2023-07-07'), 
(8, 8, 5, '2023-08-13'),
(9, 9, 9, '2023-09-19'),
(10, 10, 8, '2023-10-25'); 
select * from enrollments;

INSERT INTO Payments VALUES (1, 1, 500.00, '2023-01-10'),
(2, 2, 750.50, '2023-02-15'),
(3, 3, 400.25, '2023-03-20'),
(4, 4, 600.75, '2023-04-25'),
(5, 5, 900.00, '2023-05-30'),
(6, 6, 350.50, '2023-06-05'),
(7, 7, 800.25, '2023-07-10'),
(8, 8, 550.75, '2023-08-15'),
(9, 9, 700.00, '2023-09-20'),
(10, 10, 450.50, '2023-10-25');
select * from payments;

/* task 2*/
/*1*/
INSERT INTO Students VALUES(21, "John", "Doe", "1995-08-15", "john.doe@example.com", 1234567890);
select * from students;
/*2*/
INSERT INTO Enrollments VALUES(31, 4, 7, '2023-12-2');
select * from enrollments;
/*3*/
UPDATE Teacher SET email = 'verma.nisha@hotmail.com' WHERE teacher_id = 5;
select * from teacher;
/*4*/
DELETE FROM Enrollments WHERE student_id = 4 AND course_id = 7;
select * from enrollments;
/*5*/
UPDATE Courses SET teacher_id = 3 WHERE course_id = 5;
select * from courses;
/*6*/
DELETE FROM Students WHERE student_id = 4;
/*7*/
UPDATE Payments SET amount = 675.25 WHERE payment_id = 15;
select * from payments;

/*task 3*/
/*1*/
SELECT s.student_id, s.first_name, s.last_name, SUM(p.amount) AS total_payments
FROM Students s
JOIN Payments p ON s.student_id = p.student_id
WHERE s.student_id = 5
GROUP BY s.student_id, s.first_name, s.last_name;

/*2*/
SELECT c.course_id, c.course_name, COUNT(e.student_id) AS enrolled_students
FROM Courses c
LEFT JOIN Enrollments e ON c.course_id = e.course_id
GROUP BY c.course_id, c.course_name;

/*3*/
SELECT s.first_name, s.last_name
FROM Students s
LEFT JOIN Enrollments e ON s.student_id = e.student_id
WHERE e.student_id IS NULL;

/*4*/
SELECT s.first_name, s.last_name, c.course_name
FROM Students s
JOIN Enrollments e ON s.student_id = e.student_id
JOIN Courses c ON e.course_id = c.course_id;

/*5*/
SELECT t.first_name AS teacher_first_name, t.last_name AS teacher_last_name, c.course_name
FROM Teacher t
JOIN Courses c ON t.teacher_id = c.teacher_id;

/*6*/
SELECT s.first_name, s.last_name, e.enrollment_date
FROM Students s
JOIN Enrollments e ON s.student_id = e.student_id
JOIN Courses c ON e.course_id = c.course_id
WHERE c.course_name = 'Data Visualization Techniques';

/*7*/
SELECT s.first_name, s.last_name
FROM Students s
LEFT JOIN Payments p ON s.student_id = p.student_id
WHERE p.student_id IS NULL;

/*8*/
SELECT c.course_id, c.course_name
FROM Courses c
LEFT JOIN Enrollments e ON c.course_id = e.course_id
WHERE e.course_id IS NULL;

/*9*/
SELECT e1.student_id, COUNT(*) AS enrollments_count
FROM Enrollments e1
JOIN Enrollments e2 ON e1.student_id = e2.student_id
WHERE e1.course_id <> e2.course_id
GROUP BY e1.student_id
HAVING enrollments_count > 1;

/*10*/
SELECT t.teacher_id, t.first_name, t.last_name
FROM Teacher t
LEFT JOIN Courses c ON t.teacher_id = c.teacher_id
WHERE c.course_id IS NULL;

/*Task 4*/
/*1*/
SELECT AVG(enrollment_count) AS average_students_per_course
FROM (
    SELECT c.course_id, COUNT(e.student_id) AS enrollment_count
    FROM Courses c
    LEFT JOIN Enrollments e ON c.course_id = e.course_id
    GROUP BY c.course_id
) AS enrollment_counts;

/*2*/
SELECT s.student_id, s.first_name, s.last_name, p.amount AS highest_payment_amount
FROM Students s
JOIN Payments p ON s.student_id = p.student_id
WHERE p.amount = (
    SELECT MAX(amount)
    FROM Payments);
    
/*3*/
SELECT c.course_id, c.course_name, enrollment_counts.max_enrollments
FROM Courses c
JOIN (
    SELECT course_id, COUNT(student_id) AS max_enrollments
    FROM Enrollments
    GROUP BY course_id
    HAVING COUNT(student_id) = (
        SELECT MAX(enrollment_count)
        FROM (
            SELECT COUNT(student_id) AS enrollment_count
            FROM Enrollments
            GROUP BY course_id
        ) AS counts
    )
) AS enrollment_counts ON c.course_id = enrollment_counts.course_id;

/*4*/
SELECT t.teacher_id, t.first_name, t.last_name, COALESCE(SUM(p.amount), 0) AS total_payments
FROM Teacher t
LEFT JOIN Courses c ON t.teacher_id = c.teacher_id
LEFT JOIN Enrollments e ON c.course_id = e.course_id
LEFT JOIN Payments p ON e.student_id = p.student_id
GROUP BY t.teacher_id, t.first_name, t.last_name;

/*5*/
SELECT s.student_id, s.first_name, s.last_name
FROM Students s
WHERE (
    SELECT COUNT(DISTINCT course_id)
    FROM Courses) = (SELECT COUNT(DISTINCT e.course_id)
    FROM Enrollments e
    WHERE e.student_id = s.student_id);
    
/*6*/
SELECT t.teacher_id, t.first_name, t.last_name
FROM Teacher t
WHERE t.teacher_id NOT IN (
    SELECT DISTINCT c.teacher_id
    FROM Courses c);
    
/*7*/
SELECT AVG(student_age) AS average_age
FROM (
    SELECT TIMESTAMPDIFF(YEAR, date_of_birth, CURDATE()) AS student_age
    FROM Students) AS student_ages;
    
/*8*/
SELECT course_id, course_name FROM Courses
WHERE course_id NOT IN (
    SELECT DISTINCT course_id
    FROM Enrollments);
    
/*9*/
SELECT e.student_id, e.course_id, SUM(p.amount) AS total_payments
FROM Enrollments e
LEFT JOIN Payments p ON e.student_id = p.student_id
GROUP BY e.student_id, e.course_id;

/*10*/
SELECT student_id
FROM Payments
GROUP BY student_id
HAVING COUNT(payment_id) > 1;

/*11*/
SELECT s.student_id, s.first_name, s.last_name, COALESCE(SUM(p.amount), 0) AS total_payments
FROM Students s
LEFT JOIN Payments p ON s.student_id = p.student_id
GROUP BY s.student_id, s.first_name, s.last_name;

/*12*/
SELECT c.course_id, c.course_name, COUNT(e.student_id) AS enrolled_students
FROM Courses c
LEFT JOIN Enrollments e ON c.course_id = e.course_id
GROUP BY c.course_id, c.course_name;

/*13*/
SELECT AVG(p.amount) AS average_payment_amount
FROM Students s
JOIN Payments p ON s.student_id = p.student_id;





























