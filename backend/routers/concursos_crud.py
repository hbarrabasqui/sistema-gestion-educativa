# routers/concursos_crud.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from pydantic import BaseModel
from typing import Optional, List
from datetime import date

router = APIRouter(prefix="/concursos", tags=["concursos-crud"])

class ConcursoBase(BaseModel):
    id_instituto: int
    materia: str
    fecha_apertura: date
    fecha_cierre: date
    estado: str

class ConcursoCreate(ConcursoBase):
    pass

class ConcursoUpdate(BaseModel):
    materia: Optional[str] = None
    fecha_apertura: Optional[date] = None
    fecha_cierre: Optional[date] = None
    estado: Optional[str] = None

class ConcursoOut(ConcursoBase):
    id_concurso: int
    class Config:
        orm_mode = True

@router.get("/", response_model=List[ConcursoOut])
def listar_concursos(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    from models import ConcursoDocente
    return db.query(ConcursoDocente).offset(skip).limit(limit).all()

@router.get("/{id_concurso}", response_model=ConcursoOut)
def obtener_concurso(id_concurso: int, db: Session = Depends(get_db)):
    from models import ConcursoDocente
    concurso = db.query(ConcursoDocente).filter(ConcursoDocente.id_concurso == id_concurso).first()
    if not concurso:
        raise HTTPException(status_code=404, detail="Concurso no encontrado")
    return concurso

@router.post("/", response_model=ConcursoOut)
def crear_concurso(concurso: ConcursoCreate, db: Session = Depends(get_db)):
    from models import ConcursoDocente
    nuevo_concurso = ConcursoDocente(**concurso.dict())
    db.add(nuevo_concurso)
    db.commit()
    db.refresh(nuevo_concurso)
    return nuevo_concurso

@router.put("/{id_concurso}", response_model=ConcursoOut)
def actualizar_concurso(id_concurso: int, concurso_update: ConcursoUpdate, db: Session = Depends(get_db)):
    from models import ConcursoDocente
    concurso = db.query(ConcursoDocente).filter(ConcursoDocente.id_concurso == id_concurso).first()
    if not concurso:
        raise HTTPException(status_code=404, detail="Concurso no encontrado")
    
    update_data = concurso_update.dict(exclude_unset=True)
    for field, value in update_data.items():
        setattr(concurso, field, value)
    
    db.commit()
    db.refresh(concurso)
    return concurso

@router.delete("/{id_concurso}")
def eliminar_concurso(id_concurso: int, db: Session = Depends(get_db)):
    from models import ConcursoDocente
    concurso = db.query(ConcursoDocente).filter(ConcursoDocente.id_concurso == id_concurso).first()
    if not concurso:
        raise HTTPException(status_code=404, detail="Concurso no encontrado")
    
    db.delete(concurso)
    db.commit()
    return {"message": "Concurso eliminado correctamente"}