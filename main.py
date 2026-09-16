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



