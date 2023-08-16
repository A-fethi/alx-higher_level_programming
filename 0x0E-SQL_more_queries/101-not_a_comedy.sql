-- a script that lists all shows without the genre Comedy in the database hbtn_0d_tvshows.
SELECT tv_shows.title
FROM tv_shows
WHERE tv_shows.title NOT IN (
	SELECT tv_shows.title
	FROM tv_show_genres
	LEFT JOIN tv_shows
	ON tv_show_genres.genre_id = tv_shows.id
	JOIN tv_genres
	ON tv_show_genres.genre_id = tv_genres.id
	WHERE tv_genres.name = "Comedy"
)
GROUP BY tv_shows.title
ORDER BY tv_shows.title ASC;
