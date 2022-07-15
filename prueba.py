lista = [["Leonel", 2, 2,2],["Belen", 1,1,1],["aa", 5,6,7]]

def buscar_vendedor(lista,nombre):
    for i in lista:
        if i[0] == nombre:
         print(i,end= " ")

def listado_vendedor(lista):
    lista2 = []
    for i in lista:
        print(i, end= "")
        print("\n")
    print("ingrese un nuevo vendedor")
    nombre = input()
    lista2.append(nombre)
    for item in range(3):
        print("ingrese venta del dia "+ str(item+1))
        nota= int(input())
        lista2.append(nota)
    lista.append(lista2)
    return lista

def listado_ventas(listado):
    for vendedor in listado:
        posicion = 0
        total = 0
        ventas_dia = 0
        for datos in vendedor:
            if posicion != 0:
                ventas_dia = ventas_dia +datos * 200
                #print(ventas_dia)
            posicion+=1
        total = ventas_dia + 10000
        print("las ventas del vendedor  incluido el sueldo base es de " + str(total))
    return datos

def ventas(lista):
    for vendedor  in lista:
        ventas_dia = 0
        posicion = 0
        total = 0
        for datos in vendedor:
            if posicion != 0:
                ventas_dia = ventas_dia +datos * 200
            posicion+=1
        total = ventas_dia + 10000
        if total > 999999999 :
            print(datos, end=" ")
    print("el de menor ventas es "+ vendedor[0])
    return datos





print("1. Agregar vendedor")
print("2. Calcular sueldo de vendedor")
print("3. Mostar datos de un vendedor")
print("4. Mostrar vendedor con menos ventas")

print("Ingrese una opcion: ")
opcion = int(input())

while opcion != 0:
    if opcion == 1:
        valor = listado_vendedor(lista)
        print("lista actualizada: "+ str(valor))
    
    elif opcion == 2:
        valor = listado_ventas(lista)
    
    elif opcion == 3:
        print("Ingrese vendedor a buscar? ")
        nombre = input()
        buscador = buscar_vendedor(lista,nombre)
    
    elif opcion == 4:
        valor = ventas(lista)
        
    else:
        print("opcion invalida")
    print("\n") 
    print("1. Agregar vendedor")
    print("2. Calcular sueldo de vendedor")
    print("3. Mostrar datos de un vendedor")
    print("4. Mostrar vendedor con menos ventas")

    print("Ingrese una opcion")
    opcion= int(input())
    



