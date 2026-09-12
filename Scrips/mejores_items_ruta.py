"""Muestra los mejores ítems para comerciar entre una compra y varias ventas."""

import json
from pathlib import Path


# Una ciudad permite una ruta normal; dos ciudades permiten compararlas.
# Ejemplos: ["Lymhurst"] o ["Bridgewach", "Fort Sterling"]
compro_en = "Lymhurst"
vendo_en = ["Bridgewach", "Fort Sterling"]

RAIZ_PROYECTO = Path(__file__).resolve().parent.parent
NOMBRE_ARCHIVO = "Comercio.json"
RESET = "\033[0m"
VERDE_CLARO = "\033[92m"
ROJO_CLARO = "\033[91m"
CIAN = "\033[96m"
AMARILLO = "\033[93m"


def cargar_items(ciudad):
    """Carga los ítems de una ciudad y los indexa por nombre."""
    archivo = RAIZ_PROYECTO / ciudad / NOMBRE_ARCHIVO
    if not archivo.is_file():
        return None

    with archivo.open(encoding="utf-8") as contenido:
        items = json.load(contenido).get("Items", [])

    return {item["Item"]: item for item in items if item.get("Item")}


def calcular_mejores_items():
    """Calcula oportunidades desde ``compro_en`` a cada ciudad de ``vendo_en``."""
    items_origen = cargar_items(compro_en)
    ciudades_venta = [vendo_en] if isinstance(vendo_en, str) else vendo_en
    ciudades_venta = list(dict.fromkeys(ciudades_venta))

    if items_origen is None:
        return None, ciudades_venta

    items_por_destino = {
        ciudad: cargar_items(ciudad)
        for ciudad in ciudades_venta
        if ciudad != compro_en
    }
    ciudades_no_encontradas = [
        ciudad for ciudad, items in items_por_destino.items() if items is None
    ]

    oportunidades = []
    for ciudad, items_destino in items_por_destino.items():
        if items_destino is None:
            continue

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
                        "destino": ciudad,
                        "costo": costo,
                        "venta": venta,
                        "ganancia": ganancia,
                        "rentabilidad": ganancia / costo * 100,
                    }
                )

    return (
        sorted(
            oportunidades,
            key=lambda oportunidad: oportunidad["rentabilidad"],
            reverse=True,
        ),
        ciudades_no_encontradas,
    )


def imprimir_resultados(oportunidades, ciudades_no_encontradas):
    """Imprime las oportunidades ordenadas por rentabilidad."""
    if oportunidades is None:
        print(
            f"No se encontró la ciudad de compra: "
            f"{VERDE_CLARO}{compro_en}{RESET}."
        )
        return

    ciudades_venta = [vendo_en] if isinstance(vendo_en, str) else vendo_en
    print(
        f"Comprar en {VERDE_CLARO}{compro_en}{RESET} y vender en "
        f"{ROJO_CLARO}{', '.join(ciudades_venta)}{RESET}\n"
    )

    if ciudades_no_encontradas:
        print(
            f"Ciudades no encontradas: {ROJO_CLARO}"
            f"{', '.join(ciudades_no_encontradas)}{RESET}\n"
        )

    if not oportunidades:
        print("No hay oportunidades rentables con los precios disponibles.")
        return

    for oportunidad in oportunidades:
        print(
            f"{CIAN}{oportunidad['item']}{RESET} | Tier: {oportunidad['tier']} | "
            f"Vender en: {ROJO_CLARO}{oportunidad['destino']}{RESET} | "
            f"Compra: {AMARILLO}{oportunidad['costo']}{RESET} | "
            f"Venta: {AMARILLO}{oportunidad['venta']}{RESET} | "
            f"Ganancia: {VERDE_CLARO}{oportunidad['ganancia']}{RESET} | "
            f"Rentabilidad: {VERDE_CLARO}{oportunidad['rentabilidad']:.2f}%{RESET}"
        )


def main():
    oportunidades, ciudades_no_encontradas = calcular_mejores_items()
    imprimir_resultados(oportunidades, ciudades_no_encontradas)


if __name__ == "__main__":
    main()
