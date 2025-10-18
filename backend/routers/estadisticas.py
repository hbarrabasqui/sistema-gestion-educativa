# routers/estadisticas.py
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from sqlalchemy import text

router = APIRouter(prefix="/estadisticas", tags=["estadisticas"])

# CONCURSOS
@router.get("/concursos/por-estado")
def get_concursos_por_estado(db: Session = Depends(get_db)):
    query = text("""
        SELECT estado, COUNT(*) as cantidad 
        FROM CONCURSO_DOCENTE 
        WHERE estado IS NOT NULL
        GROUP BY estado
    """)
    result = db.execute(query)
    return [{"estado": row[0], "cantidad": row[1]} for row in result]

@router.get("/concursos/postulantes-ifts")
def get_concursos_por_ifts(db: Session = Depends(get_db)):
    query = text("""
        SELECT i.nombre as ifts, COUNT(*) as concursos
        FROM CONCURSO_DOCENTE cd
        JOIN INSTITUTOS i ON cd.id_instituto = i.id_instituto
        GROUP BY i.nombre
        ORDER BY concursos DESC
    """)
    result = db.execute(query)
    return [{"ifts": row[0], "postulantes": row[1]} for row in result]

# ALUMNOS
@router.get("/alumnos/por-carrera")
def get_alumnos_por_carrera(db: Session = Depends(get_db)):
    query = text("""
        SELECT c.nombre as carrera, COUNT(*) as cantidad
        FROM MATRICULAS m
        JOIN OFERTAS_ACADEMICAS oa ON m.id_oferta = oa.id_oferta
        JOIN CARRERAS c ON oa.id_carrera = c.id_carrera
        WHERE m.estado = 'Activa'
        GROUP BY c.nombre
    """)
    result = db.execute(query)
    return [{"carrera": row[0], "cantidad": row[1]} for row in result]

@router.get("/alumnos/por-instituto")
def get_alumnos_por_instituto(db: Session = Depends(get_db)):
    query = text("""
        SELECT i.nombre as instituto, COUNT(*) as cantidad
        FROM MATRICULAS m
        JOIN OFERTAS_ACADEMICAS oa ON m.id_oferta = oa.id_oferta
        JOIN INSTITUTOS i ON oa.id_instituto = i.id_instituto
        WHERE m.estado = 'Activa'
        GROUP BY i.nombre
    """)
    result = db.execute(query)
    return [{"instituto": row[0], "cantidad": row[1]} for row in result]

# DOCENTES
@router.get("/docentes/por-ifts")
def get_docentes_por_ifts(db: Session = Depends(get_db)):
    query = text("""
        SELECT i.nombre as ifts, COUNT(DISTINCT dm.dni) as docentes
        FROM DOCENTES_MATERIAS dm
        JOIN OFERTAS_ACADEMICAS oa ON dm.id_oferta = oa.id_oferta
        JOIN INSTITUTOS i ON oa.id_instituto = i.id_instituto
        WHERE dm.fecha_hasta IS NULL OR dm.fecha_hasta > date('now')
        GROUP BY i.nombre
    """)
    result = db.execute(query)
    return [{"ifts": row[0], "docentes": row[1]} for row in result]

@router.get("/docentes/por-materia")
def get_docentes_por_materia(db: Session = Depends(get_db)):
    query = text("""
        SELECT m.nombre as materia, COUNT(DISTINCT dm.dni) as docentes
        FROM DOCENTES_MATERIAS dm
        JOIN MATERIAS m ON dm.id_materia = m.id_materia
        WHERE dm.fecha_hasta IS NULL OR dm.fecha_hasta > date('now')
        GROUP BY m.nombre
        ORDER BY docentes DESC
        LIMIT 10
    """)
    result = db.execute(query)
    return [{"materia": row[0], "docentes": row[1]} for row in result]

# OFERTAS ACADÉMICAS
@router.get("/ofertas/por-modalidad")
def get_ofertas_por_modalidad(db: Session = Depends(get_db)):
    query = text("""
        SELECT modalidad, COUNT(*) as cantidad
        FROM OFERTAS_ACADEMICAS
        WHERE modalidad IS NOT NULL
        GROUP BY modalidad
    """)
    result = db.execute(query)
    return [{"modalidad": row[0], "cantidad": row[1]} for row in result]

@router.get("/ofertas/por-turno")
def get_ofertas_por_turno(db: Session = Depends(get_db)):
    query = text("""
        SELECT turno, COUNT(*) as cantidad
        FROM OFERTAS_ACADEMICAS
        WHERE turno IS NOT NULL
        GROUP BY turno
    """)
    result = db.execute(query)
    return [{"turno": row[0], "cantidad": row[1]} for row in result]