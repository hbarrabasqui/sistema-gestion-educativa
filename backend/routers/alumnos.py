
# routers/alumnos.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from models import Persona
from schemas.alumno import AlumnoCreate, AlumnoOut, AlumnoUpdate
from typing import List

router = APIRouter(prefix="/alumnos", tags=["alumnos"])

@router.get("/", response_model=List[AlumnoOut])
def listar_alumnos(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    results = db.query(Persona).filter(Persona.rol == "alumno").offset(skip).limit(limit).all()
    return results

@router.get("/{dni}", response_model=AlumnoOut)
def obtener_alumno(dni: str, db: Session = Depends(get_db)):
    alumno = db.query(Persona).filter(Persona.dni == dni).first()
    if not alumno:
        raise HTTPException(status_code=404, detail="Alumno no encontrado")
    return alumno

@router.post("/", response_model=AlumnoOut)
def crear_alumno(payload: AlumnoCreate, db: Session = Depends(get_db)):
    # si ya existe el dni, error
    if db.query(Persona).filter(Persona.dni == payload.dni).first():
        raise HTTPException(status_code=400, detail="Alumno ya existe")
    obj = Persona(
        dni=payload.dni,
        nombre=payload.nombre,
        apellido=payload.apellido,
        email=payload.email,
        telefono=payload.telefono,
        rol="alumno"
    )
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj

@router.put("/{dni}", response_model=AlumnoOut)
def actualizar_alumno(dni: str, payload: AlumnoUpdate, db: Session = Depends(get_db)):
    alumno = db.query(Persona).filter(Persona.dni == dni).first()
    if not alumno:
        raise HTTPException(status_code=404, detail="Alumno no encontrado")
    for field, value in payload.dict(exclude_unset=True).items():
        setattr(alumno, field, value)
    db.commit()
    db.refresh(alumno)
    return alumno

@router.delete("/{dni}")
def eliminar_alumno(dni: str, db: Session = Depends(get_db)):
    alumno = db.query(Persona).filter(Persona.dni == dni).first()
    if not alumno:
        raise HTTPException(status_code=404, detail="Alumno no encontrado")
    db.delete(alumno)
    db.commit()
    return {"detail": "Alumno eliminado"}
