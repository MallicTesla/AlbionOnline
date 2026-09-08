"""Sincroniza los precios de Scrips/precios.json con cada Comercio.json.

Al agregar un item nuevo a precios.json, el item se crea en todas las ciudades.
Las ciudades que no tengan precio para ese item lo reciben con Si_Compro y
Si_Vendo en 0. El campo PJ se ignora por completo.
"""

import json
from pathlib import Path


RAIZ_PROYECTO = Path(__file__).resolve().parent.parent
ARCHIVO_PRECIOS = Path(__file__).resolve().parent / "precios.json"
NOMBRE_ARCHIVO_CIUDAD = "Comercio.json"


def cargar_json(ruta):
    """Carga un archivo JSON UTF-8 y muestra una ruta util si no es valido."""
    try:
        with ruta.open(encoding="utf-8") as archivo:
            return json.load(archivo)
    except json.JSONDecodeError as error:
        raise ValueError(f"El JSON de {ruta} no es valido: {error}") from error


def obtener_precios_por_ciudad(datos):
    """Convierte precios.json a {ciudad: {item: (compra, venta)}}."""
    precios = {}

    for ciudad in datos.get("Precios", []):
        nombre_ciudad = ciudad.get("ciudad")
        if not nombre_ciudad:
            continue

        items_ciudad = precios.setdefault(nombre_ciudad, {})
        for item in ciudad.get("items", []):
            nombre_item = item.get("item")
            if not nombre_item:
                continue

            items_ciudad[nombre_item] = {
                "compra": item.get("compra", 0),
                "venta": item.get("venta", 0),
            }

    return precios


def crear_item(nombre, precio):
    """Crea un item nuevo con todos los atributos comunes por defecto."""
    return {
        "Item": nombre,
        "Tier": 0,
        "Tipo": 0,
        "Si_Compro": precio["compra"],
        "Si_Vendo": precio["venta"],
        "Componentes": [],
    }


def guardar_comercio(ruta, items):
    """Escribe JSON legible, dejando una linea vacia entre cada item."""
    items_formateados = []
    for item in items:
        texto = json.dumps(item, ensure_ascii=False, indent=4)
        items_formateados.append("\n".join(f"        {linea}" for linea in texto.splitlines()))

    contenido = "{\n    \"Items\": [\n"
    contenido += ",\n\n".join(items_formateados)
    contenido += "\n    ]\n}\n"

    with ruta.open("w", encoding="utf-8", newline="\n") as archivo:
        archivo.write(contenido)


def sincronizar_ciudad(carpeta, precios_ciudad, nombres_items):
    ruta = carpeta / NOMBRE_ARCHIVO_CIUDAD
    datos = cargar_json(ruta)
    items = datos.get("Items", [])
    existentes = {item.get("Item"): item for item in items if item.get("Item")}
    creados = 0

    # Conserva el orden manual existente y anexa los nuevos al final.
    for nombre in nombres_items:
        precio = precios_ciudad.get(nombre, {"compra": 0, "venta": 0})
        item = existentes.get(nombre)
        if item is None:
            item = crear_item(nombre, precio)
            items.append(item)
            existentes[nombre] = item
            creados += 1
        else:
            item["Si_Compro"] = precio["compra"]
            item["Si_Vendo"] = precio["venta"]

    guardar_comercio(ruta, items)
    return creados


def main():
    precios_por_ciudad = obtener_precios_por_ciudad(cargar_json(ARCHIVO_PRECIOS))
    nombres_items = list(
        dict.fromkeys(
            nombre
            for precios_ciudad in precios_por_ciudad.values()
            for nombre in precios_ciudad
        )
    )

    ciudades_actualizadas = 0
    items_creados = 0
    for carpeta in sorted(RAIZ_PROYECTO.iterdir()):
        ruta = carpeta / NOMBRE_ARCHIVO_CIUDAD
        if not carpeta.is_dir() or not ruta.is_file():
            continue

        items_creados += sincronizar_ciudad(
            carpeta, precios_por_ciudad.get(carpeta.name, {}), nombres_items
        )
        ciudades_actualizadas += 1

    print(
        f"Actualizadas {ciudades_actualizadas} ciudades. "
        f"Items nuevos creados: {items_creados}."
    )


if __name__ == "__main__":
    main()
