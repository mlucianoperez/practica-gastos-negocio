gastos_negocio = [
    {"descripcion": "Renta del local", "monto": 1500.00, "categoria": "Renta"},
    {"descripcion": "Compra de insumos", "monto": 3500.00, "categoria": "Insumos"},
    {"descripcion": "Publicidad en redes", "monto": 1200.00, "categoria": "Marketing"},
]


def agregar_gasto(gastos, descripcion, monto, categoria):
    nuevo_gasto = {
        "descripcion": descripcion,
        "monto": monto,
        "categoria": categoria
    }

    gastos.append(nuevo_gasto)

    return nuevo_gasto


def buscar_por_categoria(gastos, categoria_buscada):
    resultado = []

    for gasto in gastos:
        if gasto["categoria"].lower() == categoria_buscada.lower():
            resultado.append(gasto)

    return resultado


def total_por_categoria(gastos, categoria_buscada):
    total = 0
    for gasto in gastos:
        if gasto["categoria"].lower() == categoria_buscada.lower():
            total += gasto["monto"]
    return total


def ver_gastos(gastos):
    for gasto in gastos:
        print(
            f"{gasto['descripcion']} "
            f"({gasto['categoria']}): "
            f"${gasto['monto']}"
        )


ver_gastos(gastos_negocio)

agregar_gasto(
    gastos_negocio,
    "Compra de tijeras",
    800.00,
    "Insumos"
)

ver_gastos(gastos_negocio)

print(buscar_por_categoria(gastos_negocio, "INSUMOS"))
print(total_por_categoria(gastos_negocio, "insumos"))


while True:
    print("1. Ver todos los gastos")
    print("0. Salir")
    opcion = input("Elige una opción: ")

    if opcion == "1":
        ver_gastos(gastos_negocio)
    elif opcion == "0":
        print("Hasta luego")
        break



