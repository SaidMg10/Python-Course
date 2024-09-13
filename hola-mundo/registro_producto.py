lista_productos = []


while True :
    producto = input("ingresa el nombre del producto: (escriba 'echo' para terminar): ")
    if producto.lower() == 'echo' :
        break
    
    lista_productos.append(producto)

print("\nLista de productos")
for indice, valor in enumerate(lista_productos, start=1):
    print(f"{indice}. {valor}")