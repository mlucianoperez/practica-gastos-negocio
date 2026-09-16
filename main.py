gastos_negocio = [
    {"descripcion": "Renta del local", "monto": 1500.00, "categoria": "Renta"},
    {"descripcion": "Compra de insumos", "monto": 3500.00, "categoria": "Insumos"},
    {"descripcion": "Publicidad en redes", "monto": 1200.00, "categoria": "Marketing"},
]


class GestorGastos:
    def __init__(self, gastos):
        self.gastos = gastos

    def agregar_gasto(self, descripcion, monto, categoria):
        try:
            monto = float(monto)
        except ValueError:
            print("El monto debe ser un número. Gasto no agregado.")
            return None

        nuevo_gasto = {
            "descripcion": descripcion,
            "monto": monto,
            "categoria": categoria
        }

        self.gastos.append(nuevo_gasto)

        return nuevo_gasto

    def buscar_por_categoria(self, categoria_buscada):
        resultado = []

        for gasto in self.gastos:
            if gasto["categoria"].lower() == categoria_buscada.lower():
                resultado.append(gasto)

        return resultado

    def total_por_categoria(self, categoria_buscada):
        total = 0
        for gasto in self.gastos:
            if gasto["categoria"].lower() == categoria_buscada.lower():
                total += gasto["monto"]
        return total

    def ver_gastos(self):
        for gasto in self.gastos:
            print(
                f"{gasto['descripcion']} "
                f"({gasto['categoria']}): "
                f"${gasto['monto']}"
            )


gestor = GestorGastos(gastos_negocio)


gestor.ver_gastos()

gestor.agregar_gasto(
    "Compra de tijeras",
    "800.00",
    "Insumos"
)

gestor.ver_gastos()




while True:
    print("4. Ver el total gastado en una categoria")
    print("3. Buscar gastos por categoria")
    print("2. Agregar un gasto nuevo")
    print("1. Ver todos los gastos")
    print("0. Salir")
    opcion = input("Elige una opción: ")

    if opcion == "4":
        categoria_buscada = input("Categoría: ")
        total = gestor.total_por_categoria(categoria_buscada)
        print(f"Total gastado: ${total:.2f}")
    elif opcion == "3":
        categoria_buscada = input("Categoría: ")
        resultados = gestor.buscar_por_categoria(categoria_buscada)
        for gasto in resultados:
            print(gasto)
    elif opcion == "2":
        descripcion = input("Descripción: ")
        monto = input("Monto: ")
        categoria = input("Categoría: ")
        gestor.agregar_gasto(descripcion, monto, categoria)
    elif opcion == "1":
        gestor.ver_gastos()
    elif opcion == "0":
        print("Hasta luego")
        break



