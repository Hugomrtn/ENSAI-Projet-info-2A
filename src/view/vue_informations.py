import regex

from InquirerPy import inquirer
from InquirerPy.validator import PasswordValidator, EmptyInputValidator

from prompt_toolkit.validation import ValidationError, Validator

from view.vue_abstraite import VueAbstraite


class Vue_informations(VueAbstraite):
    def choisir_menu(self):

        # PENSER À FAIRE UNE LISTE QUI PEUT CHANGER POUR LES NIVEAUX ET
        # POUR LES ANNEES

        # AJOUTER LES VALIDATIONS POUR LES INPUTS

        niveau = inquirer.List("niveau",
                               message="Choisissez un niveau :",
                               choices=["Département", "Ville"])

        annee = inquirer.List("année",
                              message="Choisissez une année :",
                              choices=["2024"])

        code = inquirer.number(
            message="Entrez le code du lieu : ",
        ).execute()

        informations = # appel au service qui peut déterminer les informations

        if informations:
            message = (""
            )
        else:
            message = "Le lieu n'a pas été trouvé."

        from view.vue_menu_principal import Vue_menu_principal

        return Vue_menu_principal(message)
