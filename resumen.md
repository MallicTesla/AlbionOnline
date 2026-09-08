# Resumen del proyecto Albion Online

Este proyecto sirve para registrar los precios de objetos de Albion Online en distintas ciudades, mantenerlos actualizados y detectar oportunidades de comercio entre ellas.

Los precios se cargan manualmente en `Scrips/precios.json`. Después, el script de actualización los copia a los archivos de cada ciudad. Los demás scripts permiten calcular rutas rentables y guardar capturas históricas de los precios.

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
│   ├── precios.json
│   └── registrar_precios.py
├── Thetford/
│   └── Comercio.json
└── resumen.md
```

## Archivos y carpetas

- `Scrips/precios.json`: archivo principal donde se anotan los precios de compra y venta de cada objeto por ciudad. El campo `PJ` es solo una referencia personal y los scripts no lo usan.

- `Scrips/actualizar_precios.py`: lee `precios.json` y actualiza los campos `Si_Compro` y `Si_Vendo` de cada `Comercio.json`. Si se agrega un objeto nuevo en `precios.json`, lo crea en los archivos de todas las ciudades. Cuando no existe un precio para una ciudad, usa `0`. Los objetos nuevos comienzan con `Tier: 0`, `Tipo: 0` y `Componentes: []`.

- `Scrips/calcular_comercio.py`: compara `Si_Compro` entre ciudades y muestra las rutas rentables. Calcula la compra en la ciudad de origen, la venta al precio de compra de la ciudad destino, la ganancia y su porcentaje de rentabilidad. `Si_Vendo` no participa en este cálculo.

- `Scrips/registrar_precios.py`: guarda una captura de los precios actuales de todos los archivos de ciudad dentro del historial.

- `Bridgewach/Comercio.json`: lista de objetos y precios actuales de Bridgewach.

- `Fort Sterling/Comercio.json`: lista de objetos y precios actuales de Fort Sterling.

- `Lymhurst/Comercio.json`: lista de objetos y precios actuales de Lymhurst.

- `Martlock/Comercio.json`: lista de objetos y precios actuales de Martlock.

- `Thetford/Comercio.json`: lista de objetos y precios actuales de Thetford.

- `Estadisticas/comercio.jsonl`: historial de capturas. Cada línea es un registro JSON independiente con fecha, hora y los precios de todas las ciudades.

## Uso habitual

1. Editar `Scrips/precios.json` con los precios nuevos.
2. Ejecutar `python Scrips\actualizar_precios.py` para actualizar todas las ciudades.
3. Ejecutar `python Scrips\calcular_comercio.py` para buscar oportunidades de comercio.
4. Opcionalmente, ejecutar `python Scrips\registrar_precios.py` para guardar el estado actual en el historial.
