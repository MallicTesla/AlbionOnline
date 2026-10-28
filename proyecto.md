# Proyecto — Capturador de Mercado de Albion Online (Versión Definitiva)

> **Versión:** 1.0
>
> **Sistema operativo:** Windows 10 / Windows 11
>
> **Lenguaje:** Python 3.12+
>
> **Editor recomendado:** Visual Studio Code

---

# Objetivo del proyecto

Crear un programa en Python que capture los paquetes de red de **Albion Online**, identifique los mensajes relacionados con el mercado, extraiga información de precios **únicamente a partir de capturas reales** y guarde todos esos datos en una base SQLite local.

El proyecto está pensado para desarrollarse **paso por paso**, sin omitir etapas y con pruebas obligatorias después de cada una.

---

# Reglas obligatorias del proyecto

## Reglas para la IA

Estas reglas deben cumplirse durante todo el proyecto.

- Todo el código debe estar escrito en español.
- Todos los comentarios deben estar en español.
- Todas las funciones, variables, clases, carpetas y archivos deben tener nombres en español.
- Todas las tablas y columnas de SQLite deben estar en español.
- Nunca inventar información del protocolo Photon.
- Nunca asumir puertos, identificadores de eventos ni estructuras de paquetes.
- Si una información todavía no fue comprobada mediante una captura real, escribir exactamente:

> **PENDIENTE DE VERIFICAR CON CAPTURA REAL**

- Nunca crear archivos antes del paso donde se necesitan.
- Siempre entregar el archivo completo cuando se cree o modifique.
- Nunca continuar automáticamente al siguiente paso.

## Reglas para el usuario

- Realizar todas las pruebas indicadas.
- No continuar si una prueba falla.
- Avisar cualquier diferencia entre el resultado esperado y el obtenido.

---

# Forma de trabajar durante todo el proyecto

Cada paso tendrá exactamente este formato.

1. Objetivo.
2. Checklist.
3. Archivos creados o modificados.
4. Descripción breve de cada archivo.
5. Código completo.
6. Cómo ejecutar.
7. Qué debe hacer el usuario.
8. Prueba obligatoria.
9. Errores comunes.
10. Estado del proyecto.
11. Esperar autorización.

---

# Estructura del proyecto

> **Importante:** La estructura se crea de forma progresiva. Ningún archivo se crea antes del paso donde corresponde.

```text
capturador_mercado_albion/
│
├── codigo/
│   ├── analizadores/
│   └── interfaz/
│
├── datos/
│
├── pruebas/
│
├── README.md
├── requirements.txt
├── .gitignore
└── .env
```

La carpeta del entorno virtual será la creada automáticamente por Python (`.venv`).

No se modifica ni se documenta nada sobre esa carpeta.

---

# Índice del proyecto

## Etapa 1 — Preparación del proyecto

- [ ] Paso 1 — Crear el proyecto y el entorno virtual.
- [ ] Paso 2 — Instalar las librerías necesarias.
- [ ] Paso 3 — Crear la estructura inicial del proyecto.
- [ ] Paso 4 — Configuración del proyecto.

## Etapa 2 — Captura de paquetes

- [ ] Paso 5 — Detectar las interfaces de red.
- [ ] Paso 6 — Capturar paquetes UDP.
- [ ] Paso 7 — Guardar capturas PCAP.
- [ ] Paso 8 — Guardar paquetes JSON.

## Etapa 3 — Base de datos

- [ ] Paso 9 — Crear SQLite.
- [ ] Paso 10 — Guardar paquetes en SQLite.

## Etapa 4 — Ingeniería inversa de Photon

- [ ] Paso 11 — Analizar encabezado Photon.
- [ ] Paso 12 — Detectar eventos del mercado.

## Etapa 5 — Información del mercado

- [ ] Paso 13 — Importar la base de ítems.
- [ ] Paso 14 — Relacionar IDs con nombres.
- [ ] Paso 15 — Guardar precios del mercado.

