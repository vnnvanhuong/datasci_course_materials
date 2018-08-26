 -- multiply: Express A X B as a SQL query, referring to the class lecture for hints

-- SELECT *
-- FROM a
-- WHERE a.row_num = 2

-- SELECT *
-- FROM b
-- WHERE b.col_num = 3

SELECT DISTINCT sum(a.value * b.value)
FROM (SELECT * FROM a WHERE row_num = 2) as a
JOIN (SELECT * FROM b WHERE col_num = 3) as b
ON a.col_num = b.row_num