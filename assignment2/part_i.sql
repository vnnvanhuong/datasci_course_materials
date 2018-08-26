--Find the best matching document to the keyword query washington taxes treasury

SELECT sum(a.count * b.count) as count
FROM (SELECT * FROM frequency) as a
JOIN (SELECT * FROM (
	SELECT 'q' as docid, 'washington' as term, 1 as count 
		UNION
	SELECT 'q' as docid, 'taxes' as term, 1 as count
		UNION 
	SELECT 'q' as docid, 'treasury' as term, 1 as count
	)) as b
ON a.term = b.term
GROUP BY a.docid
ORDER BY count DESC
LIMIT 1