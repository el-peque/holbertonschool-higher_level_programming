--  lists all shows contained in hbtn_0d_tvshows that have at least one genre linked
SELECT name AS genre, COUNT(genre_id) AS number_of_shows FROM tv_genres LEFT JOIN tv_show_genres ON tv_show_genres.genre_id = tv_genres.id GROUP BY genre ORDER BY number_of_shows DESC;
