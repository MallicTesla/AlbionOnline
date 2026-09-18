# Proyecto: Capturador de Mercado de Albion Online

## Objetivo del proyecto

Crear un programa en Python que capture los paquetes UDP de Albion
Online, identifique los mensajes del mercado, decodifique únicamente
información obtenida de capturas reales y guarde todos los datos en una
base SQLite local.

> **Importante:** Este proyecto no modifica el juego, no automatiza
> acciones, no utiliza OCR ni inyección de código. Toda la información
> proviene exclusivamente de paquetes de red capturados localmente.

------------------------------------------------------------------------

# Reglas obligatorias del proyecto

-   Todo el código debe estar en español.
-   Todos los comentarios deben estar en español.
-   Variables, funciones, clases, archivos, carpetas y tablas SQLite
    estarán en español.
-   No inventar datos del protocolo Photon.
-   Si un dato no fue comprobado mediante una captura real, debe
    marcarse como **PENDIENTE DE VERIFICAR CON CAPTURA REAL**.
-   No agregar librerías nuevas sin explicar por qué son necesarias.
-   Nunca saltar un paso.
-   Al terminar un paso, detenerse y esperar que el usuario escriba (**Continuar con el Paso X**) a demás dale el mensaje (**Continuar con el Paso X**)

------------------------------------------------------------------------

# Flujo de trabajo obligatorio

Cada paso seguirá exactamente este orden:

1.  Explicación del objetivo.
2.  Checklist del paso.
3.  Archivos que se crearán o modificarán.
4.  Breve descripción de cada archivo nuevo.
5.  Código completo de los archivos.
6.  Comandos para ejecutar.
7.  Prueba obligatoria.
8.  Resultado esperado.
9.  Esperar autorización para continuar.

------------------------------------------------------------------------

# Estructura inicial del proyecto

La estructura completa **NO se crea desde el principio**. Cada carpeta y
archivo se crea únicamente cuando el paso correspondiente lo requiera.

``` text
capturador_mercado_albion/
│
├── codigo/
├── datos/
├── pruebas/
├── requirements.txt
├── README.md
└── .gitignore
```

> La carpeta del entorno virtual será la que Python crea automáticamente
> (`.venv` o la predeterminada). No se modifica ni se renombra.

------------------------------------------------------------------------

# Índice general del proyecto

-   [ ] Paso 1 --- Crear el proyecto y el entorno virtual.
-   [ ] Paso 2 --- Instalar las librerías necesarias.
-   [ ] Paso 3 --- Crear la estructura inicial del proyecto.
-   [ ] Paso 4 --- Configuración del proyecto (.env y configuracion.py).
-   [ ] Paso 5 --- Detectar interfaces de red.
-   [ ] Paso 6 --- Capturar paquetes UDP.
-   [ ] Paso 7 --- Guardar capturas PCAP.
-   [ ] Paso 8 --- Guardar paquetes en JSON.
-   [ ] Paso 9 --- Crear la base SQLite.
-   [ ] Paso 10 --- Guardar paquetes en SQLite.
-   [ ] Paso 11 --- Analizar encabezados Photon.
-   [ ] Paso 12 --- Detectar eventos del mercado.
-   [ ] Paso 13 --- Importar la base de ítems.
-   [ ] Paso 14 --- Relacionar IDs de ítems.
-   [ ] Paso 15 --- Guardar precios del mercado.
-   [ ] Paso 16 --- Crear la interfaz gráfica.

------------------------------------------------------------------------

# Paso 1 --- Crear el proyecto y el entorno virtual

## Objetivo

Preparar el proyecto y crear el entorno virtual utilizando la
herramienta estándar de Python.

## Checklist

-   [ ] Crear la carpeta del proyecto.
-   [ ] Crear el entorno virtual.
-   [ ] Activar el entorno virtual.
-   [ ] Actualizar pip.
-   [ ] Verificar que Python funciona dentro del entorno.

## Archivos que se crean

**Ninguno.**

## Prueba obligatoria

-   `python --version`
-   `pip --version`

## Resultado esperado

El entorno virtual queda activo y listo.

**Esperar autorización para continuar con el Paso 2.**

------------------------------------------------------------------------

# Paso 2 --- Instalar las librerías necesarias

## Objetivo

Instalar únicamente las dependencias necesarias para comenzar el
proyecto.

## Checklist

