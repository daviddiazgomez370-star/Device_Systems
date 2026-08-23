# 🚀 Device Systems API

API REST desarrollada con **FastAPI** para la gestión de usuarios del sistema **device_systems**.

Este proyecto hace parte de una actividad de aprendizaje orientada al desarrollo de APIs REST utilizando **FastAPI**, **Pydantic v2**, parámetros de ruta, parámetros de consulta, modelos de respuesta y cabeceras HTTP personalizadas.

---

## 📌 Descripción del proyecto

**device_systems** es una aplicación backend desarrollada en Python que permite administrar usuarios mediante una API REST.

La aplicación permite:

* Consultar todos los usuarios.
* Consultar un usuario por su ID.
* Filtrar usuarios por rol.
* Filtrar usuarios por estado activo o inactivo.
* Registrar nuevos usuarios.
* Validar los datos recibidos.
* Evitar registros con correos electrónicos duplicados.
* Estandarizar las respuestas mediante Response Models.
* Utilizar cabeceras HTTP personalizadas.
* Probar los endpoints mediante Swagger UI.

La actividad busca aplicar los fundamentos de FastAPI y construir una API funcional para la administración del recurso `users`.

---

# 🎯 Objetivos

## Objetivo general

Construir una API REST funcional utilizando FastAPI para gestionar usuarios del sistema `device_systems`, aplicando validaciones, parámetros de ruta, parámetros de consulta y respuestas HTTP estructuradas.

## Objetivos específicos

* Configurar un proyecto backend utilizando FastAPI.
* Crear modelos de datos utilizando Pydantic v2.
* Implementar endpoints GET.
* Implementar un endpoint POST.
* Utilizar Path Parameters.
* Utilizar Query Parameters.
* Validar información de los usuarios.
* Evitar correos electrónicos duplicados.
* Implementar Response Models.
* Agregar cabeceras HTTP personalizadas.
* Realizar pruebas utilizando Swagger UI.
* Documentar el proyecto.
* Gestionar el código mediante Git y GitHub.

---

# 🛠️ Tecnologías utilizadas

| Tecnología         | Uso                                  |
| ------------------ | ------------------------------------ |
| Python             | Lenguaje principal                   |
| FastAPI            | Framework para construir la API REST |
| Uvicorn            | Servidor ASGI                        |
| Pydantic v2        | Validación y modelado de datos       |
| Email Validator    | Validación de correos electrónicos   |
| Swagger UI         | Documentación y pruebas de la API    |
| Git                | Control de versiones                 |
| GitHub             | Repositorio remoto                   |
| Visual Studio Code | Editor de código                     |

---

# 📋 Requisitos previos

Antes de ejecutar el proyecto es necesario tener instalado:

* Python 3.x
* Visual Studio Code o un editor similar.
* Git.
* Navegador web.
* Postman o Thunder Client opcionalmente.

También es necesario instalar FastAPI y Uvicorn, componentes establecidos para el desarrollo de la actividad.

---

# 📁 Estructura del proyecto

La estructura recomendada es:

```text
Device_Systems/
│
├── app/
│   ├── __init__.py
│   ├── main.py
│   │
│   ├── schemas/
│   │   ├── __init__.py
│   │   └── user_schema.py
│   │
│   └── routes/
│       ├── __init__.py
│       └── user_routes.py
│
├── venv/
│
├── .gitignore
├── requirements.txt
└── README.md
```

> La carpeta `venv/` corresponde al entorno virtual y no debe subirse al repositorio de GitHub.

---

# ⚙️ Instalación

## 1. Clonar el repositorio

Si el proyecto se encuentra en GitHub, se puede clonar mediante:

```bash
git clone URL_DEL_REPOSITORIO
```

Después ingresar a la carpeta:

```bash
cd Device_Systems
```

---

## 2. Crear el entorno virtual

Desde la carpeta principal del proyecto ejecutar:

```bash
python -m venv venv
```

Esto crea un entorno virtual independiente para las dependencias del proyecto.

---

## 3. Activar el entorno virtual

En Windows:

```bash
venv\Scripts\activate
```

Si la activación fue correcta, la terminal mostrará algo parecido a:

```text
(venv) C:\Users\Administrator\Documents\Device_Systems>
```

---

# 📦 Instalación de dependencias

Con el entorno virtual activo ejecutar:

```bash
python -m pip install fastapi uvicorn email-validator
```

También es posible instalar todas las dependencias desde `requirements.txt`:

```bash
python -m pip install -r requirements.txt
```

---

# 📝 requirements.txt

El proyecto utiliza un archivo `requirements.txt` para registrar las dependencias necesarias.

Para actualizarlo después de instalar paquetes:

