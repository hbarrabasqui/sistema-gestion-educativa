# models.py
from sqlalchemy import Column, Integer, String, Date, Boolean, ForeignKey, Text, DECIMAL, TIMESTAMP
from sqlalchemy.orm import relationship
from database import Base

class Persona(Base):
    __tablename__ = "PERSONA"
    dni = Column(String, primary_key=True, index=True)
    nombre = Column(String)
    apellido = Column(String)
    cuil = Column(String, nullable=True)
    rol = Column(String)
    telefono = Column(String, nullable=True)
    email = Column(String, nullable=True)
    fecha_nacimiento = Column(Date, nullable=True)

class Supervision(Base):
    __tablename__ = "SUPERVISION"
    id_supervision = Column(Integer, primary_key=True, index=True)
    nombre = Column(String)
    jurisdiccion = Column(String)
    responsable = Column(String)

class Instituto(Base):
    __tablename__ = "INSTITUTOS"
    id_instituto = Column(Integer, primary_key=True, index=True)
    nombre = Column(String)
    direccion = Column(String)
    cue = Column(String)
    id_supervision = Column(Integer, ForeignKey("SUPERVISION.id_supervision"))
    gestion_escolar = Column(String)
    comuna = Column(Integer)
    correo_electronico = Column(String)
    codigo_postal = Column(String)
    telefono = Column(String)
    cuit = Column(String)
    geolocalizacion = Column(String)

class Carrera(Base):
    __tablename__ = "CARRERAS"
    id_carrera = Column(Integer, primary_key=True, index=True)
    nombre = Column(String)
    titulo = Column(String)
    duracion = Column(Integer)

class OfertaAcademica(Base):
    __tablename__ = "OFERTAS_ACADEMICAS"
    id_oferta = Column(Integer, primary_key=True, index=True)
    id_carrera = Column(Integer, ForeignKey("CARRERAS.id_carrera"))
    id_instituto = Column(Integer, ForeignKey("INSTITUTOS.id_instituto"))
    modalidad = Column(String)
    turno = Column(String)
    anio = Column(Integer)

class ConcursoDocente(Base):
    __tablename__ = "CONCURSO_DOCENTE"
    id_concurso = Column(Integer, primary_key=True, index=True)
    id_instituto = Column(Integer, ForeignKey("INSTITUTOS.id_instituto"))
    materia = Column(String)
    fecha_apertura = Column(Date)
    fecha_cierre = Column(Date)
    estado = Column(String)

class Materia(Base):
    __tablename__ = "MATERIAS"
    id_materia = Column(Integer, primary_key=True, index=True)
    id_carrera = Column(Integer, ForeignKey("CARRERAS.id_carrera"))
    nombre = Column(String)
    carga_horaria = Column(Integer)

class DocenteMateria(Base):
    __tablename__ = "DOCENTES_MATERIAS"
    id_asignacion = Column(Integer, primary_key=True, index=True)
    dni = Column(String, ForeignKey("PERSONA.dni"))
    id_materia = Column(Integer, ForeignKey("MATERIAS.id_materia"))
    id_oferta = Column(Integer, ForeignKey("OFERTAS_ACADEMICAS.id_oferta"))
    fecha_desde = Column(Date)
    fecha_hasta = Column(Date)

class Matricula(Base):
    __tablename__ = "MATRICULAS"
    id_matricula = Column(Integer, primary_key=True, index=True)
    dni = Column(String, ForeignKey("PERSONA.dni"))
    id_oferta = Column(Integer, ForeignKey("OFERTAS_ACADEMICAS.id_oferta"))
    anio = Column(Integer)
    cuatrimestral = Column(Boolean)
    estado = Column(String)

class Preinscripcion(Base):
    __tablename__ = "PREINSCRIPCIONES"
    id_formulario = Column(Integer, primary_key=True, index=True)
    dni = Column(String, ForeignKey("PERSONA.dni"))
    id_oferta = Column(Integer, ForeignKey("OFERTAS_ACADEMICAS.id_oferta"))
    fecha_preinscripcion = Column(Date)
    estado = Column(String)