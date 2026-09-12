# Resumen del proyecto Albion Online

Este proyecto permite registrar los precios de objetos de Albion Online en distintas ciudades, actualizarlos y encontrar oportunidades de comercio.

Los precios se cargan en `Scrips/precios.json`. Después, el script de actualización los copia a los archivos de cada ciudad. Los demás scripts calculan rutas rentables, comparan destinos de venta y guardan capturas históricas.

## Estructura

```text
Albion Online/
├── Bridgewach/
│   └── Comercio.json
├── Estadisticas/
│   └── comercio.jsonl
├── Fort Sterling/
│   └── Comercio.json
├── Lymhurst/
│   └── Comercio.json
├── Martlock/
│   └── Comercio.json
├── Scrips/
│   ├── actualizar_precios.py
│   ├── calcular_comercio.py
│   ├── mejor_ciudad_venta.py
│   ├── mejores_items_ruta.py
│   ├── mejores_ventas_ciudades.py
│   ├── precios.json
│   └── registrar_precios.py
├── Thetford/
│   └── Comercio.json
└── resumen.md
```

## Archivos y carpetas

- `Scrips/precios.json`: archivo principal donde se anotan los precios de compra y venta de cada objeto por ciudad. El campo `PJ` es solo una referencia personal y los scripts no lo usan.

- `Scrips/actualizar_precios.py`: lee `precios.json` y actualiza los campos `Si_Compro` y `Si_Vendo` de cada `Comercio.json`. Si se agrega un objeto nuevo en `precios.json`, lo crea en los archivos de todas las ciudades. Cuando no existe un precio para una ciudad, usa `0`. Los objetos nuevos comienzan con `Tier: 0`, `Tipo: 0` y `Componentes: []`.

- `Scrips/calcular_comercio.py`: compara `Si_Compro` entre todas las ciudades y muestra las rutas rentables, ordenadas por rentabilidad. Cada resultado está numerado y usa colores: número magenta, ítem cian, ciudad de compra verde claro, ciudad de venta roja, precios amarillos y ganancia/rentabilidad verdes. `Si_Vendo` no participa en este cálculo.

- `Scrips/mejores_items_ruta.py`: busca oportunidades desde una ciudad de compra hacia una o más ciudades de venta. Configura las variables al inicio del archivo:

  ```python
  compro_en = "Lymhurst"
  vendo_en = ["Bridgewach", "Fort Sterling"]
  ```

  Para una ruta entre dos ciudades, deja solo un destino, por ejemplo `vendo_en = ["Martlock"]`. Los resultados indican la ciudad específica donde vender cada ítem y están ordenados por rentabilidad.

- `Scrips/mejor_ciudad_venta.py`: indica en qué ciudad se paga mejor un ítem específico. Cambia la variable `item_a_buscar` al inicio; el script muestra la mejor ciudad y una lista de precios de todas las ciudades, de mayor a menor.

- `Scrips/mejores_ventas_ciudades.py`: muestra el ítem base y fabricado con mayor precio `Si_Compro` en cada ciudad.

- `Scrips/registrar_precios.py`: guarda una captura de los precios actuales de todos los archivos de ciudad dentro del historial.

- `Bridgewach/Comercio.json`, `Fort Sterling/Comercio.json`, `Lymhurst/Comercio.json`, `Martlock/Comercio.json` y `Thetford/Comercio.json`: listas de objetos y precios actuales de cada ciudad. Nota: el nombre de la carpeta es `Bridgewach`.

- `Estadisticas/comercio.jsonl`: historial de capturas. Cada línea es un registro JSON independiente con fecha, hora y los precios de todas las ciudades.

## Uso habitual

1. Editar `Scrips/precios.json` con los precios nuevos.
2. Ejecutar `python Scrips\actualizar_precios.py` para actualizar todas las ciudades.
3. Ejecutar uno de los análisis:
   - `python Scrips\calcular_comercio.py` para revisar todas las rutas rentables.
   - `python Scrips\mejores_items_ruta.py` para comparar una compra con uno o dos destinos de venta.
   - `python Scrips\mejor_ciudad_venta.py` para saber dónde vender mejor un ítem concreto.
4. Opcionalmente, ejecutar `python Scrips\registrar_precios.py` para guardar el estado actual en el historial.