```bash
python -m pip freeze > requirements.txt
```

---

# ▶️ Ejecución del proyecto

Para iniciar el servidor ejecutar:

```bash
python -m uvicorn app.main:app --reload
```

El parámetro:

```text
--reload
```

permite que el servidor se reinicie automáticamente cuando se realizan cambios en el código durante el desarrollo.

Si todo funciona correctamente, aparecerá un mensaje similar a:

```text
Uvicorn running on http://127.0.0.1:8000
```

---

# 🌐 URLs importantes

Una vez iniciado el servidor:

### API principal

```text
http://127.0.0.1:8000
```

### Swagger UI

```text
http://127.0.0.1:8000/docs
```

### Documentación alternativa

```text
http://127.0.0.1:8000/redoc
```

Swagger UI permite visualizar y probar los endpoints directamente desde el navegador. La guía establece Swagger UI como una de las herramientas recomendadas para las pruebas de la API.

---

# 👥 Modelo de usuario

El recurso principal de la API es:

```text
users
```

Cada usuario contiene los siguientes campos:

| Campo       | Tipo    | Descripción         |
| ----------- | ------- | ------------------- |
| `id`        | Integer | Identificador único |
| `name`      | String  | Nombre del usuario  |
| `email`     | Email   | Correo electrónico  |
| `role`      | String  | Rol del usuario     |
| `is_active` | Boolean | Estado del usuario  |

---

# 🔐 Validaciones

Los datos enviados a la API son validados mediante **Pydantic**.

## Nombre

El nombre es obligatorio y debe contener mínimo 3 caracteres.

Ejemplo válido:

```json
{
  "name": "Carlos Pérez"
}
```

Ejemplo inválido:

```json
{
  "name": "A"
}
```

---

## Email

El correo electrónico debe tener un formato válido.

Ejemplo válido:

```text
usuario@example.com
```

Ejemplo inválido:

```text
correo-invalido
```

---

## Rol

Los roles permitidos son:

```text
admin
support
user
```

No se permiten otros valores.

Ejemplo válido:

```json
{
  "role": "admin"
}
```

Ejemplo inválido:

```json
{
  "role": "superadmin"
}
```

---

## Estado

El campo `is_active` utiliza valores booleanos:

```json
true
```

o:

```json
false
```

---

# 🔗 Endpoints

La API implementa los siguientes endpoints:

| Método | Endpoint                 | Descripción              |
| ------ | ------------------------ | ------------------------ |
| GET    | `/users/`                | Listar usuarios          |
| GET    | `/users/{user_id}`       | Consultar usuario por ID |
| GET    | `/users/?role=admin`     | Filtrar por rol          |
| GET    | `/users/?is_active=true` | Filtrar por estado       |
| POST   | `/users/`                | Registrar usuario        |

Estos endpoints corresponden a los requisitos establecidos para las fases de GET y POST de la actividad.

---

# 🔎 GET `/users/`

Permite obtener todos los usuarios registrados.

### Petición

```http
GET /users/
```

### Ejemplo de respuesta

```json
[
  {
    "id": 1,
    "name": "Carlos Pérez",
    "email": "carlos@example.com",
    "role": "admin",
    "is_active": true
  },
  {
    "id": 2,
    "name": "Laura Gómez",
    "email": "laura@example.com",
    "role": "support",
    "is_active": true
  }
]
```

---

# 🔎 GET `/users/{user_id}`

Permite consultar un usuario específico utilizando su identificador.

### Ejemplo

```http
GET /users/1
```

### Respuesta

```json
{
  "id": 1,
  "name": "Carlos Pérez",
  "email": "carlos@example.com",
  "role": "admin",
  "is_active": true
}
```

El valor `1` corresponde al **Path Parameter** `user_id`.

---

# 🔎 Filtrar por rol

La API permite filtrar usuarios utilizando el Query Parameter `role`.

### Ejemplo

```http
GET /users/?role=admin
```

Esto devuelve los usuarios cuyo rol sea:

```text
admin
```

También se pueden utilizar:

```text
support
```

o:

```text
user
```

---

# 🔎 Filtrar por estado

La API permite filtrar usuarios utilizando el Query Parameter `is_active`.

### Usuarios activos

```http
GET /users/?is_active=true
```

### Usuarios inactivos

```http
GET /users/?is_active=false
```

---

# 🔎 Combinar filtros

También es posible utilizar los dos filtros:

```http
GET /users/?role=admin&is_active=true
```

Esta consulta busca usuarios que sean administradores y además estén activos.

---

# ➕ POST `/users/`

Permite registrar un nuevo usuario.

### Petición

```http
POST /users/
```

### Body

