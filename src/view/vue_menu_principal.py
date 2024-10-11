from InquirerPy import inquirer

from vue_abstraite import VueAbstraite

from view.vue_informations import Vue_informations


class Vue_menu_principal(VueAbstraite):
    """Vue du menu du joueur

    Attributes
    ----------
    message=''
        str

    Returns
    ------
    view
        retourne la prochaine vue, celle qui est choisie par l'utilisateur
    """

    def choisir_menu(self):
        """Choix du menu suivant de l'utilisateur

        Return
        ------
        vue
            Retourne la vue choisie par l'utilisateur dans le terminal
        """

        print("\n" + "-" * 50 + "\nMenu\n" + "-" * 50 + "\n")

        choix = inquirer.select(
            message="Faites votre choix : ",
            choices=[
                "Demander des informations sur un lieu",
                "Trouver un lieu à partir de coordonnées",
                "Obtenir un fichier à partir d'une liste de coordonnées",
                "Quitter"
            ],
        ).execute()

        match choix:

            case "Demander des informations sur un lieu":
                return (Vue_informations().choisir_menu())

            case "Trouver un lieu à partir de coordonnées":
                pass

            case "Obtenir un fichier à partir d'une liste de coordonnées":
                pass

            case "Quitter":
                pass
