import os 
def créditoInterno():
    os.system("cls")
    #LUna pulpería vende al crédito solo a clientes registrados. 
    #Si lo están, revisa que su saldo pendiente no supere C$500. 
    #Diseña los mensajes para todos los casos.
    cliente = input("¿Esta usted registrado? (S/N): ").upper()
    if cliente == "S":
        saldopendiente = int(input("Ingrese su saldo pendiente"))
    
        if saldopendiente <= 500:
            print("Su saldo pendiente no supera los C$500!")
        else:
            print("Su saldo pendiente supera los C$500...")
    else:
        print("Lo sentimos... la pulpería solo le vende el crédito a los clientes registrados")


def servicioEntrega():
    #Un emprendimiento calcula una tarifa simulada según zona urbana o rural y, dentro
    #de cada zona, según si el paquete supera 5 kg. Propón tarifas y calcula el total..
    os.system("cls")
    zona = input("¿La zona en la que quiere realizar entrega es urbana o rural? ")
    if zona == "urbana":
        paquete = input("¿El paquete supera los 5kg? (S/N): ").upper()
        if paquete == "S":
            print("Su total será de: C$70")
        else:
            print("Su total será de: C$60")

    if zona == "rural":
        paquete = input("¿El paquete supera los 5kg?(S/N): ").upper()
        if paquete == "S":
            print("Su total será de: C$90")
        else:
            print("Su total será de: C$80")

def clasificaciónCafé():
    os.system("cls")
    print ("clasificación de Café")
    #Una cooperativa primero verifica si la humedad está entre 10% y 12%.
    #Si cumple, clasifica el lote según los defectos reportados. Propón categorías claras.
    humedad = input("¿La humedad está entre 10% y 12%?(S/N): ").upper()
    if humedad == "S":
        resultado = int(input("¿Cuantos defectos tiene?: "))
        if resultado <= 2:
            print("Perfecto")
        if 3 <= resultado <= 5:
            print("bueno")
        if resultado > 5:
            print("Regular")
    else:
        print("La humedad no está entre 10% y 12%.")
   

def reservaHospedaje():
    os.system("cls")
    print ("Reserva de hospedaje")
    #Un hospedaje de Granada ofrece una promoción simulada en temporada baja.
    #Dentro de esa temporada, el porcentaje depende de si la reserva alcanza 3 noches.
    temp = input ("¿Es temporada baja?(S/N): ").upper()
    if temp == "S":
        dias = int(input("¿Cuantos dias desea quedarse?:"))
        if dias <= 2:
            print("Lo sentimos, no aplica para la promoción...")
        if dias >= 3:
            print("¡Enhorabuena! ha aplicado para la promoción de un 20%")
    else: 
        print("Lo sentimos, no aplica para la promoción...")


def ventaFerreterías():
    os.system("cls")
    #Una ferretería distingue mayoristas y minoristas.
    #Para cada tipo, el descuento depende de un monto mínimo diferente.
    #Propón porcentajes y explica tus reglas.
    ferreteria = input("¿Su ferretería es mayorista o minorista? ")
    if ferreteria == "mayorista":
        montof = int(input("¿Cual es el monto que va a pagar? "))
        if  montof >= 5000:
            print("¡Enhorabuena! usted ha conseguido un descuento del 15%")
            print(f"El monto total es: {montof - (montof * 0.15)} ")
        else:
            print(f"El monto total es: {montof}  ")

    if  ferreteria == "minoristas":
        montof = int(input("¿Cual es el monto que va a pagar? "))
        if  montof >= 2000: 
            print ("¡Enhorabuena! usted ha conseguido un descuento del 5%")
            print(f"El monto total es: {montof - (montof * 0.05)} ")
        else:
            print(f"El monto total es: {montof}")