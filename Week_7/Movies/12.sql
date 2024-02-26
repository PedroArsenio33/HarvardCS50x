SELECT title FROM movies WHERE id IN (
    SELECT id_brad FROM (
        SELECT movie_id AS id_brad FROM stars WHERE person_id = (
            SELECT id FROM people WHERE name = 'Bradley Cooper'
        )
    )
    JOIN (
        SELECT movie_id as id_jen FROM stars WHERE person_id = (
            SELECT id FROM people WHERE name = 'Jennifer Lawrence'
        )
    )
    ON id_brad = id_jen
);
