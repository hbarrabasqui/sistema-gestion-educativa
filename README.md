Sistema web completo para la gestión de instituciones educativas, desarrollado con **FastAPI (backend)** y **HTML/CSS/JavaScript (frontend)**.

---

## 🚀 Características Principales

- **👥 Gestión de Personas** — CRUD completo de alumnos, docentes y administradores.  
- **📊 Concursos Docentes** — Gestión y visualización de concursos con gráficos.  
- **🏫 Oferta Académica** — Administración de carreras y materias.  
- **📈 Dashboard** — Estadísticas en tiempo real.  
- **💾 Base de Datos SQLite** — Datos persistentes y reales.

---

## 🛠️ Tecnologías Utilizadas

- **Backend:** FastAPI, SQLAlchemy, Pydantic  
- **Frontend:** HTML5, CSS3, JavaScript (Vanilla)  
- **Base de Datos:** SQLite  
- **Gráficos:** Chart.js

---

## 📥 Instalación Rápida desde VS Code

### 🔧 Prerrequisitos

- Python **3.8+**
- Git
- Visual Studio Code (VS Code)

---

### 🪄 Paso a Paso en VS Code

#### 1️⃣ Abrir la terminal en VS Code
Presioná `Ctrl + Ñ` o desde el menú **Ver → Terminal**.

#### 2️⃣ Clonar el repositorio
```bash
git clone https://github.com/hbarrabasqui/sistema-gestion-educativa.git
cd sistema-gestion-educativa
```

#### 3️⃣ Crear y activar el entorno virtual
```bash
python -m venv venv
```

**Activar el entorno virtual (Windows):**
```bash
venv\Scripts\activate
```

**Si usás Mac/Linux:**
```bash
source venv/bin/activate
```

> 💡 Cuando veas `(venv)` al principio de la línea de comandos, significa que el entorno está activo.

#### 4️⃣ Navegar a la carpeta del backend e instalar dependencias
```bash
cd backend
pip install -r requirements.txt
```

#### 5️⃣ Ejecutar el servidor FastAPI
```bash
python -m uvicorn main:app --reload
```

#### 6️⃣ Abrir la aplicación en el navegador
👉 [http://127.0.0.1:8000/static/inicio.html](http://127.0.0.1:8000/static/inicio.html)

---

## 🔐 Usuarios de Prueba

| Rol        | Usuario   | Contraseña   |
|-------------|------------|---------------|
| 🧑‍💼 Administrador | `admin`     | `admin123`     |
| 👨‍🏫 Docente       | `docente`   | `docente123`   |
| 🧑‍💻 Supervisor    | `supervisor` | `super123`     |

---

## 💡 Notas finales

- Podés modificar la base de datos `Concursos.db` según tus necesidades.  
- Todos los archivos del frontend se encuentran en la carpeta `frontend/`.  
- La API está documentada automáticamente en:  
  👉 [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

---

✳️ **Autor:** xxxxxxxxxxx 
📅 Proyecto Profesionalizante — 2025