-   [ ] Instalar Scapy.
-   [ ] Instalar psutil.
-   [ ] Instalar SQLAlchemy.
-   [ ] Instalar aiosqlite.
-   [ ] Instalar Rich.
-   [ ] Instalar python-dotenv.
-   [ ] Generar requirements.txt.

## Archivos que se crean

### requirements.txt

Lista completa de dependencias del proyecto.

## Prueba obligatoria

Ejecutar `pip freeze` y verificar que las dependencias aparecen.

**Esperar autorización para continuar con el Paso 3.**

------------------------------------------------------------------------

# Paso 3 --- Crear la estructura inicial del proyecto

## Objetivo

Crear únicamente las carpetas y archivos necesarios para comenzar a
programar.

## Checklist

-   [ ] Crear carpeta `codigo`.
-   [ ] Crear carpeta `datos`.
-   [ ] Crear carpeta `pruebas`.
-   [ ] Crear archivo `principal.py`.
-   [ ] Crear archivo `README.md`.
-   [ ] Crear archivo `.gitignore`.

## Archivos que se crean

### codigo/principal.py

Punto de entrada del programa. Desde aquí comenzará la ejecución del
proyecto.

### README.md

Documentación general del proyecto.

### .gitignore

Archivos y carpetas que Git no debe controlar.

## Prueba obligatoria

Verificar que la estructura de carpetas coincide exactamente con la del
paso.

**Esperar autorización para continuar con el Paso 4.**

------------------------------------------------------------------------

# Paso 4 --- Configuración del proyecto

## Objetivo

Crear la configuración central del proyecto y cargar variables desde
`.env`.

## Checklist

-   [ ] Crear `.env`.
-   [ ] Crear `codigo/configuracion.py`.
-   [ ] Leer las variables correctamente.

## Archivos que se crean

### .env

Configuración editable del proyecto.

### codigo/configuracion.py

Carga y valida la configuración.

## Prueba obligatoria

Ejecutar un script que imprima la configuración cargada.

**Esperar autorización para continuar con el Paso 5.**

------------------------------------------------------------------------

# Paso 5 --- Detectar interfaces de red

## Objetivo

Detectar todas las interfaces de red disponibles mediante Scapy.

## Checklist

-   [ ] Crear `codigo/captura_paquetes.py`.
-   [ ] Mostrar todas las interfaces.
-   [ ] Identificar la interfaz utilizada por Albion.

## Archivos que se crean

### codigo/captura_paquetes.py

Funciones relacionadas con la captura de paquetes de red.

## Prueba obligatoria

Debe mostrarse una lista de interfaces disponibles.

**Esperar autorización para continuar con el Paso 6.**

------------------------------------------------------------------------

# Paso 6 --- Capturar paquetes UDP

## Objetivo

Capturar paquetes UDP y mostrarlos por consola.

## Checklist

-   [ ] Capturar paquetes UDP.
-   [ ] Mostrar origen, destino, puertos y tamaño.

## Archivos que se modifican

### codigo/captura_paquetes.py

Se agrega la lógica de captura.

## Prueba obligatoria

Al abrir Albion deben aparecer paquetes UDP.

**Esperar autorización para continuar con el Paso 7.**

------------------------------------------------------------------------

# Paso 7 --- Guardar capturas PCAP

## Objetivo

Guardar todos los paquetes capturados en archivos `.pcap`.

## Checklist

-   [ ] Crear carpeta `datos/paquetes_crudos`.
-   [ ] Guardar una captura por sesión.

## Archivos que se crean

### datos/paquetes_crudos/

Contendrá las capturas PCAP.

## Prueba obligatoria

Abrir el archivo PCAP en Wireshark.

**Esperar autorización para continuar con el Paso 8.**

------------------------------------------------------------------------

# Paso 8 --- Guardar paquetes en JSON

## Objetivo

Guardar cada paquete capturado también en formato JSON.

## Checklist

-   [ ] Crear carpeta `datos/paquetes_json`.
-   [ ] Guardar timestamp, IPs, puertos y payload hexadecimal.

## Archivos que se crean

### datos/paquetes_json/

Archivos JSON de cada paquete.

## Prueba obligatoria

Verificar que se generan archivos JSON correctamente.

**Esperar autorización para continuar con el Paso 9.**

------------------------------------------------------------------------

# Paso 9 --- Crear la base SQLite

## Objetivo

