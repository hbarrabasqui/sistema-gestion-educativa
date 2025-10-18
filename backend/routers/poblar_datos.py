# routers/poblar_datos.py
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from sqlalchemy import text
from datetime import date, timedelta

router = APIRouter(prefix="/util", tags=["util"])

@router.post("/poblar-concursos")
def poblar_concursos_ejemplo(db: Session = Depends(get_db)):
    """Inserta datos de ejemplo en CONCURSO_DOCENTE"""
    
    # Primero verificar si ya hay datos
    check_query = text("SELECT COUNT(*) FROM CONCURSO_DOCENTE")
    count = db.execute(check_query).scalar()
    
    if count > 0:
        return {"message": "Ya existen datos en CONCURSO_DOCENTE", "count": count}
    
    # Obtener algunos institutos existentes
    institutos_query = text("SELECT id_instituto FROM INSTITUTOS LIMIT 5")
    institutos = [row[0] for row in db.execute(institutos_query)]
    
    if not institutos:
        return {"error": "No hay institutos en la BD. Ejecuta /util/poblar-institutos primero"}
    
    # Datos de ejemplo para concursos
    concursos_ejemplo = [
        {
            "id_instituto": institutos[0],
            "materia": "Programación I",
            "fecha_apertura": date(2024, 1, 15),
            "fecha_cierre": date(2024, 2, 15),
            "estado": "Cerrado"
        },
        {
            "id_instituto": institutos[1],
            "materia": "Base de Datos",
            "fecha_apertura": date(2024, 2, 1),
            "fecha_cierre": date(2024, 3, 1),
            "estado": "En Evaluación"
        },
        {
            "id_instituto": institutos[2],
            "materia": "Redes",
            "fecha_apertura": date(2024, 3, 10),
            "fecha_cierre": date(2024, 4, 10),
            "estado": "Abierto"
        },
        {
            "id_instituto": institutos[0],
            "materia": "Sistemas Operativos",
            "fecha_apertura": date(2024, 1, 20),
            "fecha_cierre": date(2024, 2, 20),
            "estado": "Finalizado"
        },
        {
            "id_instituto": institutos[1],
            "materia": "Estadística",
            "fecha_apertura": date(2024, 2, 10),
            "fecha_cierre": date(2024, 3, 10),
            "estado": "Cerrado"
        }
    ]
    
    # Insertar datos
    insert_query = text("""
        INSERT INTO CONCURSO_DOCENTE 
        (id_instituto, materia, fecha_apertura, fecha_cierre, estado)
        VALUES (:id_instituto, :materia, :fecha_apertura, :fecha_cierre, :estado)
    """)
    
    for concurso in concursos_ejemplo:
        db.execute(insert_query, concurso)
    
    db.commit()
    
    return {"message": f"Se insertaron {len(concursos_ejemplo)} concursos de ejemplo"}

@router.post("/poblar-institutos")
def poblar_institutos_ejemplo(db: Session = Depends(get_db)):
    """Inserta datos de ejemplo en INSTITUTOS si está vacío"""
    
    check_query = text("SELECT COUNT(*) FROM INSTITUTOS")
    count = db.execute(check_query).scalar()
    
    if count > 0:
        return {"message": "Ya existen datos en INSTITUTOS", "count": count}
    
    institutos_ejemplo = [
        {
            "nombre": "IFTS 16",
            "direccion": "Av. Corrientes 1234",
            "cue": "123456",
            "id_supervision": 1,
            "gestion_escolar": "Pública",
            "comuna": 1,
            "correo_electronico": "ifts16@buenosaires.edu.ar",
            "telefono": "4111-1111"
        },
        {
            "nombre": "IFTS 18", 
            "direccion": "Av. Santa Fe 5678",
            "cue": "234567",
            "id_supervision": 1,
            "gestion_escolar": "Pública",
            "comuna": 2,
            "correo_electronico": "ifts18@buenosaires.edu.ar",
            "telefono": "4111-2222"
        },
        {
            "nombre": "IFTS 22",
            "direccion": "Av. Rivadavia 9012",
            "cue": "345678", 
            "id_supervision": 1,
            "gestion_escolar": "Pública",
            "comuna": 3,
            "correo_electronico": "ifts22@buenosaires.edu.ar",
            "telefono": "4111-3333"
        }
    ]
    
    insert_query = text("""
        INSERT INTO INSTITUTOS 
        (nombre, direccion, cue, id_supervision, gestion_escolar, comuna, correo_electronico, telefono)
        VALUES (:nombre, :direccion, :cue, :id_supervision, :gestion_escolar, :comuna, :correo_electronico, :telefono)
    """)
    
    for instituto in institutos_ejemplo:
        db.execute(insert_query, instituto)
    
    db.commit()
    
    return {"message": f"Se insertaron {len(institutos_ejemplo)} institutos de ejemplo"}