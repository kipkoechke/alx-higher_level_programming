-- Retrieve a list of TV shows in the 'hbtn_0d_tvshows' database without the 'Comedy' genre.
-- Records are sorted by ascending show title.
SELECT DISTINCT t.`title`
FROM `tv_shows` AS t
LEFT JOIN `tv_show_genres` AS s
ON s.`show_id` = t.`id`
LEFT JOIN `tv_genres` AS g
ON g.`id` = s.`genre_id`
WHERE t.`title` NOT IN (
    SELECT DISTINCT t.`title`
    FROM `tv_shows` AS t
    INNER JOIN `tv_show_genres` AS s
    ON s.`show_id` = t.`id`
    INNER JOIN `tv_genres` AS g
    ON g.`id` = s.`genre_id`
    WHERE g.`name` = "Comedy"
)
ORDER BY t.`title`;
