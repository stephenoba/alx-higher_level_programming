-- lists all shows contained in hbtn_0d_tvshows that have
-- at least one genre linked (LEFT JOIN)
SELECT		ts.title, tsg.genre_id
FROM		tv_shows AS ts
LEFT JOIN	tv_show_genres AS tsg
ON		(ts.id = tsg.show_id)
ORDER BY	ts.title, tsg.genre_id;
