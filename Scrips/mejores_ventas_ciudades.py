"""Muestra el ítem base y fabricado que mejor se vende en cada ciudad."""

import json
from pathlib import Path


RAIZ_PROYECTO = Path(__file__).resolve().parent.parent
NOMBRE_ARCHIVO = "Comercio.json"
ORDEN_CIUDADES = [
    "Lymhurst",
    "Martlock",
    "Thetford",
    "Fort Sterling",
    "Bridgewach",
]


def mejor_item(items, tipo):
    """Devuelve el artículo de ``tipo`` con el mayor precio Si_Compro."""
    candidatos = [
        item
        for item in items
        if item.get("Tipo") == tipo and item.get("Si_Compro", 0) > 0
    ]
    return max(candidatos, key=lambda item: item["Si_Compro"], default=None)


def obtener_mejores_ventas():
    """Obtiene el mejor ítem base y fabricado de cada ciudad."""
    mejores_por_ciudad = []

    for carpeta in RAIZ_PROYECTO.iterdir():
        archivo = carpeta / NOMBRE_ARCHIVO
        if not carpeta.is_dir() or not archivo.is_file():
            continue

        with archivo.open(encoding="utf-8") as contenido:
            items = json.load(contenido).get("Items", [])

        resultados = {"ciudad": carpeta.name}
        for tipo, clave in (("Base", "base"), ("Fabricado", "fabricado")):
            item = mejor_item(items, tipo)
            if item:
                resultados[clave] = item

        if len(resultados) > 1:
            mejores_por_ciudad.append(resultados)

    posiciones = {ciudad: posicion for posicion, ciudad in enumerate(ORDEN_CIUDADES)}
    return sorted(
        mejores_por_ciudad,
        key=lambda resultado: posiciones.get(resultado["ciudad"], len(posiciones)),
    )


def imprimir_resultados(resultados):
    if not resultados:
        print("No hay precios disponibles.")
        return

    for resultado in resultados:
        for tipo in ("base", "fabricado"):
            item = resultado.get(tipo)
            if not item:
                continue
            print(
                f"{resultado['ciudad']}: {item['Item']} | Tier: {item['Tier']} "
                f"| Mejor precio de venta: {item['Si_Compro']}"
            )
        print()


def main():
    imprimir_resultados(obtener_mejores_ventas())


if __name__ == "__main__":
    main()
