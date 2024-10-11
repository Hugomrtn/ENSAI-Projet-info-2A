--------------------------------------------------------------
-- Création du schéma projet_2A
--------------------------------------------------------------
DROP SCHEMA IF EXISTS projet_2A CASCADE;
CREATE SCHEMA projet_2A;
-----------------------------------------------------
-- lieu
-----------------------------------------------------
DROP TABLE IF EXISTS lieu CASCADE ;
CREATE TABLE projet_2A.lieu(
    id_lieu SERIAL PRIMARY KEY
    nom TEXT
    niveau TEXT
    code INT
);
-----------------------------------------------------
-- points
-----------------------------------------------------
DROP TABLE IF EXISTS points CASCADE ;
CREATE TABLE projet_2A.points(
    id_point SERIAL PRIMARY KEY,
    long FLOAT,
    lat FLOAT,
);
-----------------------------------------------------
-- polygones
-----------------------------------------------------
DROP TABLE IF EXISTS polygones CASCADE ;
CREATE TABLE projet_2A.polygones(
    id_polygone SERIAL PRIMARY KEY,
);
-----------------------------------------------------
-- association_polygone_points
-----------------------------------------------------
DROP TABLE IF EXISTS association_polygone_points CASCADE ;
CREATE TABLE projet_2A.association_polygone_points(
    id_polygone FOREIGN KEY REFERENCES polygones(id_polygone),
    id_point FOREIGN KEY REFERENCES points(id_point),
    ordre INT,
);
-----------------------------------------------------
-- contour
-----------------------------------------------------
DROP TABLE IF EXISTS contours CASCADE ;
CREATE TABLE projet_2A.contours(
    id_contour SERIAL PRIMARY KEY,
);
-----------------------------------------------------
-- association_polygone_points
-----------------------------------------------------
DROP TABLE IF EXISTS association_contours_polygones CASCADE ;
CREATE TABLE projet_2A.association_contours_polygones(
    id_contour FOREIGN KEY REFERENCES contour(id_contour),
    id_polygone FOREIGN KEY REFERENCES polygones(id_polygone),
    appartient BOOLEAN,
);
-----------------------------------------------------
-- association_lieu_contour
-----------------------------------------------------
DROP TABLE IF EXISTS association_lieu_contour CASCADE ;
CREATE TABLE projet_2A.association_lieu_contour(
    id_lieu FOREIGN KEY REFERENCES lieu(id_lieu),
    annee INT,
    id_contour FOREIGN KEY REFERENCES contour(id_contour),
    pop INT,
);
