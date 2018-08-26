
SELECT COUNT(*)
FROM (SELECT docid, COUNT(count) as term_count
FROM frequency
GROUP BY docid
HAVING term_count > 300)