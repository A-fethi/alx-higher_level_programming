-- a script that lists all shows contained in the database hbtn_0d_tvshows
SELECT tv_genres.name AS genre, COUNT(tv_genres.name) AS number_of_shows
FROM tv_show_genres
LEFT JOIN tv_genres
ON tv_show_genres.genre_id = tv_genres.id
GROUP BY genre
ORDER BY number_of_shows DESC;