## Etapa 6 — Interfaz gráfica

- [ ] Paso 16 — Crear la aplicación para consultar precios.

---

# Capturas de referencia (se usarán durante todo el proyecto)

Estas capturas siempre deberán hacerse exactamente igual.

| Captura | Acción dentro de Albion |
|---------|-------------------------|
| Captura A | Caminar durante 10 segundos. |
| Captura B | Abrir y cerrar el inventario. |
| Captura C | Abrir Mercado y buscar **Bolsa de Adepto (T4_BAG)**. |
| Captura D | Buscar **Espada de Adepto (T4_MAIN_SWORD)**. |
| Captura E | Buscar **Piedra Rúnica**. |

Estas capturas serán la referencia para comparar paquetes.

Nunca cambiar los pasos de estas capturas sin documentarlo.

---

# PASO 1 — Crear el proyecto y el entorno virtual

## Objetivo

Preparar el proyecto utilizando el Python que ya está instalado.

## Checklist

- [ ] Crear la carpeta del proyecto.
- [ ] Crear el entorno virtual.
- [ ] Activar el entorno virtual.
- [ ] Actualizar `pip`.
- [ ] Verificar Python y `pip`.

## Archivos creados

**Ninguno.**

## Qué debe hacer el usuario

### Preparación

- Cerrar Visual Studio Code si estaba abierto.
- Abrir PowerShell.

### Acción

Ejecutar:

```powershell
mkdir capturador_mercado_albion
cd capturador_mercado_albion

python -m venv .venv

.venv\Scripts\Activate.ps1

python -m pip install --upgrade pip
```

## Prueba obligatoria

Ejecutar:

```powershell
python --version
pip --version
```

## Resultado esperado

- Aparece `(.venv)` al principio de la consola.
- Se muestra la versión de Python.
- Se muestra la versión de `pip`.

## Errores comunes

- No aparece `(.venv)`.
- PowerShell bloquea scripts.

## Estado del proyecto

- [x] Entorno virtual listo.
- [ ] Dependencias instaladas.

## IMPORTANTE

**DETENERSE AQUÍ.**

Esperar:

> **Continuar con el Paso 2**

---

# PASO 2 — Instalar las librerías necesarias

## Objetivo

Instalar únicamente las dependencias del proyecto.

## Checklist

- [ ] Instalar Scapy.
- [ ] Instalar psutil.
- [ ] Instalar SQLAlchemy.
- [ ] Instalar aiosqlite.
- [ ] Instalar Rich.
- [ ] Instalar python-dotenv.
- [ ] Crear `requirements.txt`.

## Archivos creados

### requirements.txt

Lista de dependencias utilizadas por el proyecto.

## Qué debe hacer el usuario

### Preparación

- Entorno virtual activado (`.venv`).

### Acción

Ejecutar:

```powershell
pip install scapy
pip install psutil
pip install sqlalchemy
pip install aiosqlite
pip install rich
pip install python-dotenv

pip freeze > requirements.txt
```

## Prueba obligatoria

Abrir `requirements.txt`.

Debe contener las librerías instaladas.

## Resultado esperado

Existe el archivo `requirements.txt`.

## Estado del proyecto

- [x] Dependencias instaladas.
- [ ] Estructura creada.

## IMPORTANTE

**DETENERSE AQUÍ.**

Esperar:

> **Continuar con el Paso 3**

---

# PASO 3 — Crear la estructura inicial del proyecto

## Objetivo

Crear únicamente las carpetas y archivos necesarios para comenzar.

## Checklist

- [ ] Crear carpeta `codigo`.
- [ ] Crear carpeta `datos`.
- [ ] Crear carpeta `pruebas`.
- [ ] Crear `principal.py`.
- [ ] Crear `README.md`.
- [ ] Crear `.gitignore`.

## Archivos creados

### codigo/principal.py

Punto de entrada del programa.

### README.md

Documentación general del proyecto.

### .gitignore

