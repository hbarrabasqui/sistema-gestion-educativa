# routers/personas.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from pydantic import BaseModel, EmailStr
from typing import Optional, List
from datetime import date

router = APIRouter(prefix="/personas", tags=["personas"])

class PersonaBase(BaseModel):
    dni: str
    nombre: str
    apellido: str
    cuil: Optional[str] = None
    rol: str
    telefono: Optional[str] = None
    email: Optional[EmailStr] = None
    fecha_nacimiento: Optional[date] = None

class PersonaCreate(PersonaBase):
    pass

class PersonaUpdate(BaseModel):
    nombre: Optional[str] = None
    apellido: Optional[str] = None
    telefono: Optional[str] = None
    email: Optional[EmailStr] = None
    fecha_nacimiento: Optional[date] = None

class PersonaOut(PersonaBase):
    class Config:
        orm_mode = True

@router.get("/", response_model=List[PersonaOut])
def listar_personas(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    from models import Persona
    return db.query(Persona).offset(skip).limit(limit).all()

@router.get("/{dni}", response_model=PersonaOut)
def obtener_persona(dni: str, db: Session = Depends(get_db)):
    from models import Persona
    persona = db.query(Persona).filter(Persona.dni == dni).first()
    if not persona:
        raise HTTPException(status_code=404, detail="Persona no encontrada")
    return persona

@router.post("/", response_model=PersonaOut)
def crear_persona(persona: PersonaCreate, db: Session = Depends(get_db)):
    from models import Persona
    print(f"🎯 RECIBIDO: {persona.dict()}")  # ← AGREGAR ESTO
    
    if db.query(Persona).filter(Persona.dni == persona.dni).first():
        print("❌ DNI ya existe")  # ← AGREGAR ESTO
        raise HTTPException(status_code=400, detail="Persona ya existe")
    
    try:
        nueva_persona = Persona(**persona.dict())
        db.add(nueva_persona)
        db.commit()
        db.refresh(nueva_persona)
        print(f"✅ GUARDADO: {nueva_persona.dni}")  # ← AGREGAR ESTO
        return nueva_persona
    except Exception as e:
        print(f"💥 ERROR: {e}")  # ← AGREGAR ESTO
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")

@router.put("/{dni}", response_model=PersonaOut)
def actualizar_persona(dni: str, persona_update: PersonaUpdate, db: Session = Depends(get_db)):
    from models import Persona
    persona = db.query(Persona).filter(Persona.dni == dni).first()
    if not persona:
        raise HTTPException(status_code=404, detail="Persona no encontrada")
    
    update_data = persona_update.dict(exclude_unset=True)
    for field, value in update_data.items():
        setattr(persona, field, value)
    
    db.commit()
    db.refresh(persona)
    return persona

@router.delete("/{dni}")
def eliminar_persona(dni: str, db: Session = Depends(get_db)):
    from models import Persona
    persona = db.query(Persona).filter(Persona.dni == dni).first()
    if not persona:
        raise HTTPException(status_code=404, detail="Persona no encontrada")
    
    db.delete(persona)
    db.commit()
    return {"message": "Persona eliminada correctamente"}