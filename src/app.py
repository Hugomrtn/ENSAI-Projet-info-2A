import logging

from fastapi import FastAPI, HTTPException # noqa

from utils.log_init import initialiser_logs # noqa

from service.service_utilisateur import Service_utilisateur

from business_object.point import Point

app = FastAPI(title="Où suis-je?")


# initialiser_logs("Webservice")

service_utilisateur = Service_utilisateur()


@app.get("/ousuisje/emplacement/{annee}/{code}", tags=["Emplacement"])
async def emplacement_selon_code_et_an(annee: int, code: int):
    """Trouver un emplacement à partir de son code et son année
    GET http://localhost/ousuisje/emplacement/2024/35238
    """
    logging.info("Trouver un emplacement à partir de son code et son année")
    res = service_utilisateur.\
        fonction1_obtenir_informations_selon_code_et_annee(code, annee)
    if not res:
        return "Emplacement non trouvé"
    return res


@app.get("/ousuisje/localiser-point/{annee}/{niveau}/{latitude}/{longitude}",
         tags=["Localiser"])
async def localiser_selon_point(annee: int, niveau: str, latitude, longitude):
    """Trouver un emplacement à partir de son code et son année
    GET http://localhost/ousuisje/localiser-point/2024/Ville/2.5/2.5
    """
    logging.info("Trouver un emplacement à partir de son code et son année")
    point = Point(float(latitude), float(longitude))
    res = service_utilisateur.\
        fonction2_obtenir_emplacement_selon_point_niveau_annee(niveau, annee,
                                                               point)
    if not res:
        return "Emplacement non trouvé"
    return res

# Run the FastAPI application
if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=80)

    logging.info("Arret du Webservice")
