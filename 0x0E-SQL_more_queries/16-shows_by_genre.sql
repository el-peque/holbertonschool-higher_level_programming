--  lists all shows contained in hbtn_0d_tvshows that have at least one genre linked
SELECT tv_shows.title, tv_genres.name FROM tv_shows LEFT JOIN tv_show_genres ON tv_shows.id = show_id LEFT JOIN tv_genres ON tv_genres.id = genre_id ORDER BY tv_shows.title ASC, tv_genres.name;
