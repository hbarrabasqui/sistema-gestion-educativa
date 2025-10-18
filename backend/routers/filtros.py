# routers/filtros.py
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from sqlalchemy import text

router = APIRouter(prefix="/filtros", tags=["filtros"])

@router.get("/ifts")
def get_ifts(db: Session = Depends(get_db)):
    query = text("SELECT id_instituto, nombre FROM INSTITUTOS ORDER BY nombre")
    result = db.execute(query)
    return [{"id": row[0], "nombre": row[1]} for row in result]

@router.get("/carreras")
def get_carreras(db: Session = Depends(get_db)):
    query = text("SELECT id_carrera, nombre FROM CARRERAS ORDER BY nombre")
    result = db.execute(query)
    return [{"id": row[0], "nombre": row[1]} for row in result]

@router.get("/materias")
def get_materias(db: Session = Depends(get_db)):
    query = text("SELECT id_materia, nombre FROM MATERIAS ORDER BY nombre")
    result = db.execute(query)
    return [{"id": row[0], "nombre": row[1]} for row in result]

@router.get("/estados-concursos")
def get_estados_concursos(db: Session = Depends(get_db)):
    query = text("SELECT DISTINCT estado FROM CONCURSO_DOCENTE WHERE estado IS NOT NULL")
    result = db.execute(query)
    return [{"estado": row[0]} for row in result]

@router.get("/modalidades")
def get_modalidades(db: Session = Depends(get_db)):
    query = text("SELECT DISTINCT modalidad FROM OFERTAS_ACADEMICAS WHERE modalidad IS NOT NULL")
    result = db.execute(query)
    return [{"modalidad": row[0]} for row in result]

@router.get("/turnos")
def get_turnos(db: Session = Depends(get_db)):
    query = text("SELECT DISTINCT turno FROM OFERTAS_ACADEMICAS WHERE turno IS NOT NULL")
    result = db.execute(query)
    return [{"turno": row[0]} for row in result]

@router.get("/roles")
def get_roles(db: Session = Depends(get_db)):
    query = text("SELECT DISTINCT rol FROM PERSONA WHERE rol IS NOT NULL")
    result = db.execute(query)
    return [{"rol": row[0]} for row in result]

@router.get("/supervisiones")
def get_supervisiones(db: Session = Depends(get_db)):
    query = text("SELECT id_supervision, nombre FROM SUPERVISION ORDER BY nombre")
    result = db.execute(query)
    return [{"id": row[0], "nombre": row[1]} for row in result]
