-- Retrieve a list of TV shows from the 'hbtn_0d_tvshows_rate' database, grouped by their ratings.
-- Records are ordered by descending rating.
SELECT t.`title`, SUM(r.`rate`) AS `rating`
FROM `tv_shows` AS t
INNER JOIN `tv_show_ratings` AS r
ON t.`id` = r.`show_id`
GROUP BY t.`title`
ORDER BY `rating` DESC;
