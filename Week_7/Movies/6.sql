SELECT AVG(rating) AS average_ratings_2012 FROM ratings WHERE movie_id IN (SELECT id FROM movies WHERE year = 2012);
