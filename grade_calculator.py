mysql> create database exam28;
Query OK, 1 row affected (0.55 sec)

mysql> use exam28;
Database changed

A)
mysql> create table emp(emp_no integer(3) primary key, name char(20) not null,department char(10));
Query OK, 0 rows affected, 1 warning (2.52 sec)

mysql> create table details(emp_no integer(3),foreign key(emp_no) references emp(emp_no),bpay integer(10),DA integer(10) null,PF integer(10) null);
Query OK, 0 rows affected, 4 warnings (1.83 sec)
 ______________
B)
mysql> INSERT INTO EMP VALUES(100,"Daniel","CSC");
Query OK, 1 row affected (0.