```json
{
  "name": "David Martínez",
  "email": "david@example.com",
  "role": "user",
  "is_active": true
}
```

### Respuesta esperada

```json
{
  "id": 4,
  "name": "David Martínez",
  "email": "david@example.com",
  "role": "user",
  "is_active": true
}
```

El código de respuesta esperado para una creación exitosa es:

```text
201 Created
```

---

# 🚫 Control de correos duplicados

La aplicación verifica que el correo electrónico no se encuentre registrado previamente.

Si se intenta registrar un correo existente:

```json
{
  "name": "Otro Usuario",
  "email": "david@example.com",
  "role": "user",
  "is_active": true
}
```

La API responde con un error:

```text
400 Bad Request
```

Y un mensaje similar a:

```json
{
  "detail": "El correo electrónico ya está registrado"
}
```

Esta validación forma parte de los requisitos del endpoint POST.

---

# 📤 Response Models

El proyecto utiliza modelos de respuesta para definir la información que devuelve la API.

Ejemplo:

```python
response_model=UserResponse
```

Esto permite:

* Estandarizar las respuestas.
* Definir la estructura de salida.
* Controlar los datos enviados al cliente.
* Mantener respuestas consistentes.

La guía solicita específicamente el uso de Response Models para estandarizar las respuestas y ocultar datos que no sean necesarios.

---

# 🧾 Cabeceras HTTP personalizadas

La API utiliza las siguientes cabeceras:

```text
X-App-Name: device_systems
X-API-Version: 1.0
```

Estas cabeceras permiten identificar la aplicación y la versión de la API.

La actividad establece como ejemplo estas dos cabeceras personalizadas.

---

# 🧪 Pruebas

Las pruebas pueden realizarse mediante:

* Swagger UI.
* Postman.
* Thunder Client.

Estas herramientas permiten comprobar el funcionamiento de los endpoints y verificar las respuestas de la API.

---

# 🧪 Pruebas recomendadas

## Prueba 1 — Listar usuarios

```http
GET /users/
```

**Resultado esperado:** `200 OK`.

---

## Prueba 2 — Buscar usuario existente

```http
GET /users/1
```

**Resultado esperado:** `200 OK`.

---

## Prueba 3 — Buscar usuario inexistente

```http
GET /users/999
```

**Resultado esperado:** `404 Not Found`.

---

## Prueba 4 — Filtrar por rol

```http
GET /users/?role=admin
```

**Resultado esperado:** usuarios con rol `admin`.

---

## Prueba 5 — Filtrar por estado

```http
GET /users/?is_active=true
```

**Resultado esperado:** usuarios activos.

---

## Prueba 6 — Crear usuario

```http
POST /users/
```

Con un usuario válido.

**Resultado esperado:** `201 Created`.

---

## Prueba 7 — Email inválido

Enviar:

```json
{
  "name": "Usuario Prueba",
  "email": "correo-invalido",
  "role": "user",
  "is_active": true
}
```

**Resultado esperado:** `422 Unprocessable Entity`.

---

## Prueba 8 — Nombre corto

Enviar:

```json
{
  "name": "AB",
  "email": "usuario@example.com",
  "role": "user",
  "is_active": true
}
```

**Resultado esperado:** `422 Unprocessable Entity`.

---

## Prueba 9 — Rol inválido

Enviar:

```json
{
  "name": "Usuario Prueba",
  "email": "usuario@example.com",
  "role": "superadmin",
  "is_active": true
}
```

**Resultado esperado:** `422 Unprocessable Entity`.

---

## Prueba 10 — Correo duplicado

Intentar registrar un correo que ya existe.

**Resultado esperado:** `400 Bad Request`.

---

# 📸 Evidencias

Para documentar el desarrollo del proyecto se recomienda incluir capturas de:

1. Estructura del proyecto en Visual Studio Code.
2. Instalación de dependencias.
3. Servidor Uvicorn funcionando.
4. Swagger UI.
5. `GET /users`.
6. `GET /users/{user_id}`.
7. Filtro por `role`.
8. Filtro por `is_active`.
9. `POST /users`.
10. Validación de nombre.
11. Validación de email.
12. Validación de rol.
13. Validación de correo duplicado.
14. Cabeceras HTTP.

La guía solicita evidencias de Swagger, pruebas GET, prueba POST y validaciones/errores.

---

# 🖥️ Ejemplo de ejecución

Después de activar el entorno virtual:

```bash
venv\Scripts\activate
```

Ejecutar:

```bash
python -m uvicorn app.main:app --reload
```

Servidor:

```text
http://127.0.0.1:8000
```

Swagger:

```text
http://127.0.0.1:8000/docs
```

---

# 🛑 Solución de problemas

