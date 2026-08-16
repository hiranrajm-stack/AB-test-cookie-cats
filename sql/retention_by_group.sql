SELECT 
  version, COUNT(*) AS total_players,
  AVG(CAST(retention_1 AS INT64)*100) AS day1_retention,
  AVG(CAST(retention_7 AS INT64)*100) AS day7_retention
FROM `cookie-cats-ab-test.cookie_cats_ab_test.cookie_cats_raw`
GROUP BY version;

