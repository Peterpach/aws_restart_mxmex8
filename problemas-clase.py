# PROBLEMA 1

# Solicitar Kilometros recorridos
km = float(input("Ingrese el número de kilometros recorridos: "))
# Solicitar cantidad de combustible
combustible = float(input("Ingrese la cantidad de combustible gastado: "))

# Calcular el consumo por kilometro si los valores son mayores a 0
if km > 0 and combustible >0:
    consumo = km / combustible
    print(f"El consumo por kilometros es de: {consumo}")
else:
    print("Ingrese un valor mayor a 0")


# PROBLEMA 5

# Solicitar el precio del producto
precioProducto = float(input("Ingrese el precio del producto: "))

# Calcular el precio total del producto
if precioProducto > 0:
    descuento = precioProducto * 0.15
    total = precioProducto - descuento
    print(f"El precio total es de: {total}")
else:
    print("Ingrese un valor mayor a 0")