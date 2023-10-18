-- Retrieve a list of all cities in California from the 'hbtn_0d_usa' database.
-- Results are ordered by ascending cities.id.
SELECT `id`, `name`
FROM `cities`
WHERE `state_id` IN (
    SELECT `id`
    FROM `states`
    WHERE `name` = "California"
)
ORDER BY `id`;
