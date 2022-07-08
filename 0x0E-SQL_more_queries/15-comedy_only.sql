--  lists all shows contained in hbtn_0d_tvshows that have at least one genre linked
SELECT tv_shows.title FROM tv_shows JOIN tv_show_genres ON tv_shows.id = show_id JOIN tv_genres ON tv_genres.id = genre_id WHERE name = 'Comedy' ORDER BY tv_shows.title ASC;
