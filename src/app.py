from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from service.emplacement_service import EmplacementService
from service.contour_service import ContourService
from service.polygone_service import PolygoneService
from service.point_service import PointService
from business_object.point import Point

from utils.log_init import initialiser_logs

app = FastAPI(title="Mon webservice")

initialiser_logs("Webservice")

emplacement_service = EmplacementService()
contour_service = ContourService()
polygone_service = PolygoneService()
point_service = PointService()

### Emplacement Endpoints


class EmplacementModel(BaseModel):
    niveau: str
    nom: str
    code: int
    pop: int
    annee: int


@app.get("/emplacement/", tags=["Emplacements"])
async def lister_tous_emplacements():
    liste_emplacements = emplacement_service.lister_tous()
    return liste_emplacements


@app.get("/emplacement/{id_emplacement}", tags=["Emplacements"])
async def emplacement_par_id(id_emplacement: int):
    emplacement = emplacement_service.trouver_par_id(id_emplacement)
    if not emplacement:
        raise HTTPException(status_code=404, detail="Emplacement non trouvé")
    return emplacement


@app.post("/emplacement/", tags=["Emplacements"])
async def creer_emplacement(e: EmplacementModel):
    emplacement = emplacement_service.creer(e.niveau, e.nom, e.code, e.pop, e.annee)
    if not emplacement:
        raise HTTPException(
            status_code=404, detail="Erreur lors de la création de l'emplacement"
        )
    return emplacement


@app.put("/emplacement/{id_emplacement}", tags=["Emplacements"])
async def modifier_emplacement(id_emplacement: int, e: EmplacementModel):
    emplacement = emplacement_service.trouver_par_id(id_emplacement)
    if not emplacement:
        raise HTTPException(status_code=404, detail="Emplacement non trouvé")
    emplacement.niveau = e.niveau
    emplacement.nom = e.nom
    emplacement.code = e.code
    emplacement.pop = e.pop
    emplacement.annee = e.annee
    emplacement = emplacement_service.modifier(emplacement)
    if not emplacement:
        raise HTTPException(
            status_code=404, detail="Erreur lors de la modification de l'emplacement"
        )
    return f"Emplacement {emplacement.nom} modifié"


@app.delete("/emplacement/{id_emplacement}", tags=["Emplacements"])
async def supprimer_emplacement(id_emplacement: int):
    emplacement = emplacement_service.trouver_par_id(id_emplacement)
    if not emplacement:
        raise HTTPException(status_code=404, detail="Emplacement non trouvé")
    emplacement_service.supprimer(id_emplacement)
    return f"Emplacement {id_emplacement} supprimé"


### Contour Endpoints


class ContourModel(BaseModel):
    polygones_composants: list[int]
    polygones_enclaves: list[int]


@app.get("/contour/", tags=["Contours"])
async def lister_tous_contours():
    liste_contours = contour_service.lister_tous()
    return liste_contours


@app.get("/contour/{id_contour}", tags=["Contours"])
async def contour_par_id(id_contour: int):
    contour = contour_service.trouver_par_id(id_contour)
    if not contour:
        raise HTTPException(status_code=404, detail="Contour non trouvé")
    return contour


@app.post("/contour/", tags=["Contours"])
async def creer_contour(c: ContourModel):
    polygones_composants = [
        polygone_service.trouver_par_id(pid) for pid in c.polygones_composants
    ]
    polygones_enclaves = [
        polygone_service.trouver_par_id(pid) for pid in c.polygones_enclaves
    ]
    contour = contour_service.creer(polygones_composants, polygones_enclaves)
    if not contour:
        raise HTTPException(
            status_code=404, detail="Erreur lors de la création du contour"
        )
    return contour


@app.put("/contour/{id_contour}", tags=["Contours"])
async def modifier_contour(id_contour: int, c: ContourModel):
    contour = contour_service.trouver_par_id(id_contour)
    if not contour:
        raise HTTPException(status_code=404, detail="Contour non trouvé")
    polygones_composants = [
        polygone_service.trouver_par_id(pid) for pid in c.polygones_composants
    ]
    polygones_enclaves = [
        polygone_service.trouver_par_id(pid) for pid in c.polygones_enclaves
    ]
    contour.polygones_composants = polygones_composants
    contour.polygones_enclaves = polygones_enclaves
    contour = contour_service.modifier(contour)
    if not contour:
        raise HTTPException(
            status_code=404, detail="Erreur lors de la modification du contour"
        )
    return f"Contour {id_contour} modifié"


