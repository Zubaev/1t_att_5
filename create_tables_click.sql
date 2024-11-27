create table test_table(id UInt32, 
name String,
age UInt16, 
salary Decimal(10, 2))
ENGINE = MergeTree()
ORDER BY id;



INSERT INTO test_table VALUES (1 , 'Alice', 30, 70000),
(2 , 'Bob', 25, 50000),
(3 , 'Cherlie', 35, 100000),
(4 , 'David', 40, 120000),
(5 , 'Eve', 28, 60000),
(6 , 'Frank', 50, 150000),
(7 , 'Grace', 33, 80000),
(8 , 'Hank', 29, 55000),
(9 , 'Ivy', 42, 110000),
(10 , 'Jack', 31, 90000);