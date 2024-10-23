--------------------------------------------------------------
-- Création du schéma projet_2A
--------------------------------------------------------------
DROP SCHEMA IF EXISTS projet_2A CASCADE;
CREATE SCHEMA projet_2A;

-----------------------------------------------------
-- emplacement
-----------------------------------------------------
DROP TABLE IF EXISTS projet_2A.emplacement CASCADE;
CREATE TABLE projet_2A.emplacement(
    id_emplacement SERIAL PRIMARY KEY,
    nom_emplacement TEXT,
    niveau TEXT,
    code INT
);

-----------------------------------------------------
-- points
-----------------------------------------------------
DROP TABLE IF EXISTS projet_2A.points CASCADE;
CREATE TABLE projet_2A.points(
    id_point SERIAL PRIMARY KEY,
    x FLOAT,
    y FLOAT
);

-----------------------------------------------------
-- polygones
-----------------------------------------------------
DROP TABLE IF EXISTS projet_2A.polygone CASCADE;
CREATE TABLE projet_2A.polygone(
    id_polygone SERIAL PRIMARY KEY
);

-----------------------------------------------------
-- association_polygone_points
-----------------------------------------------------
DROP TABLE IF EXISTS projet_2A.association_polygone_points CASCADE;
CREATE TABLE projet_2A.association_polygone_points(
    id_polygone INT REFERENCES projet_2A.polygone(id_polygone),
    id_point INT REFERENCES projet_2A.points(id_point),
    ordre INT
);

-----------------------------------------------------
-- contour
-----------------------------------------------------
DROP TABLE IF EXISTS projet_2A.contour CASCADE;
CREATE TABLE projet_2A.contour(
    id_contour SERIAL PRIMARY KEY
);

-----------------------------------------------------
-- association_contours_polygones
-----------------------------------------------------
DROP TABLE IF EXISTS projet_2A.association_contours_polygones CASCADE;
CREATE TABLE projet_2A.association_contours_polygones(
    id_contour INT REFERENCES projet_2A.contour(id_contour),
    id_polygone INT REFERENCES projet_2A.polygone(id_polygone),
    appartient BOOLEAN
);

-----------------------------------------------------
-- association_emplacement_contour
-----------------------------------------------------
DROP TABLE IF EXISTS projet_2A.association_emplacement_contour CASCADE;
CREATE TABLE projet_2A.association_emplacement_contour(
    id_emplacement INT REFERENCES projet_2A.emplacement(id_emplacement),
    annee INT,
    id_contour INT REFERENCES projet_2A.contour(id_contour),
    nombre_habitants INT
);
