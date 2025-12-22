import os
import pickle

def borra_la_pantalla():
    os.system("cls")

def escoger_una_opcion(max:int, min:int):
    try:
        opcion = int(input("\t"))
    except:
        print("\t\033[4;31mOPCION INVALIDA\033[0m")
        escoger_una_opcion(max,min)

    if ((opcion < min) or (opcion > max)):
        print("\t\033[4;31mOPCION INVALIDA\033[0m")
        escoger_una_opcion(max, min)

    
    return opcion

def merge_sort(lista, opcion:int):
    if len(lista) <= 1:
        return lista

    mid = len(lista) // 2
    left_part = merge_sort(lista[:mid], opcion)
    right_part = merge_sort(lista[mid:], opcion)

    lista_final = []
    i = 0
    k = 0
    while i < len(left_part) and k < len(right_part):
        if left_part[i][opcion] <= right_part[k][opcion]:
            lista_final.append(left_part[i])
            i += 1
        else:
            lista_final.append(right_part[k])
            k += 1

    while i < len(left_part):
        lista_final.append(left_part[i])
        i += 1

    while k < len(right_part):
        lista_final.append(right_part[k])
        k += 1

    return(lista_final)



def imprimir_inventario():
    print("\t\033[4;31mIMPRIMIR EL INVENTARIO\033[0m")
    print("\t\033[4;31mOPCION 1\033[0m LISTA ORDENADA POR CODIGO DEL PRODUCTO");
    print("\t\033[4;31mOPCION 2\033[0m LISTA ORDENADA POR NOMBRE DEL PRODUCTO");
    opcion = (escoger_una_opcion(2, 1)) -1

    borra_la_pantalla()
    print("\a")

    
    inventario = "inventario_productos.bin"

    with open(inventario, "rb") as productos:
        lista = pickle.load(productos)
        resultado = (merge_sort(lista, opcion))

    for every in resultado:
        print("\n")
        print (f"\tCODIGO: {every[0]}")
        print (f"\tNOMBRE: {every[1]}")
        print (f"\tPRECIO: {every[2]}")
        if every[3] > 0:
            print (f"\tCANTIDAD DISPONIBLE: {every[0]}")

        else: 
            print("\tPRODUCTO NO DISPONIBLE")



def buscar_producto():
    print("\t\033[4;31mBUSCAR UN PRODUCTO ESPECIFICO\033[0m")
    print("\t\033[4;31mOPCION 1\033[0m BUSCAR POR EL CODIGO DEL PRODUCTO");
    print("\t\033[4;31mOPCION 2\033[0m BUSCAR POR EL NOMBRE DEL PRODUCTO");
    opcion = (escoger_una_opcion(2, 1)) -1

    borra_la_pantalla()
    print("\a")

    
    inventario = "inventario_productos.bin"

    with open(inventario, "rb") as productos:
        lista = pickle.load(productos)

def agregar_producto():
    print("\tAGREGANDO UN PRODUCTO AL INVENTARIO")

def egresar_producto():
    print("\tEGRESANDO UN PRODUCTO DEL INVENTARIO")

def modificar_producto():
    print("\tMODIFICANDO UN PRODUCTO DEL INVENTARIO")


def main():
    opcion:int =0;
    print("\t\033[4;31mBIENVENIDO\033[0m");
    print("\t\033[4;31mQUE DECEA HACER?\033[0m");
    print("\t\033[4;31mOPCION 1\033[0m IMPRIMIR EL INVETARIO");
    print("\t\033[4;31mOPCION 2\033[0m BUSCAR UN PRODCTO ESPECIFICO");
    print("\t\033[4;31mOPCION 3\033[0m AGREGAR UN PRODUCTO AL INVENTARIO");
    print("\t\033[4;31mOPCION 4\033[0m EGRESAR UN PRODUCTO DEL INVENTARIO");
    print("\t\033[4;31mOPCION 5\033[0m MODIFICAR UN PRODUCTO DEL INVENTARIO");
    print("\t\033[4;31mELIJA UNA OPCION\033[0m");
    opcion = escoger_una_opcion(5, 1)
    
    borra_la_pantalla()
    
    inventario = "inventario_productos.bin"
    productos = [
    [1, 'pollo', 15, 33],
    [2, 'camaron', 25, 45],
    [3, 'pablo', 3, 1]
    ]
    with open(inventario, 'wb') as file:
        pickle.dump(productos, file)

    match (opcion):
        case 1:
            imprimir_inventario()
        case 2:
            buscar_producto()
        case 3:
            agregar_producto()
        case 4:
            egresar_producto()
        case 5:
            modificar_producto()

        

if (__name__ == "__main__"):
    main()
