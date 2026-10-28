# Pasos para la aplicación de comercio

Este archivo contiene el plan de trabajo para crear la aplicación local de escritorio con React, TypeScript, Vite y Tauri. Las tareas terminadas se marcarán cambiando `[ ]` por `[x]`.

## 1. Preparación del proyecto

- [ ] Confirmar las reglas de precios: qué significan `compra` y `venta` y cuáles se editan en la aplicación.
- [x] Crear un proyecto de Tauri con React, TypeScript y Vite.
- [ ] Comprobar que la ventana de escritorio se abre correctamente en Windows.
- [ ] Configurar el proyecto para leer y guardar los archivos locales JSON y JSONL.
- [ ] Mantener los scripts actuales de Python como referencia mientras se crea la aplicación.

## 2. Datos y lógica de comercio

- [ ] Leer `Scrips/precios.json` desde la aplicación.
- [ ] Leer los archivos `Comercio.json` de cada ciudad.
- [ ] Leer el historial de `Estadisticas/comercio.jsonl`.
- [ ] Crear la lógica para guardar cambios de precios.
- [ ] Crear la lógica equivalente a `actualizar_precios.py`.
- [ ] Crear la lógica equivalente a `calcular_comercio.py`.
- [ ] Crear la lógica equivalente a `mejores_items_ruta.py`.
- [ ] Crear la lógica equivalente a `mejor_ciudad_venta.py`.
- [ ] Comparar los resultados de la aplicación con los scripts actuales para verificar los cálculos.

## 3. Estructura y estilo visual

- [ ] Crear la estructura principal de la ventana.
- [ ] Crear las pestañas: Precios, Oportunidades, Ruta personalizada, Mejor ciudad de venta e Historial.
- [ ] Definir colores, tipografía, espaciados y estilos generales.
- [ ] Adaptar la interfaz para que se vea correctamente en distintos tamaños de ventana.

## 4. Pestaña Precios

- [ ] Mostrar un selector de ciudad.
- [ ] Cargar la lista de ítems y sus precios de la ciudad seleccionada.
- [ ] Mostrar columnas para nombre del ítem, compra y venta.
- [ ] Hacer que `Tab` siga el orden: nombre → compra → venta → siguiente ítem.
- [ ] Seleccionar todo el nombre del ítem al recibir foco para copiarlo con `Ctrl+C`.
- [ ] Seleccionar todo el precio al recibir foco.
- [ ] Permitir escribir un precio nuevo.
- [ ] Permitir aumentar o disminuir el precio con las flechas ↑ y ↓.
- [ ] Mostrar cambios sin guardar de forma clara.
- [ ] Añadir el botón Guardar cambios.
- [ ] Actualizar los JSON al guardar y mostrar un mensaje de confirmación.

## 5. Pestaña Oportunidades

- [ ] Mostrar las oportunidades rentables entre todas las ciudades.
- [ ] Numerar y ordenar los resultados por rentabilidad.
- [ ] Mostrar ítem, compra, venta, ganancia y rentabilidad.
- [ ] Aplicar colores a ítems, ciudades, precios, ganancias y rentabilidad.
- [ ] Permitir copiar el nombre del ítem y las ciudades.
- [ ] Añadir filtros o búsqueda si resultan necesarios.

## 6. Pestaña Ruta personalizada

- [ ] Permitir elegir una ciudad de compra.
- [ ] Permitir elegir uno o dos destinos de venta.
- [ ] Mostrar las oportunidades de la ruta elegida.
- [ ] Indicar claramente en qué ciudad conviene vender cada ítem.
- [ ] Ordenar los resultados por rentabilidad.

## 7. Pestaña Mejor ciudad de venta

- [ ] Permitir buscar o seleccionar un ítem.
- [ ] Mostrar la ciudad que ofrece el mejor precio de venta.
- [ ] Mostrar la comparación de precios entre todas las ciudades.
- [ ] Permitir copiar el ítem y el nombre de la ciudad.

## 8. Pestaña Historial y gráficas

- [ ] Permitir elegir una ciudad.
- [ ] Permitir elegir un ítem.
- [ ] Permitir elegir entre precio de compra y precio de venta.
- [ ] Mostrar una gráfica de línea con la evolución del precio.
- [ ] Mostrar fecha, hora y precio al pasar sobre cada punto de la gráfica.
- [ ] Permitir comparar el mismo ítem entre varias ciudades.
- [ ] Añadir opciones de período de tiempo si son necesarias.

## 9. Revisión y distribución

- [ ] Probar todas las pestañas y los atajos de teclado.
- [ ] Verificar que guardar precios no dañe los archivos existentes.
- [ ] Crear una copia de seguridad antes de guardar cambios importantes.
- [ ] Crear el ejecutable o instalador para Windows.
- [ ] Probar la aplicación instalada fuera del entorno de desarrollo.
