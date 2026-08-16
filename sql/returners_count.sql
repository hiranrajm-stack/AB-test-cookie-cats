select version,count(*) as total_players,sum(cast(retention_7 as INT64))as day7_returners
from `cookie-cats-ab-test.cookie_cats_ab_test.cookie_cats_raw`
group by version;
