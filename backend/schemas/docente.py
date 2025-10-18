# schemas/docente.py
from pydantic import BaseModel, EmailStr
from typing import Optional

class DocenteBase(BaseModel):
    dni: str
    nombre: Optional[str]
    apellido: Optional[str]
    email: Optional[EmailStr]
    telefono: Optional[str]

class DocenteCreate(DocenteBase):
    pass

class DocenteUpdate(BaseModel):
    nombre: Optional[str]
    apellido: Optional[str]
    email: Optional[EmailStr]
    telefono: Optional[str]

class DocenteOut(DocenteBase):
    class Config:
        orm_mode = True
