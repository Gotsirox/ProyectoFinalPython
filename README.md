Sistema de Gestión de Clientes
Este proyecto es una aplicación web robusta desarrollada con Python y Django para la administración centralizada de clientes. Permite gestionar información detallada, manejar perfiles de usuario personalizados y facilitar la búsqueda de registros de forma eficiente.

🚀 Características Principales
Gestión Integral (CRUD): Creación, lectura, actualización y eliminación de registros de clientes.

Perfiles de Usuario: Implementación de perfiles con carga de imágenes personalizadas.

Motor de Búsqueda: Filtro dinámico para localizar clientes rápidamente en toda la base de datos.

Sección Profesional: Apartado dedicado con información del desarrollador y detalles del proyecto.

🏗️ Arquitectura del Proyecto
La lógica del sistema se divide en 3 aplicaciones de Django para mantener un código limpio y escalable:

usuarios: Maneja la autenticación, registro y la gestión de perfiles con imágenes.

clientes: Administra toda la lógica del CRUD y el motor de búsqueda de registros.

core (o pages): Controla las vistas estáticas, como la sección de información personal y la página de inicio.

🛠️ Tecnologías Utilizadas
Lenguaje: Python 

Framework: Django

Base de Datos: SQLite 

Frontend: HTML5, CSS3 

📋 Requisitos Previos
Asegúrate de tener instalado:

Python 3.14.4

pip 

🔧 Instalación y Configuración
Clonar el repositorio:

Bash
git clone https://github.com/Gotsirox/ProyectoFinalPython
cd ProyectoFinalPython
Crear un entorno virtual:

Bash
    python -m venv venv
    source venv/bin/activate  # En Windows: venv\Scripts\activate
    ```

3.  **Instalar dependencias:**
    
```bash
    pip install -r requirements.txt
    ```

4.  **Realizar las migraciones:**
    
```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

5.  **Iniciar el servidor:**
    ```bash
    python manage.py runserver
    ```

Accede a `[http://127.0.0.1:8000](http://127.0.0.1:8000)` en tu navegador.



Este proyecto fue desarrollado como parte de un trabajo final, aplicando conocimientos de desarrollo web full-stack, manejo de bases de datos relacionales y lógica de servidores con Django.

---
Desarrollado con por Robert Conrado