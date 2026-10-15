-- Example queries for importing data/events.csv into SQLite table events(user_id TEXT,event TEXT)
SELECT event, COUNT(DISTINCT user_id) AS users FROM events GROUP BY event;
SELECT COUNT(DISTINCT CASE WHEN event='purchase' THEN user_id END)*1.0 / NULLIF(COUNT(DISTINCT CASE WHEN event='view' THEN user_id END),0) AS conversion FROM events;
