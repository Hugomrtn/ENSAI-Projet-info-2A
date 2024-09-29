--------------------------------------------------------------
-- Création du schéma projet_2A
--------------------------------------------------------------
DROP SCHEMA IF EXISTS projet_2A CASCADE;
CREATE SCHEMA projet_2A;
-----------------------------------------------------
-- lieu
-----------------------------------------------------
DROP TABLE IF EXISTS lieu CASCADE ;
CREATE TABLE projet_2A.emplacements(
    id_emplacement UNIQUE INT, -- on utilisera le code insee
    nom_emplacement TEXT;
    niveau TEXT;
    pop INT;
    annee INT;
);
-----------------------------------------------------
-- points
-----------------------------------------------------
DROP TABLE IF EXISTS points CASCADE ;
CREATE TABLE projet_2A.points(
    id_point SERIAL PRIMARY KEY,
    long FLOAT;
    lat FLOAT;
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
    ordre INT
);
-----------------------------------------------------
-- delimitations
-----------------------------------------------------
DROP TABLE IF EXISTS delimitations CASCADE ;
CREATE TABLE projet_2A.delimitations(
);
-----------------------------------------------------
-- relations
-----------------------------------------------------
DROP TABLE IF EXISTS relations CASCADE ;
CREATE TABLE projet_2A.relations(
);
