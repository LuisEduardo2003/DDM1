

def main():
  print("--- Programa de conversión de Sistemas Numéricos ---\n")
  print("Inserte la base del sistema numérico que desea convertir: ")
  base = int(input())

  print("----- Considere solo la parte ENTERA -----")
  print("Inserte un 0 si no contiene parte entera")
  num_digitos_entera = int(input("\n¿Cuántos digitos contiene la cantidad a covertir? \n"))

  print("----- Considere solo la parte DECIMAL -----")
  print("Inserte un 0 si no contiene parte decimal")
  num_digitos_decimal = int(input("\n¿Cuántos digitos contiene la cantidad a covertir? \n"))
  
  cantidad_entera = []
  cantidad_decimal = []

  if(num_digitos_entera != 0):
    for i in range(num_digitos_entera):
      valor = input(f"\nIntroduce el valor para el digito {i+1} de la parte ENTERA:")
      cantidad_entera.append(valor)

  print("La cantidad a covertir ENTERA es:", cantidad_entera)

  if(num_digitos_decimal != 0):
    for i in range(num_digitos_decimal):
      valor = input(f"\nIntroduce el valor para el digito {i+1} de la parte DECIMAL:")
      cantidad_decimal.append(valor)

  print("La cantidad a covertir DECIMAL es:", cantidad_decimal)

  
  Xsistema_decimal(base, cantidad_entera, cantidad_decimal)
  
  # print("Inserte la base del sistema al cual desea convertir: ")
  #salida = int(input()) 
 
  return

def Xsistema_decimal(base, cantidad_entera, cantidad_decimal):
  # ----- PARTE ENTERA -----
  longitud_lista = len(cantidad_entera)
  copia_lista_entera =[]
  for digito in cantidad_entera:
    digito = int(digito) #Se hace una coversión a entero
    copia_lista_entera.append(digito * (base**(longitud_lista-1)))
    longitud_lista -=1
  
  suma_total_entera = sum(copia_lista_entera)

  # ----- PARTE DECIMAL -----
  #longitud_lista = len(cantidad_decimal)
  copia_lista_decimal =[]
  exponente = -1
  for digito in cantidad_decimal:
    digito = int(digito) #Se hace una coversión a entero
    copia_lista_decimal.append(digito * (base**(exponente)))
    exponente -=1

  suma_total_decimal = sum(copia_lista_decimal)

  # SUMA FINAL
  suma_total_entera = str(suma_total_entera) #Conversiíon a cadena
  suma_total_decimal = str(suma_total_decimal)
  print("La cantidad en sistema decimal es: " + suma_total_entera + " ENTERA y " + suma_total_decimal + " DECIMAL") 

  return

main()
