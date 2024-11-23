# [Où suis-je ?]

## À propos

Projet réalisé dans le cadre du projet informatique de 2A à l'ENSAI.

Se présentant sous la forme d'une API, il permet d'obtenir des informations sur
des villes, départements, régions de France à partir de leur code INSEE.\
Il est également possible de trouver le nom de l'emplacement dans lequel se trouve une coordonnée
GPS.\
Enfin, à partir d'un fichier contenant une liste de points GPS, l'API est en mesure d'envoyer un fichier
texte contenant des informations sur leur emplacement.

## Table des matières

- 🪧 [À propos](#à-propos)
- 📦 [Prérequis](#prérequis)
- 🚀 [Installation](#installation)
- 🛠️ [Utilisation](#utilisation)
- 🤝 [Contribution](#contribution)

## Prérequis

Le dépot contient les fichiers suivants: [README](./README.md), [.gitignore](./.gitignore.md), [requirements](./requirements.txt) et de [LICENSE](./LICENSE).

Le dépot est composé d'un dossier [src](src), qui comprend le fichier [app](/src/app.py) et les dossiers [business_object](src/business_object/), [dao](src/dao/), [data](data), [service](/src/service/), [utils](src/utils/) et [test](src/tests/).

Un autre dossier [doc](doc) qui regroupe le suivi du projet est disponible.

## Installation

Il est nécessaire d'avoir les librairies *fastapi*, *fiona*, *psycopg2_binary*, *pytest*, *python-dotenv* et *uvicorn*.

Il est possible de les installer grâce à la commande :
```
pip install -r requirements.txt
```

## Utilisation

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

- Pour exéctuer [shp_formatter](src/utils/shp_formatter.py), il faut renseigner
le chemin des fichiers *shp* voulus. Le dossier est téléchargeable depuis [Admin-Express](https://geoservices.ign.fr/adminexpress).
- De même, pour que les test de [shp_formatter](src/utils/shp_formatter.py)
fonctionnent, il faut y renseigner le chemin vers un fichier *shp*.

## Contribution

Voir le fichier [CONTRIBUTING](./CONTRIBUTING.md) du dépôt.
