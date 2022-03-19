------------Problem------------
/*
There is a table World
這裡有張 World 表

+-----------------+------------+------------+--------------+---------------+
| name            | continent  | area       | population   | gdp           |
+-----------------+------------+------------+--------------+---------------+
| Afghanistan     | Asia       | 652230     | 25500100     | 20343000      |
| Albania         | Europe     | 28748      | 2831741      | 12960000      |
| Algeria         | Africa     | 2381741    | 37100000     | 188681000     |
| Andorra         | Europe     | 468        | 78115        | 3712000       |
| Angola          | Africa     | 1246700    | 20609294     | 100990000     |
+-----------------+------------+------------+--------------+---------------+

A country is big if it has an area of bigger than 3 million square km or a population of more than 25 million.

Write a SQL solution to output big countries' name, population and area.

For example, according to the above table, we should output:

如果一個國家的面積超過300萬平方公里，或者人口超過2500萬，那麼這個國家就是大國家。

編寫一個SQL查詢，輸出表中所有大國家的名稱、人口和麵積。

例如，根據上表，我們應該輸出:

+--------------+-------------+--------------+
| name         | population  | area         |
+--------------+-------------+--------------+
| Afghanistan  | 25500100    | 652230       |
| Algeria      | 37100000    | 2381741      |
+--------------+-------------+--------------+

*/

------------Answer------------
SELECT name, population, area
FROM World
WHERE area > 3000000 --找面積超過300萬的國家
OR population > 25000000; --或是人口超過2500萬也符合