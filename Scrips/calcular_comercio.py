"""Compara precios de compra entre ciudades para encontrar oportunidades."""

import json
from pathlib import Path


RAIZ_PROYECTO = Path(__file__).resolve().parent.parent
NOMBRE_ARCHIVO = "Comercio.json"


def cargar_precios():
    """Carga los precios de cada carpeta de ciudad."""
    precios_por_item = {}

    for carpeta in RAIZ_PROYECTO.iterdir():
        archivo = carpeta / NOMBRE_ARCHIVO
        if not carpeta.is_dir() or not archivo.is_file():
            continue

        with archivo.open(encoding="utf-8") as contenido:
            items = json.load(contenido).get("Items", [])

        for item in items:
            nombre = item.get("Item")
            compra = item.get("Si_Compro", 0)

            if not nombre:
                continue

            precios_por_item.setdefault(nombre, []).append(
                {
                    "ciudad": carpeta.name,
                    "compra": compra,
                }
            )

    return precios_por_item


def calcular_oportunidades(precios_por_item):
    """Devuelve rutas rentables usando Si_Compro al comprar y al vender.

    Al revender un item se usa el precio de compra de la ciudad destino:
    es el valor que otra persona paga por comprar ese item alli. Si_Vendo
    representa una venta directa y no se utiliza en este calculo.
    """
    oportunidades = []

    for nombre, precios in precios_por_item.items():
        precios_validos = [precio for precio in precios if precio["compra"] > 0]

        for origen in precios_validos:
            for destino in precios_validos:
                ganancia = destino["compra"] - origen["compra"]
                if origen["ciudad"] != destino["ciudad"] and ganancia > 0:
                    oportunidades.append(
                        {
                            "item": nombre,
                            "origen": origen["ciudad"],
                            "destino": destino["ciudad"],
                            "costo": origen["compra"],
                            "venta": destino["compra"],
                            "ganancia": ganancia,
                            "rentabilidad": ganancia / origen["compra"] * 100,
                        }
                    )

    return sorted(
        oportunidades,
        key=lambda oportunidad: oportunidad["rentabilidad"],
        reverse=True,
    )


def main():
    oportunidades = calcular_oportunidades(cargar_precios())

    if not oportunidades:
        print("No hay oportunidades rentables con los precios disponibles.")
        return

    for oportunidad in oportunidades:
        print(
            f"{oportunidad['item']}: comprar en {oportunidad['origen']} por "
            f"{oportunidad['costo']} y vender en {oportunidad['destino']} por "
            f"{oportunidad['venta']} | Ganancia: {oportunidad['ganancia']} "
            f"| Rentabilidad: {oportunidad['rentabilidad']:.2f}%"
        )


if __name__ == "__main__":
    main()
