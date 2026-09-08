"""Guarda capturas de precios de las ciudades sin eliminar el historial."""

import json
from datetime import datetime
from pathlib import Path


RAIZ_PROYECTO = Path(__file__).resolve().parent.parent
NOMBRE_ARCHIVO_CIUDAD = "Comercio.json"
ARCHIVO_HISTORIAL = RAIZ_PROYECTO / "Estadisticas" / "comercio.jsonl"


def cargar_precios_actuales():
    """Obtiene todos los precios registrados actualmente para cada ciudad."""
    ciudades = []

    for carpeta in sorted(RAIZ_PROYECTO.iterdir()):
        archivo_ciudad = carpeta / NOMBRE_ARCHIVO_CIUDAD
        if not carpeta.is_dir() or not archivo_ciudad.is_file():
            continue

        with archivo_ciudad.open(encoding="utf-8") as archivo:
            datos = json.load(archivo)

        items = []
        for item in datos.get("Items", []):
            nombre = item.get("Item")
            if not nombre:
                continue

            items.append(
                {
                    "item": nombre,
                    "compra": item.get("Si_Compro", 0),
                    "venta": item.get("Si_Vendo", 0),
                }
            )

        ciudades.append({"ciudad": carpeta.name, "items": items})

    return ciudades


def guardar_captura(ciudades):
    """Añade una captura al archivo JSON Lines y conserva el historial."""
    captura = {
        "fecha_hora": datetime.now().astimezone().isoformat(timespec="seconds"),
        "ciudades": ciudades,
    }

    ARCHIVO_HISTORIAL.parent.mkdir(exist_ok=True)
    with ARCHIVO_HISTORIAL.open("a", encoding="utf-8") as archivo:
        json.dump(captura, archivo, ensure_ascii=False)
        archivo.write("\n")

    return captura


def main():
    ciudades = cargar_precios_actuales()
    if not ciudades:
        print("No se encontraron archivos Comercio.json para registrar.")
        return

    captura = guardar_captura(ciudades)
    cantidad_items = sum(len(ciudad["items"]) for ciudad in ciudades)
    print(
        f"Precios guardados: {cantidad_items} items de {len(ciudades)} ciudades "
        f"({captura['fecha_hora']})."
    )


if __name__ == "__main__":
    main()
