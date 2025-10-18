# database.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import os

# Ruta ABSOLUTA y CORRECTA a la base de datos
current_dir = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(current_dir, "../database/Concursos.db")

print(f"✅ Base de datos encontrada: {db_path}")

DATABASE_URL = f"sqlite:///{db_path}"

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()