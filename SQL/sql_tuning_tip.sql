--Optimizing SQL tips
--Specify columns in use
Problem:  SELECT * FROM Table
Solution: SELECT COLUMN_1,COLUMN_6,COLUMN_11 FROM Table
--Using like query logic instead of apply string function on table column data
Problem:  SELECT ... WHERE SUBSTR(customer_name, 1, 4) = 'Bard'
Solution: SELECT ... WHERE customer_name LIKE 'Bard%'
--Using comparison logic instead of getting date information on table column data
Problem:  SELECT ... WHERE TO_CHAR(DATE birth_date 'YYYY') = 2022
Solution: SELECT ... WHERE birth_date >= TO_DATE('2022/01/01', 'yyyy/mm/dd') AND birth_date < TO_DATE('2023/01/01', 'yyyy/mm/dd')
--Caculation on variables instead of on table column
Problem:  SELECT ... WHERE (trunc(SYSDATE) - submit_date) > 28
Solution: SELECT ... WHERE submit_date <= (trunc(SYSDATE)-28)

