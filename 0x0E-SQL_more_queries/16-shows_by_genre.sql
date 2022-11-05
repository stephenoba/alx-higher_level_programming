-- lists all shows, and all genres linked to that show, from the
-- database hbtn_0d_tvshows
SELECT		title, name
FROM		tv_shows AS ts
INNER JOIN	tv_show_genres as tsg
ON		(ts.id = tsg.show_id)
INNER JOIN	tv_genres as tg
ON		(tg.id = tsg.genre_id)
ORDER BY	title, name;
