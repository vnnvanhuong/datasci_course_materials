-- Write a query to compute the similarity matrix DDT.

SELECT DISTINCT sum(a.count * b.count)
FROM (SELECT * FROM frequency WHERE docid = '10080_txt_crude') as a
JOIN (SELECT * FROM frequency WHERE docid = '17035_txt_earn') as b
ON a.term = b.term
