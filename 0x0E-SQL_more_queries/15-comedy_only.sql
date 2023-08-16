-- a script that lists all shows contained in the database hbtn_0d_tvshows
SELECT tv_shows.title
FROM tv_show_genres
LEFT JOIN tv_shows
ON tv_shows.id = tv_show_genres.show_id
JOIN tv_genres
ON tv_show_genres.genre_id = tv_genres.id
WHERE tv_genre_name = "Comedy"
ORDER BY tv_shows.title ASC;
