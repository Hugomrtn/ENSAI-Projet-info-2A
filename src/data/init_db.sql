--------------------------------------------------------------
-- Création du schéma projet_2A
--------------------------------------------------------------
DROP SCHEMA IF EXISTS projet_2A CASCADE;
CREATE SCHEMA projet_2A;
-----------------------------------------------------
-- emplacement
-----------------------------------------------------
DROP TABLE IF EXISTS emplacement CASCADE ;
CREATE TABLE projet_2A.emplacement(
    id_emplacement SERIAL PRIMARY KEY
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
    x FLOAT,
    y FLOAT,
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
-- association_emplacement_contour
-----------------------------------------------------
DROP TABLE IF EXISTS association_emplacement_contour CASCADE ;
CREATE TABLE projet_2A.association_emplacement_contour(
    id_emplacement FOREIGN KEY REFERENCES emplacement(id_emplacement),
    annee INT,
    id_contour FOREIGN KEY REFERENCES contour(id_contour),
    pop INT,
);
