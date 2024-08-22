def conversion(numero, base_numero,base_solicitada):
    numero_decimal = conversion_decimal(numero,base_numero)
    numero_convertido = conversion_decimal_a_solicitada(numero_decimal,base_solicitada)
    return numero_convertido

def conversion_decimal(numero,base):
    #DIVIDIMOS Y GUARDAMOS EN UNA LISTA DE 2 ELEMENTOS LA PARTE ENTERA Y LA PARTE FLOTANTE
    numero_dividido = numero.split(".")
    
    #SEPARAMOS CADA PARTE Y REALIZAMOS LA CONVERSIÓN

    #LA CLASE INT CONVIERTE UN NUMERO ENTERO A UNA BASE CUALESQUIERA
    parte_entera = int(numero_dividido[0],base)
    #SI NO TIENE PARTE FLOTANTE:
    if len(numero_dividido)==1:
        return parte_entera
    #SI TIENE PARTE FLOTANTE:
    else:
        #PARA LOS FLOTANTES APLICAREMOS EL ALGORITMO DE CLASE
        parte_flotante = numero_dividido[1]
        j=-1 #POSICION INICIAL DEL DIGITO EN EL ALGORITMO PARA DECIMALES
        parte_flotante_decimal = [] #LISTA QUE ALMACENA LOS RESULTADOS DEL ALGORITMO
        for digito in parte_flotante: 
            valor_letra = int(digito,base) #SI SE TRATA DE UN NUMERO DE BASE >10, SE CONVIERTEN LAS LETRAS (A:F)
            parte_flotante_decimal.append(valor_letra*(base**j)) #ALGORITMO
            j-=1

        parte_flotante = sum(parte_flotante_decimal) #SUMAMOS LOS RESULTADOS PARA OBTENER LA PARTE FLOTANTE
        return parte_entera+parte_flotante #NUMERO EN BASE DECIMAL SOLICITADO
    

def conversion_decimal_a_solicitada(numero,base):
    #SI LA BASE SOLICITADA ES 10 NO TIENE CASO HACER EL PROCESO
    if(base==10):
        return(numero)
    else:
        #LA CLASE INT SI EL NUMERO TIENE PARTE FLOTANTE LO DELIMITA A SU ENTERO
        parte_entera = int(numero)
        #OBTENEMOS LA PARTE FLOTANTE
        parte_flotante = numero - parte_entera



#MAIN
print("----- CONVERSOR BASES NÚMERICAS -----\n")
base_numero = int(input("Ingresa la base del número: "))
numero = input("Ingresa el número: ")
base_solicitada = int(input("Ingresa la base de conversión: "))

numero_convertido = conversion(numero, base_numero,base_solicitada)
print("\n______________________________")
print("Número dado: " +numero+ "\nNúmero en base " +str(base_solicitada)+ ": " +str(numero_convertido))