## Error: `'uvicorn' no se reconoce como un comando`

Si aparece:

```text
'uvicorn' no se reconoce como un comando interno o externo
```

utilizar:

```bash
python -m pip install uvicorn
```

y posteriormente:

```bash
python -m uvicorn app.main:app --reload
```

---

## Error: FastAPI no está instalado

Ejecutar:

```bash
python -m pip install fastapi
```

---

## Error relacionado con EmailStr

Instalar:

```bash
python -m pip install email-validator
```

---

## Error al importar `app`

Verificar que el comando se esté ejecutando desde la carpeta principal:

```text
Device_Systems/
```

La estructura debe contener:

```text
app/
    main.py
```

El comando correcto es:

```bash
python -m uvicorn app.main:app --reload
```

---

# 🔄 Flujo de trabajo

El desarrollo del proyecto sigue este proceso:

```text
Crear proyecto
      ↓
Crear entorno virtual
      ↓
Instalar dependencias
      ↓
Crear estructura de carpetas
      ↓
Crear modelos Pydantic
      ↓
Crear rutas
      ↓
Configurar FastAPI
      ↓
Ejecutar Uvicorn
      ↓
Probar Swagger
      ↓
Validar errores
      ↓
Documentar evidencias
      ↓
Crear README
      ↓
Subir a GitHub
```

---

# 📚 Conceptos aplicados

Durante el desarrollo se aplican los siguientes conceptos:

### FastAPI

Framework utilizado para construir la API REST.

### API REST

Arquitectura utilizada para permitir la comunicación entre clientes y servidor mediante HTTP.

### HTTP GET

Utilizado para consultar información.

### HTTP POST

Utilizado para registrar información.

### Path Parameters

Permiten enviar información directamente en la URL.

Ejemplo:

```text
/users/1
```

### Query Parameters

Permiten enviar filtros mediante la URL.

Ejemplo:

```text
/users/?role=admin
```

### Pydantic

Permite validar y estructurar los datos recibidos.

### Response Models

Definen la estructura de los datos devueltos por la API.

### HTTP Headers

Permiten enviar información adicional en las respuestas HTTP.

---

# 🔐 Consideraciones de seguridad

Este proyecto corresponde a una API educativa y utiliza una estructura sencilla de almacenamiento en memoria.

Por este motivo:

* Los usuarios no se almacenan permanentemente.
* No existe autenticación.
* No existe autorización mediante tokens.
* No se implementa una base de datos.
* Los datos se reinician cuando se reinicia el servidor.

Estas características no forman parte de los requisitos indicados en la guía para este reto.

---

# 📌 Alcance del proyecto

El alcance de `device_systems` está centrado en la gestión básica del recurso `users`.

Incluye:

```text
Usuarios
├── Consulta
├── Búsqueda por ID
├── Filtro por rol
├── Filtro por estado
├── Registro
└── Validación
```

---

# 📊 Códigos HTTP utilizados

| Código | Significado          | Uso                 |
| ------ | -------------------- | ------------------- |
| `200`  | OK                   | Consulta exitosa    |
| `201`  | Created              | Usuario creado      |
| `400`  | Bad Request          | Correo duplicado    |
| `404`  | Not Found            | Usuario inexistente |
| `422`  | Unprocessable Entity | Error de validación |

---

# 🌐 Documentación automática

FastAPI genera automáticamente documentación interactiva.

## Swagger UI

```text
http://127.0.0.1:8000/docs
```

## ReDoc

```text
http://127.0.0.1:8000/redoc
```

Swagger permite ejecutar las peticiones directamente desde la interfaz gráfica.

---

# 📝 Reflexión

El desarrollo de esta actividad permite comprender los fundamentos de la construcción de APIs REST utilizando FastAPI. La implementación de endpoints GET y POST permite trabajar con operaciones básicas de consulta y registro de información.

El uso de Pydantic facilita la validación de los datos recibidos, evitando que la API procese información que no cumple con las reglas establecidas. De igual manera, los Path Parameters y Query Parameters permiten construir endpoints más flexibles para consultar y filtrar usuarios.

Los Response Models ayudan a mantener respuestas estructuradas y consistentes, mientras que las cabeceras HTTP permiten incluir información adicional relacionada con la aplicación y la versión de la API.

Finalmente, Swagger UI facilita las pruebas y permite verificar de manera visual el comportamiento de los diferentes endpoints.

---

# 👨‍💻 Autor

**Aprendiz:** David Díaz Gómez

**Proyecto:** `device_systems`

**Tecnología principal:** FastAPI

**Lenguaje:** Python

**Actividad:** Fundamentos de FastAPI: API REST para Gestión de Usuarios

---



