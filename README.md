# [Où suis-je ?]

## Overview

This project was made as part of the Informatic Project of the 2nd year at ENSAI.
Projet réalisé dans le cadre du projet informatique de 2A à l'ENSAI.

Provided as an API, it enables users to search for information on French cities,
departments or regions from their INSEE codes.\
It is also possible to find the name of the location in which is located a specific spot,
defined on its GPS coordinates.\
Finally, the API offers the download of a file containing information on the location
of several spots. These spots must be provided to the API in a csv file.


Se présentant sous la forme d'une API, il permet d'obtenir des informations sur
des villes, départements, régions de France à partir de leur code INSEE.\
Il est également possible de trouver le nom de l'emplacement dans lequel se trouve une coordonnée
GPS.\
Enfin, à partir d'un fichier contenant une liste de points GPS, l'API est en mesure d'envoyer un fichier
texte contenant des informations sur leur emplacement.

## Summary

- 🪧 [Overview](#overview)
- 📦 [Prerequisites](#prerequisites)
- 🚀 [Setup](#setup)
- 🛠️ [Usage](#usage)
- 🤝 [Contribution](#contribution)

## Prerequisites

The repository contains the following files : [README](./README.md), [.gitignore](./.gitignore.md), [requirements](./requirements.txt) and [LICENSE](./LICENSE).

The repository contains the following directories : [src](src), which contains the file [app](/src/app.py), [business_object](src/business_object/), [dao](src/dao/), [data](data), [service](/src/service/), [utils](src/utils/) and [test](src/tests/).

Another directory, [doc](doc), which includes the project's tracking, is available.


Le dépot contient les fichiers suivants: [README](./README.md), [.gitignore](./.gitignore.md), [requirements](./requirements.txt) et de [LICENSE](./LICENSE).

Le dépot est composé d'un dossier [src](src), qui comprend le fichier [app](/src/app.py) et les dossiers [business_object](src/business_object/), [dao](src/dao/), [data](data), [service](/src/service/), [utils](src/utils/) et [test](src/tests/).

Un autre dossier [doc](doc) qui regroupe le suivi du projet est disponible.

## Setup

It is necessary to have installed the following libraries : *fastapi*, *fiona*, *psycopg2_binary*, *pytest*, *python-dotenv* et *uvicorn*. 

It is possible to install them with the command :
```
pip install -r requirements.txt
```


Il est nécessaire d'avoir les librairies *fastapi*, *fiona*, *psycopg2_binary*, *pytest*, *python-dotenv* et *uvicorn*.

Il est possible de les installer grâce à la commande :
```
pip install -r requirements.txt
```

## Usage

Firstly, you need to be connected to the database. In order to do that, you need to create a *.env* file and fill in the gaps in the
following code :
```bash
POSTGRES_HOST=xxx
POSTGRES_PORT=xxx
POSTGRES_DATABASE=xxx
POSTGRES_USER=xxx
POSTGRES_PASSWORD=xxx
POSTGRES_SCHEMA=xxx
```

If the database does not exist, you must execute the files [reset_database](src/utils/reset_database.py) then [shp_formatter](src/utils/shp_formatter.py).

Finally, to run the API, you need to execute the [app](src/app.py) file.
It will then be possible to access it from a browser via the link : [localhost/docs](http://localhost/docs).

You must note that the last function of the API (allow the download of a file) only works when giving a csv file where a line contains the
coordinates of a point.


Dans un premier temps, il faut se connecter à la base de donnée. Pour cela, il faut créer un fichier *.env* et completer le code suivant:
```bash
POSTGRES_HOST=xxx
POSTGRES_PORT=xxx
POSTGRES_DATABASE=xxx
POSTGRES_USER=xxx
POSTGRES_PASSWORD=xxx
POSTGRES_SCHEMA=xxx
```

Si la base de donnée n'existe pas, il faut exécuter les fichiers [reset_database](src/utils/reset_database.py) puis [shp_formatter](src/utils/shp_formatter.py).


Enfin, pour lancer l'API, il suffit d'exécuter le fichier [app](src/app.py).
Il est alors possible d'y accéder depuis son navigateur via le lien [localhost/docs](http://localhost/docs).

Il est impotant de noter que l'API fonctionne lorsqu'on lui envoie un fichier
csv où une ligne contient les coordonnées d'un point.

## Notes

- To execute [shp_formatter](src/utils/shp_formatter.py), you need to specify the path to the required *shp* files.
The directory can be downloaded on [Admin-Express](https://geoservices.ign.fr/adminexpress).
- In order for the tests of [shp_formatter](src/utils/shp_formatter.py) to , you have to specify the path to a *shp* file.

- Pour exéctuer [shp_formatter](src/utils/shp_formatter.py), il faut renseigner
le chemin des fichiers *shp* voulus. Le dossier est téléchargeable depuis [Admin-Express](https://geoservices.ign.fr/adminexpress).
- De même, pour que les test de [shp_formatter](src/utils/shp_formatter.py)
fonctionnent, il faut y renseigner le chemin vers un fichier *shp*.

## Contribution

See the [CONTRIBUTING](./CONTRIBUTING.md) file in the repository

Voir le fichier [CONTRIBUTING](./CONTRIBUTING.md) du dépôt.
