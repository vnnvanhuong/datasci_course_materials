SELECT DISTINCT count(*)
FROM (SELECT * FROM frequency WHERE term = 'world') as world
JOIN (SELECT * FROM frequency WHERE term = 'transactions') as transactions
ON world.docid = transactions.docid


