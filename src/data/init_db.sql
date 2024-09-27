--------------------------------------------------------------
-- Création du schéma projet_2A
--------------------------------------------------------------
DROP SCHEMA IF EXISTS projet_2A CASCADE;
CREATE SCHEMA projet_2A;
-----------------------------------------------------
-- lieu
-----------------------------------------------------
DROP TABLE IF EXISTS lieu CASCADE ;
CREATE TABLE projet_2A.emplacement(
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
    annee INT;
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