Archivos que Git debe ignorar.

## Qué debe hacer el usuario

### Preparación

Estar dentro de `capturador_mercado_albion`.

### Acción

Crear exactamente esta estructura.

```text
capturador_mercado_albion/
│
├── codigo/
├── datos/
├── pruebas/
├── README.md
├── requirements.txt
└── .gitignore
```

## Prueba obligatoria

Verificar que la estructura coincide exactamente.

## Estado del proyecto

- [x] Estructura creada.
- [ ] Configuración creada.

## IMPORTANTE

**DETENERSE AQUÍ.**

Esperar:

> **Continuar con el Paso 4**

---

# PASO 4 — Configuración del proyecto

## Objetivo

Centralizar la configuración del proyecto.

## Checklist

- [ ] Crear `.env`.
- [ ] Crear `configuracion.py`.
- [ ] Leer correctamente las variables.

## Archivos creados

### .env

Configuración editable del proyecto.

### codigo/configuracion.py

Carga la configuración del proyecto.

## Qué debe hacer el usuario

### Acción

Crear `.env` únicamente con los valores indicados durante el paso.

## Prueba obligatoria

Ejecutar un programa que imprima las variables cargadas.

## Resultado esperado

Se muestran correctamente todas las variables.

## Estado del proyecto

- [x] Configuración creada.
- [ ] Interfaces detectadas.

## IMPORTANTE

**DETENERSE AQUÍ.**

Esperar:

> **Continuar con el Paso 5**

---

# PASO 5 — Detectar interfaces de red

## Objetivo

Encontrar la interfaz de red que utilizará Albion Online.

## Checklist

- [ ] Crear `captura_paquetes.py`.
- [ ] Mostrar todas las interfaces disponibles.
- [ ] Identificar la interfaz correcta.

## Archivos creados

### codigo/captura_paquetes.py

Contendrá todas las funciones relacionadas con la captura de paquetes.

## Qué debe hacer el usuario

### Preparación

- [ ] Npcap instalado.
- [ ] Conexión a Internet funcionando.
- [ ] Albion **cerrado**.

### Acción

1. Ejecutar el programa que lista las interfaces.
2. Anotar el nombre exacto de la interfaz conectada a Internet.

## Prueba obligatoria

La consola debe mostrar una lista similar a:

- Ethernet
- Wi-Fi
- Npcap Loopback
- Adaptadores virtuales

## Resultado esperado

El usuario identifica la interfaz que utilizará el proyecto.

## Qué debe anotar el usuario

- Nombre exacto.
- Si es Wi-Fi o Ethernet.

## Estado del proyecto

- [x] Interfaz identificada.
- [ ] Captura UDP.

## IMPORTANTE

**DETENERSE AQUÍ.**

Esperar:

> **Continuar con el Paso 6**

---

# PASO 6 — Capturar paquetes UDP

## Objetivo

Capturar paquetes UDP y mostrarlos en pantalla.

## Checklist

- [ ] Capturar paquetes UDP.
- [ ] Mostrar IP origen.
- [ ] Mostrar IP destino.
- [ ] Mostrar puertos.
- [ ] Mostrar tamaño del paquete.

## Archivos modificados

### codigo/captura_paquetes.py

Se agrega la captura UDP.

## Qué debe hacer el usuario

### Preparación

- [ ] Programa de captura abierto.
- [ ] Albion Online abierto.
- [ ] Personaje conectado.
- [ ] Personaje dentro del mundo (no en pantalla de selección).

### Acción

1. Caminar durante **10 segundos**.
2. Abrir el inventario.
3. Esperar **3 segundos**.
4. Cerrar el inventario.
5. Caminar otros **5 segundos**.

## Prueba obligatoria

Durante todas esas acciones la consola debe mostrar paquetes UDP.

## Resultado esperado

Se imprimen continuamente paquetes.

## Errores comunes

- No aparecen paquetes.
- Se eligió una interfaz incorrecta.

