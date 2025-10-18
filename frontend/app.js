/*
function apiGetClientes() {
  return fetch("http://127.0.0.1:8000/clientes").then(r => r.json());
}

function apiCrearCliente(cliente) {
  return fetch("http://127.0.0.1:8000/clientes", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(cliente)
  }).then(r => r.json());
}

function apiActualizarCliente(id, cliente) {
  return fetch(`http://127.0.0.1:8000/clientes/${id}`, {
    method: "PUT",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(cliente)
  }).then(r => r.json());
}

function apiEliminarCliente(id) {
  return fetch(`http://127.0.0.1:8000/clientes/${id}`, {
    method: "DELETE"
  }).then(r => r.json());
}*/
// URL base del backend
const API_BASE = "http://127.0.0.1:8000";

// Funciones para la API
async function apiGetAlumnos() {
    const response = await fetch(`${API_BASE}/alumnos/`);
    return await response.json();
}

async function apiGetDocentes() {
    const response = await fetch(`${API_BASE}/docentes/`);
    return await response.json();
}

async function apiGetConcursos() {
    const response = await fetch(`${API_BASE}/concursos/`);
    return await response.json();
}

// Función para cargar datos en la página de docentes
async function cargarDatosDocentes() {
    try {
        const docentes = await apiGetDocentes();
        console.log("Docentes cargados:", docentes);
        
        // Actualizar tarjetas de resumen
        document.getElementById('total-docentes').textContent = docentes.length;
        
        // Actualizar tabla
        const tbody = document.getElementById('tabla-docentes');
        tbody.innerHTML = '';
        
        docentes.forEach(docente => {
            const tr = document.createElement('tr');
            tr.innerHTML = `
                <td>${docente.dni}</td>
                <td>${docente.nombre} ${docente.apellido}</td>
                <td>${docente.email || 'N/A'}</td>
                <td>${docente.telefono || 'N/A'}</td>
            `;
            tbody.appendChild(tr);
        });
    } catch (error) {
        console.error("Error cargando docentes:", error);
    }
}

// Función de navegación
function navigateTo(pagina) {
    const pages = {
        'alumnos': 'alumno.html',
        'docentes': 'docente.html',
        'concursos': 'concurso.html',
        'inicio': 'inicio.html',
        'principal': 'pantallaprincipal.html'
    };
    
    if (pages[pagina]) {
        window.location.href = `/static/${pages[pagina]}`;
    }
}

// Inicializar cuando la página cargue
document.addEventListener('DOMContentLoaded', function() {
    // Si estamos en la página de docentes, cargar datos
    if (window.location.pathname.includes('docente.html')) {
        cargarDatosDocentes();
    }
});
