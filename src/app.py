import logging

from fastapi import FastAPI, UploadFile, HTTPException
from fastapi.responses import StreamingResponse
from io import StringIO

from service.service_utilisateur import Service_utilisateur

from business_object.point import Point

app = FastAPI(title="Où suis-je?")

service_utilisateur = Service_utilisateur()


@app.get("/ousuisje/emplacement/{annee}/{niveau}/{code}", tags=["Emplacement"])
async def emplacement_selon_code_et_an(annee: int, niveau: str, code: int):
    """Trouver un emplacement à partir de son code, son niveau et son année
    GET http://localhost/ousuisje/emplacement/2024/35238
    """
    logging.info("Trouver un emplacement à partir de son code et son année")
    res = service_utilisateur.\
        fonction1_obtenir_informations_selon_code_niveau_et_annee(code, niveau,
                                                                  annee)
    if not res:
        return "Emplacement non trouvé"
    return res


@app.get("/ousuisje/localiser-point/{annee}/{niveau}/{longitude}/{latitude}",
         tags=["Localiser"])
async def localiser_selon_point(annee: int, niveau: str, longitude, latitude):
    """Trouver un emplacement à partir de l'année, du niveau et des coordonnées
    GET http://localhost/ousuisje/localiser-point/2024/Ville/2.5/2.5
    """
    logging.info("Trouver un emplacement à partir de son code et son année")
    point = Point(float(longitude), float(latitude))
    res = service_utilisateur.\
        fonction2_obtenir_emplacement_selon_point_niveau_annee(niveau, annee,
                                                               point)
    if not res:
        return "Emplacement non trouvé"
    return res


@app.post("/ousuisje/localiser-liste-de-points/", tags=["Localiser"])
async def localiser_selon_liste_points(file: UploadFile, annee, niveau):
    """Trouver des emplacement à partir de l'année, du niveau et des
    coordonnées d'une liste de points à partir d'un fichier CSV
    POST /ousuisje/localiser-liste-de-points/
    """
    if not file.filename.endswith(".csv"):
        raise HTTPException(status_code=400,
                            detail="Only CSV files are supported.")

    try:
        content = await file.read()
        csv_content = StringIO(content.decode("utf-8"))

        liste_points = Point(0, 0).lire_fichier(csv_content)
        liste_resultats = Service_utilisateur().\
            fonction3_obtenir_multiples_emplacements_selons_liste_coordonnees(
                liste_points, niveau, annee)

        output = StringIO()
        for resultat in liste_resultats:
            output.write(resultat + "\n")
        output.seek(0)

        response = StreamingResponse(
            output,
            media_type="text/plain",
            headers={
                "Content-Disposition": f"attachment; filename=résultat_"
                f"{file.filename.replace('.csv', '.txt')}"}
        )

        return response

    except Exception as e:
        raise HTTPException(status_code=500,
                            detail=f"Error processing file: {e}")

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=80)

    logging.info("Arret du Webservice")
