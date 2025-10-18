# routers/carreras.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from pydantic import BaseModel
from typing import Optional, List

router = APIRouter(prefix="/carreras", tags=["carreras"])

class CarreraBase(BaseModel):
    nombre: str
    titulo: str
    duracion: int

class CarreraCreate(CarreraBase):
    pass

class CarreraUpdate(BaseModel):
    nombre: Optional[str] = None
    titulo: Optional[str] = None
    duracion: Optional[int] = None

class CarreraOut(CarreraBase):
    id_carrera: int
    class Config:
        orm_mode = True

@router.get("/", response_model=List[CarreraOut])
def listar_carreras(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    from models import Carrera
    return db.query(Carrera).offset(skip).limit(limit).all()

@router.get("/{id_carrera}", response_model=CarreraOut)
def obtener_carrera(id_carrera: int, db: Session = Depends(get_db)):
    from models import Carrera
    carrera = db.query(Carrera).filter(Carrera.id_carrera == id_carrera).first()
    if not carrera:
        raise HTTPException(status_code=404, detail="Carrera no encontrada")
    return carrera

@router.post("/", response_model=CarreraOut)
def crear_carrera(carrera: CarreraCreate, db: Session = Depends(get_db)):
    from models import Carrera
    nueva_carrera = Carrera(**carrera.dict())
    db.add(nueva_carrera)
    db.commit()
    db.refresh(nueva_carrera)
    return nueva_carrera

@router.put("/{id_carrera}", response_model=CarreraOut)
def actualizar_carrera(id_carrera: int, carrera_update: CarreraUpdate, db: Session = Depends(get_db)):
    from models import Carrera
    carrera = db.query(Carrera).filter(Carrera.id_carrera == id_carrera).first()
    if not carrera:
        raise HTTPException(status_code=404, detail="Carrera no encontrada")
    
    update_data = carrera_update.dict(exclude_unset=True)
    for field, value in update_data.items():
        setattr(carrera, field, value)
    
    db.commit()
    db.refresh(carrera)
    return carrera

@router.delete("/{id_carrera}")
def eliminar_carrera(id_carrera: int, db: Session = Depends(get_db)):
    from models import Carrera
    carrera = db.query(Carrera).filter(Carrera.id_carrera == id_carrera).first()
    if not carrera:
        raise HTTPException(status_code=404, detail="Carrera no encontrada")
    
    db.delete(carrera)
    db.commit()
    return {"message": "Carrera eliminada correctamente"}