# routers/concursos.py

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from models import ConcursoDocente as Concurso
from typing import List

router = APIRouter(prefix="/concursos", tags=["concursos"])

# ENDPOINT 1: Listar todos los concursos (ya existía)
@router.get("/")
def listar_concursos(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return db.query(Concurso).offset(skip).limit(limit).all()

# ENDPOINT 2: Obtener concurso por ID (ya existía)
@router.get("/{id_concurso}")
def obtener_concurso(id_concurso: int, db: Session = Depends(get_db)):
    c = db.query(Concurso).filter(Concurso.id_concurso == id_concurso).first()
    if not c:
        raise HTTPException(status_code=404, detail="Concurso no encontrado")
    return c

# 🎯 ENDPOINT NUEVO 1: Estadísticas para gráficos
@router.get("/estadisticas/graficos")
def get_estadisticas_graficos():
    """
    Endpoint para alimentar los gráficos del frontend
    Devuelve datos mock (luego conectaremos con la BD real)
    """
    return {
        "por_estado": [
            {"estado": "Abierto", "cantidad": 8},
            {"estado": "En Evaluación", "cantidad": 3},
            {"estado": "Cerrado", "cantidad": 15},
            {"estado": "Finalizado", "cantidad": 12}
        ],
        "postulantes_ifts": [
            {"ifts": "IFTS 16", "postulantes": 45},
            {"ifts": "IFTS 18", "postulantes": 62},
            {"ifts": "IFTS 22", "postulantes": 28},
            {"ifts": "IFTS 25", "postulantes": 51},
            {"ifts": "IFTS 28", "postulantes": 19}
        ]
    }

# 🎯 ENDPOINT NUEVO 2: Estadísticas con filtros
@router.get("/estadisticas/filtradas")
def get_estadisticas_filtradas(ifts: str = None, estado: str = None, anio: str = None):
    """
    Endpoint que acepta filtros desde el frontend
    Por ahora simula filtrado, luego conectaremos con BD
    """
    # Datos base (mock)
    datos_base = {
        "por_estado": [
            {"estado": "Abierto", "cantidad": 8},
            {"estado": "En Evaluación", "cantidad": 3},
            {"estado": "Cerrado", "cantidad": 15},
            {"estado": "Finalizado", "cantidad": 12}
        ],
        "postulantes_ifts": [
            {"ifts": "IFTS 16", "postulantes": 45},
            {"ifts": "IFTS 18", "postulantes": 62},
            {"ifts": "IFTS 22", "postulantes": 28},
            {"ifts": "IFTS 25", "postulantes": 51},
            {"ifts": "IFTS 28", "postulantes": 19}
        ]
    }
    
    # Simular filtrado (luego será con BD real)
    datos_filtrados = {"por_estado": [], "postulantes_ifts": []}
    
    # Filtrar por estado
    if estado:
        datos_filtrados["por_estado"] = [item for item in datos_base["por_estado"] if item["estado"] == estado]
    else:
        datos_filtrados["por_estado"] = datos_base["por_estado"]
    
    # Filtrar por IFTS
    if ifts:
        datos_filtrados["postulantes_ifts"] = [item for item in datos_base["postulantes_ifts"] if item["ifts"] == ifts]
    else:
        datos_filtrados["postulantes_ifts"] = datos_base["postulantes_ifts"]
    
    return datos_filtrados
