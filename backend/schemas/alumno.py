# schemas/alumno.py
from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import date

class AlumnoBase(BaseModel):
    dni: str
    nombre: Optional[str]
    apellido: Optional[str]
    email: Optional[EmailStr]
    telefono: Optional[str]

class AlumnoCreate(AlumnoBase):
    pass

class AlumnoUpdate(BaseModel):
    nombre: Optional[str]
    apellido: Optional[str]
    email: Optional[EmailStr]
    telefono: Optional[str]

class AlumnoOut(AlumnoBase):
    class Config:
        orm_mode = True
