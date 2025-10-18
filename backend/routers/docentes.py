# routers/docentes.py

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from models import Persona
from typing import List
from pydantic import BaseModel

router = APIRouter(prefix="/docentes", tags=["docentes"])

# Modelo para crear docente
class DocenteCreate(BaseModel):
    dni: str
    nombre: str
    apellido: str

# 1. LISTAR todos los docentes
@router.get("/")
def listar_docentes(db: Session = Depends(get_db)):
    docentes = db.query(Persona).filter(Persona.rol == "docente").all()
    return {"total": len(docentes), "docentes": docentes}

# 2. CREAR docente - CON JSON
@router.post("/crear")
def crear_docente(docente: DocenteCreate, db: Session = Depends(get_db)):
    try:
        # Verificar si ya existe
        if db.query(Persona).filter(Persona.dni == docente.dni).first():
            return {"error": "Ya existe una persona con este DNI"}
        
        nuevo_docente = Persona(
            dni=docente.dni,
            nombre=docente.nombre,
            apellido=docente.apellido,
            rol="docente"
        )
        
        db.add(nuevo_docente)
        db.commit()
        db.refresh(nuevo_docente)
        
        return {
            "mensaje": "✅ Docente creado exitosamente", 
            "docente": {
                "dni": nuevo_docente.dni,
                "nombre": nuevo_docente.nombre, 
                "apellido": nuevo_docente.apellido,
                "rol": nuevo_docente.rol
            }
        }
    except Exception as e:
        db.rollback()
        return {"error": f"Error al crear docente: {str(e)}"}

# 3. ELIMINAR docente
@router.delete("/{dni}")
def eliminar_docente(dni: str, db: Session = Depends(get_db)):
    try:
        docente = db.query(Persona).filter(Persona.dni == dni, Persona.rol == "docente").first()
        if not docente:
            return {"error": "Docente no encontrado"}
        
        db.delete(docente)
        db.commit()
        return {"mensaje": "✅ Docente eliminado correctamente"}
    except Exception as e:
        db.rollback()
        return {"error": f"Error al eliminar docente: {str(e)}"}
