SELECT name AS toystory_stars FROM people WHERE id IN (SELECT person_id FROM stars JOIN movies ON movie_id = id WHERE title = 'Toy Story');
