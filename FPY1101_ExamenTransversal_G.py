prendas = {
    'S001': ['Polera Basica', 'polera', 'M', 'negro', 'algodon', True],
    'S002': ['Jeans Slim', 'pantalon', 'L', 'azul', 'denim', False],
    'S003': ['Chaqueta Urban', 'chaqueta', 'M', 'gris', 'poliester', True],
    'S004': ['Vestido Sol', 'vestido', 'S', 'rojo', 'lino', False],
    'S005': ['Poleron Cozy', 'poleron', 'XL', 'verde', 'algodon', True],
    'S006': ['Camisa Formal', 'camisa', 'M', 'blanco', 'algodon', False],
}

bodega = {
    'S001': [7990, 12],
    'S002': [19990, 0],
    'S003': [29990, 3],
    'S004': [24990, 6],
    'S005': [17990, 8],
    'S006': [14990, 2],
}

def validar_campo_texto(campo):
    return campo.strip() != ""

def unidades_categoria(categoria):
    categoria = categoria.strip() .lower()
    total=0
    
    for codigo,datos in prendas.items():
        if datos[1].lower() == categoria:
            total += bodega[codigo][1]
            
    print(f"El total de unidades disponibles es: {total}")            
    
def busqueda_rango_precio(precio_min, precio_max):
    
    encontrados = []
    
    for codigo, datos in bodega.items():
        
        precio = datos[0]
        unidades = datos[1]
        
        if precio_min <= precio <= precio_max and unidades != 0:
            nombre = prendas[codigo][0]
            encontrados.append(f"{nombre}--{codigo}")
            
    encontrados.sort()
    
    if encontrados:
        print("Las prendas encontradas son:")
        print(encontrados)
    else:
        print("No hay prendas en ese rango de precios.")
        
def actualizar_precio(codigo, nuevo_precio):
    
    codigo = codigo.strip().upper()        
    
    if codigo not in bodega:
        return False
    bodega[codigo][0] = nuevo_precio
    return True

def agregar_prenda():
    
    codigo= input("Ingrese el código de la prenda: ").strip().upper()
    if codigo == "":
        print("El código no puede estar vacío.")
        return
    
    if codigo in prendas:
        print("El código ya existe. No se puede agregar la prenda.")
        return
    
    nombre = input("Ingrese el nombre de la prenda: ").strip()
    if not validar_campo_texto(nombre):
        print("El nombre no puede estar vacío.")
        return
    
    categoria = input("Ingrese la categoría de la prenda: ").strip()
    if not validar_campo_texto(categoria):
        print("La categoría no puede estar vacía.")
        return  
    
    talla=input("Ingrese la talla de la prenda: ").strip()
    if not validar_campo_texto(talla):
        print("Talla invalida.")
        
    color= input("Ingrese el color de la prenda: ").strip()
    if not validar_campo_texto(color):
        print("Color invalido.")
        return  
    
    material= input("Ingrese el material de la prenda: ").strip()
    if not validar_campo_texto(material):
        print("Material invalido.")
        return  
    
    unisex= input("Ingrese si la prenda es unisex (s/n): ").lower()
    if unisex not in ("s", "n"):
        print("Valor invalido para unisex.")
        return  
    
    es_unisex = True if unisex == "s" else False
    
    try:
        precio = int(input("Ingrese el precio de la prenda: "))
        if precio <= 0:
            print("El precio debe ser un número entero mayor que cero.")
            return
    except ValueError:
        print("Precio inválido.")
        return
    
    try:
        unidades = int(input("Ingrese la cantidad de unidades: "))
        if unidades < 0:
            print("La cantidad de unidades no puede ser negativa.")
            return
    except ValueError:
        print("Cantidad de unidades inválida.")
        return
    
    prendas[codigo] = [nombre, categoria, talla, color, material, es_unisex]
    bodega[codigo] = [precio, unidades] 
    
    print(f"Prenda {codigo} agregada exitosamente con {unidades} unidades a un precio de {precio}.") 
    
    
def eliminar_prenda(codigo):
    
    codigo = codigo.strip().upper()
    
    if codigo not in prendas:
        print("El código no existe. No se puede eliminar la prenda.")
        return False
    
    del prendas[codigo]
    del bodega[codigo]
    
    print(f"Prenda {codigo} eliminada exitosamente.")
    return True 

def menu():
    while True:
        
        print("\n=====MENU PRINCIPAL=====")
        print("1. Unidades por categoría")
        print("2. Búsqueda de prendas por rango de precio")
        print("3. Actualizar precio de prenda")
        print("4. Agregar prenda")
        print("5. Eliminar prenda")
        print("6. Salir")
        print("=====================================")
        
        opcion = input("Seleccione una opción: ").strip()
        if opcion == '1':
            categoria = input("Ingrese categoría: ")
            unidades_categoria(categoria)
            
        elif opcion == '2':
            try:
                precio_min = int(input("Ingrese precio mínimo: "))
                precio_max = int(input("Ingrese precio máximo: "))
                if precio_min > precio_max:
                    print("El precio mínimo no puede ser mayor que el máximo.")
                    continue
                
            except ValueError:
                print("Debe ingresar un numero entero.")
                continue
                
            busqueda_rango_precio(precio_min, precio_max) 
            
        elif opcion == '3':
            
            while True:

                codigo = input("Ingrese código de prenda: ").upper()

                try:
                    nuevo_precio = int(input("Ingrese nuevo precio: "))

                    if nuevo_precio <= 0:
                        print("Debe ingresar un precio mayor que cero.")
                        continue

                except ValueError:
                    print("Debe ingresar un número entero.")
                    continue

                if actualizar_precio(codigo, nuevo_precio):
                    print(f"Precio de la prenda {codigo} actualizado a {nuevo_precio}.")
                else:
                    print(f"No se encontró la prenda con código {codigo}.")
                    
                seguir = input("¿Desea actualizar otro precio (s/n)? ").lower()
                if seguir == "n":
                    break
                
        elif opcion == '4':
            agregar_prenda()    
            
        elif opcion == '5':
            codigo = input("Ingrese el código de la prenda a eliminar: ").strip().upper()
            if eliminar_prenda(codigo):
                print("La prenda ha sido eliminada exitosamente.")
            else:
                print("No se pudo eliminar la prenda. Verifique el código ingresado.")
                
        elif opcion == '6':
            print("Programa finalizado.")
            break     
        
        else:
            print("Opción inválida. Por favor, seleccione una opción válida del menú.")
            
menu()        
            
            
                
                
        
    