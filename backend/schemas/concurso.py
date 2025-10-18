# schemas/concurso.py
from pydantic import BaseModel
from typing import Optional

class ConcursoBase(BaseModel):
    codigo: Optional[str]
    id_oferta: Optional[int]
    fecha_apertura: Optional[str]
    fecha_cierre: Optional[str]
    estado: Optional[str]

class ConcursoCreate(ConcursoBase):
    pass

class ConcursoUpdate(ConcursoBase):
    pass

class ConcursoOut(ConcursoBase):
    id_concurso: int
    class Config:
        orm_mode = True
