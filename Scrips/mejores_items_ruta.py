"""Muestra los mejores ítems para comerciar entre dos ciudades."""

import json
from pathlib import Path


# Cambia estas dos ciudades antes de ejecutar el script.
compro_en = "Fort Sterling"
vendo_en = "Lymhurst"

RAIZ_PROYECTO = Path(__file__).resolve().parent.parent
NOMBRE_ARCHIVO = "Comercio.json"
RESET = "\033[0m"
VERDE_CLARO = "\033[92m"
ROJO_CLARO = "\033[91m"
CIAN = "\033[96m"
AMARILLO = "\033[93m"


def cargar_items(ciudad):
    """Carga los ítems de la ciudad indicada y los indexa por nombre."""
    archivo = RAIZ_PROYECTO / ciudad / NOMBRE_ARCHIVO

    if not archivo.is_file():
        return None

    with archivo.open(encoding="utf-8") as contenido:
        items = json.load(contenido).get("Items", [])

    return {item["Item"]: item for item in items if item.get("Item")}


def calcular_mejores_items():
    """Calcula las oportunidades rentables de ``compro_en`` a ``vendo_en``."""
    items_origen = cargar_items(compro_en)
    items_destino = cargar_items(vendo_en)

    if items_origen is None or items_destino is None:
        return None

    oportunidades = []
    for nombre, item_origen in items_origen.items():
        item_destino = items_destino.get(nombre)
        if not item_destino:
            continue

        costo = item_origen.get("Si_Compro", 0)
        venta = item_destino.get("Si_Compro", 0)
        ganancia = venta - costo

        if costo > 0 and ganancia > 0:
            oportunidades.append(
                {
                    "item": nombre,
                    "tier": item_origen.get("Tier", "-"),
                    "costo": costo,
                    "venta": venta,
                    "ganancia": ganancia,
                    "rentabilidad": ganancia / costo * 100,
                }
            )

    return sorted(
        oportunidades,
        key=lambda oportunidad: oportunidad["rentabilidad"],
        reverse=True,
    )


def imprimir_resultados(oportunidades):
    """Imprime las oportunidades ordenadas por rentabilidad."""
    if oportunidades is None:
        print(
            f"No se encontró una ciudad válida. Revisa {VERDE_CLARO}compro_en{RESET} "
            f"y {ROJO_CLARO}vendo_en{RESET}."
        )
        return

    print(
        f"Comprar en {VERDE_CLARO}{compro_en}{RESET} y vender en "
        f"{ROJO_CLARO}{vendo_en}{RESET}\n"
    )

    if not oportunidades:
        print("No hay oportunidades rentables con los precios disponibles.")
        return

    for oportunidad in oportunidades:
        print(
            f"{CIAN}{oportunidad['item']}{RESET} | Tier: {oportunidad['tier']} | "
            f"Compra: {AMARILLO}{oportunidad['costo']}{RESET} | "
            f"Venta: {AMARILLO}{oportunidad['venta']}{RESET} | "
            f"Ganancia: {VERDE_CLARO}{oportunidad['ganancia']}{RESET} | "
            f"Rentabilidad: {VERDE_CLARO}{oportunidad['rentabilidad']:.2f}%{RESET}"
        )


def main():
    imprimir_resultados(calcular_mejores_items())


if __name__ == "__main__":
    main()
