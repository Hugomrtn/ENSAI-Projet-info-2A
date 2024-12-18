import sys
import os
import logging
import dotenv

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from utils.singleton import Singleton # noqa
from dao.db_connection import DBConnection # noqa


class ResetDatabase(metaclass=Singleton):
    """

    Reinitialisation de la base de données

    """

    def lancer(self):
        """

        Lancement de la réinitialisation des données

        """

        dotenv.load_dotenv()

        init_db = open("src/data/init_db.sql", encoding="utf-8")
        init_db_as_string = init_db.read()
        init_db.close()

        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(init_db_as_string)
        except Exception as e:
            logging.info(e)
            raise

        return True


if __name__ == "__main__":
    ResetDatabase().lancer()
