-- Retrieve a list of all cities in the 'hbtn_0d_usa' database.
-- Records are sorted in ascending order of cities.id.
SELECT c.`id`, c.`name`, s.`name`
FROM `cities` AS c
INNER JOIN `states` AS s
ON c.`state_id` = s.`id`
ORDER BY c.`id`;
