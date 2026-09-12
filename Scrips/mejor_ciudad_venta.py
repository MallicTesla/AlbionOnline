"""Encuentra la ciudad que paga mejor por un ítem determinado."""

import json
from pathlib import Path


# Escribe aquí el nombre exacto del ítem que quieres consultar.
item_a_buscar = "Tronco de castaño"

RAIZ_PROYECTO = Path(__file__).resolve().parent.parent
NOMBRE_ARCHIVO = "Comercio.json"
RESET = "\033[0m"
VERDE_CLARO = "\033[92m"
ROJO_CLARO = "\033[91m"
CIAN = "\033[96m"
AMARILLO = "\033[93m"


def buscar_precios(item_buscado):
    """Obtiene el precio Si_Compro del ítem en cada ciudad disponible."""
    resultados = []

    for carpeta in RAIZ_PROYECTO.iterdir():
        archivo = carpeta / NOMBRE_ARCHIVO
        if not carpeta.is_dir() or not archivo.is_file():
            continue

        with archivo.open(encoding="utf-8") as contenido:
            items = json.load(contenido).get("Items", [])

        item = next(
            (item for item in items if item.get("Item", "").lower() == item_buscado.lower()),
            None,
        )
        if item and item.get("Si_Compro", 0) > 0:
            resultados.append(
                {
                    "ciudad": carpeta.name,
                    "precio": item["Si_Compro"],
                    "tier": item.get("Tier", "-"),
                }
            )

    return sorted(resultados, key=lambda resultado: resultado["precio"], reverse=True)


def imprimir_resultados(resultados):
    """Muestra la mejor ciudad y la comparación con las demás."""
    if not resultados:
        print(f"No se encontró el ítem {ROJO_CLARO}{item_a_buscar}{RESET}.")
        return

    mejor_precio = resultados[0]["precio"]
    mejores_ciudades = [
        resultado["ciudad"]
        for resultado in resultados
        if resultado["precio"] == mejor_precio
    ]

    print(f"Ítem: {CIAN}{item_a_buscar}{RESET} | Tier: {resultados[0]['tier']}")
    print(
        f"Mejor ciudad para vender: {VERDE_CLARO}{', '.join(mejores_ciudades)}{RESET} "
        f"| Precio: {AMARILLO}{mejor_precio}{RESET}\n"
    )
    print("Precios por ciudad:")

    for posicion, resultado in enumerate(resultados, start=1):
        color_ciudad = VERDE_CLARO if resultado["precio"] == mejor_precio else ROJO_CLARO
        print(
            f"{posicion}. {color_ciudad}{resultado['ciudad']}{RESET} | "
            f"Precio de venta: {AMARILLO}{resultado['precio']}{RESET}"
        )


def main():
    imprimir_resultados(buscar_precios(item_a_buscar))


if __name__ == "__main__":
    main()
