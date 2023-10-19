-- Retrieve a list of genres from the 'hbtn_0d_tvshows_rate' database, grouped by their ratings.
-- Records are ordered by descending rating.
SELECT g.`name`, SUM(r.`rate`) AS `rating`
FROM `tv_genres` AS g
INNER JOIN `tv_show_genres` AS s
ON s.`genre_id` = g.`id`
INNER JOIN `tv_show_ratings` AS r
ON r.`show_id` = s.`show_id`
GROUP BY g.`name`
ORDER BY `rating` DESC;
