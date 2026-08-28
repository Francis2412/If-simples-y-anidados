import os 
from Simples import inventarioPulpería, promociónTienda, metaVentas, entregaComedor, pesoProductos
from Anidadas import créditoInterno, servicioEntrega, clasificaciónCafé, reservaHospedaje, ventaFerreterías
def main():
    os.system("cls")
    print("*********🌸 CATÁLOGO DE FUNCIONES 🌸*********")
    print("***************** If Simples *****************")
    print("1...................Inventario de una pulpería")
    print("2......................Promoción de una tienda")
    print("3...............................Meta de ventas")
    print("4........................Entrega de un comedor")
    print("5............................Peso de productos")
    print("***************** If Anidados ****************")
    print("6..............................Crédito interno")
    print("7..........................Servicio de entrega")
    print("8........................Clasificación de café")
    print("9.........................Reserva de hospedaje")
    print("10........................Venta de ferreterías")
    print("**********************************************")
    opc= int(input("Seleccione la tarea a ejecutarse: "))
    match opc:
        case 1:
            inventarioPulpería()
            
        case 2:
            promociónTienda()

        case 3:
            metaVentas()
        case 4:
            entregaComedor()
        case 5:
            pesoProductos()
        case 6:
            créditoInterno()
        case 7:
            servicioEntrega()
        case 8:
            clasificaciónCafé()
        case 9:
            reservaHospedaje()
        case 10:
            ventaFerreterías()

main()