## Estado del proyecto

- [x] Captura UDP funcionando.
- [ ] Captura PCAP.

## IMPORTANTE

**DETENERSE AQUÍ.**

Esperar:

> **Continuar con el Paso 7**

---

# PASO 7 — Guardar capturas PCAP

## Objetivo

Guardar los paquetes en archivos `.pcap`.

## Checklist

- [ ] Crear carpeta `datos/paquetes_crudos`.
- [ ] Guardar una captura por sesión.

## Archivos creados

### datos/paquetes_crudos/

Almacenará todos los archivos `.pcap`.

## Qué debe hacer el usuario

### Preparación

- [ ] Programa capturando paquetes.
- [ ] Albion abierto.
- [ ] Ciudad: **Martlock**.

### Acción (Captura C)

1. Abrir el Mercado.
2. Buscar exactamente:

   **Bolsa de Adepto (T4_BAG)**

3. Esperar **5 segundos**.
4. No mover el personaje.
5. Cerrar el Mercado.
6. Detener la captura.

## Prueba obligatoria

Debe existir un archivo `.pcap`.

## Prueba manual

Abrir el archivo con Wireshark.

## Resultado esperado

Wireshark muestra paquetes UDP.

## Estado del proyecto

- [x] Captura PCAP creada.
- [ ] Captura JSON.

## IMPORTANTE

**DETENERSE AQUÍ.**

Esperar:

> **Continuar con el Paso 8**

---

# PASO 8 — Guardar paquetes JSON

## Objetivo

Guardar todos los paquetes también como archivos JSON.

## Checklist

- [ ] Crear carpeta `datos/paquetes_json`.
- [ ] Guardar payload hexadecimal.
- [ ] Guardar IPs y puertos.

## Archivos creados

### datos/paquetes_json/

Archivos JSON de cada sesión.

## Qué debe hacer el usuario

### Preparación

- [ ] Programa ejecutándose.
- [ ] Albion abierto.
- [ ] Ciudad: Martlock.

### Acción

Repetir exactamente la captura del Paso 7.

1. Buscar **Bolsa de Adepto**.
2. Esperar **5 segundos**.
3. Cerrar Mercado.

## Prueba obligatoria

Debe aparecer un archivo JSON nuevo.

## Resultado esperado

Cada paquete contiene:

- timestamp
- IP origen
- IP destino
- puerto origen
- puerto destino
- payload hexadecimal

## Estado del proyecto

- [x] JSON funcionando.
- [ ] SQLite.

## IMPORTANTE

**DETENERSE AQUÍ.**

Esperar:

> **Continuar con el Paso 9**

---

# PASO 9 — Crear la base SQLite

## Objetivo

Crear la base de datos del proyecto.

## Checklist

- [ ] Crear `base_datos.py`.
- [ ] Crear `albion.db`.
- [ ] Crear tablas.

## Archivos creados

### codigo/base_datos.py

Administra SQLite.

### datos/albion.db

Base local.

## Tablas creadas

- paquetes
- precios_mercado
- items
- ciudades

## Qué debe hacer el usuario

### Acción

Ejecutar el programa que crea la base.

## Prueba obligatoria

Abrir `albion.db` con DB Browser for SQLite.

## Resultado esperado

Las cuatro tablas existen.

## Estado del proyecto

- [x] Base creada.
- [ ] Guardado de paquetes.

## IMPORTANTE

**DETENERSE AQUÍ.**

Esperar:

> **Continuar con el Paso 10**

---

# PASO 10 — Guardar paquetes en SQLite

## Objetivo

Guardar todos los paquetes capturados.

## Checklist

- [ ] Insertar paquetes.
- [ ] Evitar duplicados.

## Archivos modificados

### codigo/base_datos.py

Inserta paquetes.

### codigo/captura_paquetes.py

Guarda automáticamente cada paquete.

## Qué debe hacer el usuario

### Preparación

