# main.py - VERSIÓN LIMPIA
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from database import engine, Base
import os

# Crear tablas si no existen
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Sistema Gestión Educativa DETS", version="1.0")

# Configurar CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Importar y incluir routers
from routers import (
    alumnos, docentes, concursos,  
    estadisticas, filtros, personas, 
    concursos_crud, carreras, poblar_datos
)

app.include_router(alumnos.router)
app.include_router(docentes.router)  
app.include_router(concursos.router)
app.include_router(estadisticas.router)
app.include_router(filtros.router)
app.include_router(personas.router)
app.include_router(concursos_crud.router)
app.include_router(carreras.router)
app.include_router(poblar_datos.router)

# Servir archivos estáticos del frontend
frontend_path = os.path.join(os.path.dirname(__file__), "../frontend")
app.mount("/static", StaticFiles(directory=frontend_path), name="static")

@app.get("/")
def root():
    return {"message": "Sistema de Gestión Educativa DETS - Backend activo"}

# 🎯 SOLO UN ENDPOINT DE DIAGNÓSTICO ESENCIAL
@app.get("/diagnostico")
def diagnostico():
    """Diagnóstico básico del sistema"""
    import os
    from database import engine, db_path
    from sqlalchemy import text
    
    try:
        # Verificar que la BD existe
        db_exists = os.path.exists(db_path)
        
        # Verificar conexión y tablas
        with engine.connect() as conn:
            result = conn.execute(text("SELECT name FROM sqlite_master WHERE type='table'"))
            tablas = [row[0] for row in result]
            
            # Contar registros en tablas principales
            conteos = {}
            for tabla in ['PERSONA', 'INSTITUTOS', 'CARRERAS', 'CONCURSO_DOCENTE']:
                if tabla in tablas:
                    count_result = conn.execute(text(f"SELECT COUNT(*) FROM {tabla}"))
                    conteos[tabla] = count_result.scalar()
        
        return {
            "estado": "✅ Sistema operativo",
            "bd_existe": db_exists,
            "tablas": len(tablas),
            "conteos": conteos,
            "ruta_bd": db_path
        }
        
    except Exception as e:
        return {
            "estado": "❌ Error en el sistema",
            "error": str(e)
        }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)