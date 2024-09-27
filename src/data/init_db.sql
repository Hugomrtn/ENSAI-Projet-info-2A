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
    id_emplacement SERIAL PRIMARY KEY,
    nom_emplacement TEXT;
    niveau TEXT;
    pop INT;
);
-----------------------------------------------------
-- points
-----------------------------------------------------
DROP TABLE IF EXISTS points CASCADE ;
CREATE TABLE points(
    id_point SERIAL PRIMARY KEY,
    long FLOAT;
    lat FLOAT;
);
-----------------------------------------------------
-- points
-----------------------------------------------------
DROP TABLE IF EXISTS relations CASCADE ;
CREATE TABLE relations(
    id_point SERIAL PRIMARY KEY,
    long FLOAT;
    lat FLOAT;
);