- [ ] Albion abierto.
- [ ] Ciudad: Martlock.

### Acción

Buscar exactamente estos tres ítems.

1. **Bolsa de Adepto**
2. Esperar **5 segundos**.

3. **Espada de Adepto**
4. Esperar **5 segundos**.

5. **Piedra Rúnica**
6. Esperar **5 segundos**.

Cerrar Mercado.

## Prueba obligatoria

Abrir SQLite.

La tabla `paquetes` debe tener registros nuevos.

## Estado del proyecto

- [x] Paquetes almacenados.
- [ ] Photon.

## IMPORTANTE

**DETENERSE AQUÍ.**

Esperar:

> **Continuar con el Paso 11**

---

# PASO 11 — Analizar encabezado Photon

## Objetivo

Separar encabezado y payload.

## Checklist

- [ ] Crear carpeta `analizadores`.
- [ ] Crear `utilidades_paquetes.py`.
- [ ] Crear `photon.py`.

## Archivos creados

### codigo/analizadores/utilidades_paquetes.py

Funciones para leer datos binarios.

### codigo/analizadores/photon.py

Analizador del encabezado Photon.

## Qué debe hacer el usuario

### Preparación

Usar el archivo PCAP generado en el Paso 7.

### Acción

Ejecutar el analizador sobre ese archivo.

## Prueba obligatoria

Debe mostrar:

- Tamaño del paquete.
- Tamaño del encabezado.
- Tamaño del payload.

## Resultado esperado

No debe interpretar eventos todavía.

## Estado del proyecto

- [x] Photon separado.
- [ ] Eventos del mercado.

## IMPORTANTE

**DETENERSE AQUÍ.**

Esperar:

> **Continuar con el Paso 12**

---

# PASO 12 — Detectar eventos del mercado

## Objetivo

Encontrar los paquetes exclusivos del mercado.

## Checklist

- [ ] Crear `mercado.py`.
- [ ] Comparar capturas.
- [ ] Registrar observaciones.

## Archivos creados

### codigo/analizadores/mercado.py

Analizador específico del mercado.

## Qué debe hacer el usuario

Realizar tres capturas distintas.

---

### Captura A — Movimiento

#### Preparación

- Albion abierto.
- Martlock.

#### Acción

Caminar durante **10 segundos**.

Guardar captura.

---

### Captura B — Inventario

#### Preparación

- Mismo personaje.
- Misma ciudad.

#### Acción

Abrir inventario durante **10 segundos**.

Cerrar inventario.

Guardar captura.

---

### Captura C — Mercado

#### Preparación

- Martlock.

#### Acción

Abrir Mercado.

Buscar:

**Bolsa de Adepto**

Esperar **10 segundos**.

Cerrar Mercado.

Guardar captura.

---

## Prueba obligatoria

El programa debe indicar qué paquetes aparecen solamente en la Captura C.

## Resultado esperado

Lista de paquetes candidatos.

## IMPORTANTE

No asignar nombres ni IDs todavía.

## Estado del proyecto

- [x] Candidatos encontrados.
- [ ] Base de ítems.

## IMPORTANTE

**DETENERSE AQUÍ.**

Esperar:

> **Continuar con el Paso 13**

---

# PASO 13 — Importar la base de ítems

## Objetivo

Importar `items.json`.

## Checklist

- [ ] Descargar base de ítems.
- [ ] Guardarla en `datos`.
- [ ] Importarla a SQLite.

## Archivos creados

### datos/items.json

Base pública de ítems.

### codigo/modelos.py

Modelos de acceso.

## Qué debe hacer el usuario

### Acción

Colocar `items.json` dentro de la carpeta `datos`.

## Prueba obligatoria

Consultar un `UniqueName`.

## Resultado esperado

Devuelve información del ítem.

## Estado del proyecto

- [x] Ítems importados.
- [ ] Resolver IDs.

## IMPORTANTE

**DETENERSE AQUÍ.**

Esperar:

> **Continuar con el Paso 14**