@app.delete("/contour/{id_contour}", tags=["Contours"])
async def supprimer_contour(id_contour: int):
    contour = contour_service.trouver_par_id(id_contour)
    if not contour:
        raise HTTPException(status_code=404, detail="Contour non trouvé")
    contour_service.supprimer(id_contour)
    return f"Contour {id_contour} supprimé"


### Polygone Endpoints


class PolygoneModel(BaseModel):
    liste_points: list[list[float]]


@app.get("/polygone/", tags=["Polygones"])
async def lister_tous_polygones():
    liste_polygones = polygone_service.lister_tous()
    return liste_polygones


@app.get("/polygone/{id_polygone}", tags=["Polygones"])
async def polygone_par_id(id_polygone: int):
    polygone = polygone_service.trouver_par_id(id_polygone)
    if not polygone:
        raise HTTPException(status_code=404, detail="Polygone non trouvé")
    return polygone


@app.post("/polygone/", tags=["Polygones"])
async def creer_polygone(p: PolygoneModel):
    points = [Point(x=x, y=y) for x, y in p.liste_points]
    polygone = polygone_service.creer(points)
    if not polygone:
        raise HTTPException(
            status_code=404, detail="Erreur lors de la création du polygone"
        )
    return polygone


@app.put("/polygone/{id_polygone}", tags=["Polygones"])
async def modifier_polygone(id_polygone: int, p: PolygoneModel):
    polygone = polygone_service.trouver_par_id(id_polygone)
    if not polygone:
        raise HTTPException(status_code=404, detail="Polygone non trouvé")
    points = [Point(x=x, y=y) for x, y in p.liste_points]
    polygone.liste_points = points
    polygone = polygone_service.modifier(polygone)
    if not polygone:
        raise HTTPException(
            status_code=404, detail="Erreur lors de la modification du polygone"
        )
    return f"Polygone {id_polygone} modifié"


@app.delete("/polygone/{id_polygone}", tags=["Polygones"])
async def supprimer_polygone(id_polygone: int):
    polygone = polygone_service.trouver_par_id(id_polygone)
    if not polygone:
        raise HTTPException(status_code=404, detail="Polygone non trouvé")
    polygone_service.supprimer(id_polygone)
    return f"Polygone {id_polygone} supprimé"


### Point Endpoints


class PointModel(BaseModel):
    x: float
    y: float


@app.get("/point/", tags=["Points"])
async def lister_tous_points():
    liste_points = point_service.lister_tous()
    return liste_points


@app.get("/point/{id_point}", tags=["Points"])
async def point_par_id(id_point: int):
    point = point_service.trouver_par_id(id_point)
    if not point:
        raise HTTPException(status_code=404, detail="Point non trouvé")
    return point


@app.post("/point/", tags=["Points"])
async def creer_point(p: PointModel):
    point = point_service.creer(p.x, p.y)
    if not point:
        raise HTTPException(
            status_code=404, detail="Erreur lors de la création du point"
        )
    return point


@app.put("/point/{id_point}", tags=["Points"])
async def modifier_point(id_point: int, p: PointModel):
    point = point_service.trouver_par_id(id_point)
    if not point:
        raise HTTPException(status_code=404, detail="Point non trouvé")
    point.x = p.x
    point.y = p.y
    point = point_service.modifier(point)
    if not point:
        raise HTTPException(
            status_code=404, detail="Erreur lors de la modification du point"
        )
    return f"Point {id_point} modifié"


@app.delete("/point/{id_point}", tags=["Points"])
async def supprimer_point(id_point: int):
    point = point_service.trouver_par_id(id_point)
    if not point:
        raise HTTPException(status_code=404, detail="Point non trouvé")
    point_service.supprimer(id_point)
    return f"Point {id_point} supprimé"


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=80)
