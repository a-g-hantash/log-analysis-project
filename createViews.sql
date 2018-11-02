CREATE VIEW stat_log AS
SELECT COUNT(*) AS stat, status, cast(time AS date) AS day
FROM log
WHERE status LIKE '%404%'
GROUP BY status, day
ORDER BY stat DESC
LIMIT 3;
    
CREATE VIEW visitors_in_total AS
SELECT count(*) AS visitors, cast(time AS date) AS errorTime
FROM log
GROUP BY errorTime;
    

CREATE VIEW countError AS
SELECT * FROM stat_log JOIN visitors_in_total
ON stat_log.day = visitors_in_total.errorTime;
    