---

# PASO 14 — Relacionar IDs de ítems

## Objetivo

Convertir IDs encontrados en nombres reales.

## Checklist

- [ ] Leer IDs desde SQLite.
- [ ] Buscar nombres.
- [ ] Mostrar nombre localizado.

## Archivos modificados

### codigo/modelos.py

Funciones de búsqueda.

## Qué debe hacer el usuario

### Preparación

Utilizar la captura del Paso 10.

### Acción

Buscar el ID correspondiente a:

- Bolsa de Adepto.
- Espada de Adepto.

## Prueba obligatoria

El programa debe mostrar esos nombres correctamente.

## Estado del proyecto

- [x] IDs resueltos.
- [ ] Precios.

## IMPORTANTE

**DETENERSE AQUÍ.**

Esperar:

> **Continuar con el Paso 15**

---

# PASO 15 — Guardar precios del mercado

## Objetivo

Guardar precios reales.

## Checklist

- [ ] Detectar ciudad.
- [ ] Detectar calidad.
- [ ] Guardar precio de compra.
- [ ] Guardar precio de venta.

## Archivos modificados

### codigo/analizadores/mercado.py

Extrae información del mercado.

### codigo/base_datos.py

Guarda precios.

## Qué debe hacer el usuario

### Preparación

- Albion abierto.
- Ciudad: **Martlock**.

### Acción completa de prueba

Realizar exactamente este recorrido.

#### Búsqueda 1

Buscar:

**Bolsa de Adepto**

Esperar **5 segundos**.

#### Búsqueda 2

Buscar:

**Espada de Adepto**

Esperar **5 segundos**.

#### Búsqueda 3

Buscar:

**Piedra Rúnica**

Esperar **5 segundos**.

#### Finalizar

Cerrar Mercado.

Esperar **3 segundos**.

Detener captura.

## Prueba obligatoria

Abrir SQLite.

La tabla `precios_mercado` debe contener tres registros nuevos.

## Resultado esperado

Cada registro contiene:

- Ítem.
- Ciudad.
- Calidad.
- Precio.
- Fecha.

## Estado del proyecto

- [x] Precios almacenados.
- [ ] Interfaz gráfica.

## IMPORTANTE

**DETENERSE AQUÍ.**

Esperar:

> **Continuar con el Paso 16**

---

# PASO 16 — Crear la interfaz gráfica

## Objetivo

Crear una aplicación para consultar la información almacenada.

## Checklist

- [ ] Crear ventana principal.
- [ ] Buscar ítems.
- [ ] Mostrar historial.
- [ ] Mostrar precios por ciudad.

## Archivos creados

### codigo/interfaz.py

Ventana principal del proyecto.

## Qué debe hacer el usuario

### Preparación

Tener una base `albion.db` con datos obtenidos en el Paso 15.

### Acción

Abrir la aplicación.

Buscar:

- Bolsa de Adepto.
- Espada de Adepto.
- Piedra Rúnica.

## Prueba obligatoria

La aplicación debe mostrar los precios almacenados para esos ítems.

## Resultado esperado

La interfaz consulta SQLite correctamente.

## Estado final del proyecto

- [x] Entorno virtual.
- [x] Dependencias.
- [x] Captura UDP.
- [x] Captura PCAP.
- [x] Captura JSON.
- [x] SQLite.
- [x] Photon.
- [x] Eventos del mercado.
- [x] Base de ítems.
- [x] Relación de IDs.
- [x] Precios.
- [x] Interfaz gráfica.

# Reglas finales del proyecto

## Nunca avanzar automáticamente.

La IA debe detenerse siempre al finalizar un paso y esperar una orden explícita del usuario.

### Órdenes válidas

- `Continuar con el Paso 2`
- `Continuar con el Paso 7`
- `Continuar con el Paso siguiente`

Hasta recibir esa autorización **no se crea código nuevo, no se modifican archivos y no se avanza al siguiente paso**.
