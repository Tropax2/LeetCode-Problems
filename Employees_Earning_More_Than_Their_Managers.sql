-- Two solutions to the same problem.

SELECT emp.name AS "Employee"
FROM Employee AS emp JOIN Employee AS man
ON emp.managerId = man.id 
WHERE emp.managerId IS NOT NULL AND emp.salary > man.salary;

-------------------------

SELECT emp.name AS "Employee"
FROM Employee AS emp 
WHERE emp.managerId IS NOT NULL AND emp.salary > (SELECT man.salary FROM Employee AS man WHERE emp.managerId = man.Id)