Crear la base de datos local del proyecto.

## Checklist

-   [ ] Crear `codigo/base_datos.py`.
-   [ ] Crear `datos/albion.db`.
-   [ ] Crear tablas iniciales.

## Archivos que se crean

### codigo/base_datos.py

Manejo de la base SQLite.

### datos/albion.db

Base de datos local.

## Tablas que se crean

-   paquetes
-   precios_mercado
-   items
-   ciudades

## Prueba obligatoria

Abrir la base y verificar las tablas.

**Esperar autorización para continuar con el Paso 10.**

------------------------------------------------------------------------

# Paso 10 --- Guardar paquetes en SQLite

## Objetivo

Registrar todos los paquetes capturados en la base.

## Checklist

-   [ ] Insertar paquetes.
-   [ ] Evitar duplicados.

## Archivos que se modifican

### codigo/base_datos.py

Inserción de paquetes.

### codigo/captura_paquetes.py

Guardar paquetes automáticamente.

## Prueba obligatoria

Verificar registros dentro de SQLite.

**Esperar autorización para continuar con el Paso 11.**

------------------------------------------------------------------------

# Paso 11 --- Analizar encabezados Photon

## Objetivo

Separar encabezado y payload del protocolo Photon.

## Checklist

-   [ ] Crear carpeta `codigo/analizadores`.
-   [ ] Crear `utilidades_paquetes.py`.
-   [ ] Crear `photon.py`.

## Archivos que se crean

### codigo/analizadores/utilidades_paquetes.py

Funciones para leer datos binarios.

### codigo/analizadores/photon.py

Analizador del encabezado Photon.

## Prueba obligatoria

Separar encabezado y payload de paquetes reales.

**Esperar autorización para continuar con el Paso 12.**

------------------------------------------------------------------------

# Paso 12 --- Detectar eventos del mercado

## Objetivo

Encontrar los paquetes que pertenecen al mercado comparando capturas
reales.

## Checklist

-   [ ] Crear `mercado.py`.
-   [ ] Registrar observaciones.
-   [ ] Marcar eventos candidatos.

## Archivos que se crean

### codigo/analizadores/mercado.py

Analizador de eventos relacionados con el mercado.

## Prueba obligatoria

Identificar candidatos reales sin asumir IDs.

**Esperar autorización para continuar con el Paso 13.**

------------------------------------------------------------------------

# Paso 13 --- Importar la base de ítems

## Objetivo

Importar la base pública de ítems de Albion.

## Checklist

-   [ ] Descargar `items.json`.
-   [ ] Importarlo a SQLite.

## Archivos que se crean

### datos/items.json

Base pública de ítems.

### codigo/modelos.py

Modelos de acceso a los datos.

## Prueba obligatoria

Consultar un ítem por `UniqueName`.

**Esperar autorización para continuar con el Paso 14.**

------------------------------------------------------------------------

# Paso 14 --- Relacionar IDs de ítems

## Objetivo

Convertir IDs de los paquetes en nombres de ítems.

## Checklist

-   [ ] Buscar IDs.
-   [ ] Mostrar nombre localizado.

## Archivos que se modifican

### codigo/modelos.py

Funciones de búsqueda.

## Prueba obligatoria

Mostrar correctamente el nombre de un ítem conocido.

**Esperar autorización para continuar con el Paso 15.**

------------------------------------------------------------------------

# Paso 15 --- Guardar precios del mercado

## Objetivo

Guardar precios reales detectados en SQLite.

## Checklist

-   [ ] Registrar ciudad.
-   [ ] Registrar calidad.
-   [ ] Registrar precio de compra y venta.

## Archivos que se modifican

### codigo/analizadores/mercado.py

Extracción de precios.

### codigo/base_datos.py

Inserción de precios.

## Prueba obligatoria

Ver un precio real guardado en la base.

**Esperar autorización para continuar con el Paso 16.**

------------------------------------------------------------------------

# Paso 16 --- Crear la interfaz gráfica

## Objetivo

Crear una aplicación de escritorio para consultar los datos capturados.

## Checklist

-   [ ] Crear ventana principal.
-   [ ] Buscar ítems.
-   [ ] Mostrar historial de precios.

## Archivos que se crean

### codigo/interfaz.py

Interfaz gráfica del proyecto.

## Prueba obligatoria

Buscar un ítem y visualizar precios almacenados.

**Proyecto finalizado.**
