import os
os.system("cls")

def inventarioPulpería():
    #La pulpería La Esquina necesita reponer un producto cuando quedan menos de 5 unidades. 
    # Solicita el nombre y la existencia; muestra una alerta cuando corresponda.
    os.system("cls")
    print("********** PULPERÍA LA ESQUINA **********")
    nombreproducto = input("Ingresa el nombre del producto: ")
    cantidadproducto = int(input("Ingresa la cantidad del producto"))
    if cantidadproducto < 5:
        print("¡QUEDAN MENOS DE 5 UNIDADES! Es hora de reponer el producto...")
    else: 
        print("¡Perfecto! no es necesario reponer el producto...")
    


def promociónTienda():
    print("promociónTienda")
    os.system("cls")
    #Una tienda de Masaya aplica una promoción simulada de 10% cuando la compra supera C$1,500. 
    # Solicita el monto y muestra el total.
    monto = int(input("Ingresa el monto: "))
    if monto > 1500:
        print (f"El monto total es igual a: {monto} y con 10% de descuento incluido es igual a {monto - (monto * 0.10)}" )
    else:
        print(f"El monto total es igual a: {monto}" )



def metaVentas():
    os.system("cls")
    #Un emprendimiento fija una meta diaria de C$4,000. 
    # Lee el total vendido e informa si se alcanzó; muestra cuánto faltó o cuánto se superó.
    meta = int(input("Ingresa el total ganado hoy: "))
    if meta == 4000:
        print (f"¡Enhorabuena! has conseguido la meta, sigue así")
    if meta < 4000:
        print(f"Uhhh... faltaron {4000 - meta} córdobas, buena suerte la próxima...")


    if meta > 4000:
        print(f"¡Enhorabuena! has superado la meta por {meta - 4000} córdobas, sigue así")

def entregaComedor():
    os.system("cls")
    #Un comedor realiza entrega sin recargo desde C$300. 
    # Indica si la entrega es gratuita o suma un recargo simulado de C$40.
    entregaprecio = int(input("Por favor ingrese el monto de su compra: "))
    if entregaprecio >= 300:
        print("¡La entrega será gratuitua!")
    else:
        print(f"El total será de: {entregaprecio + 40} córdobas, pues la entrega cuesta 40 córdobas")

def pesoProductos():
    os.system("cls")
    #Una bodega espera sacos de 46 kg. 
    # Lee el peso e informa si cumple o debe revisarse por estar debajo del valor esperado.
    pesosacos = int(input("Ingrese el peso del saco: "))
    if pesosacos == 46: 
        print("¡El peso del saco es el adecuado!")
    else:
        print("¡Oops! El peso del saco no el adecuado, por favor revisalo")