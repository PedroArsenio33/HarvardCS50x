SELECT AVG(energy) AS drake_energy FROM songs WHERE artist_id IN (SELECT id FROM artists WHERE name = 'Drake');
