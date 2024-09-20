-----------------------------------------------------
-- lieu
-----------------------------------------------------
DROP TABLE IF EXISTS lieu CASCADE ;
CREATE TABLE lieu(
    id_lieu    SERIAL PRIMARY KEY,
);

-----------------------------------------------------
-- points
-----------------------------------------------------
DROP TABLE IF EXISTS points CASCADE ;
CREATE TABLE points(
    id_points    SERIAL PRIMARY KEY,
    coordonnée FLOAT;
);
