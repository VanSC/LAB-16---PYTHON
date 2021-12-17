import libreria

while True:
    print("-----Menu de opciones-----")
    print("1. Registrar")
    print("2. Reporte")
    print("3. Salir")

    opcion = input("Ingrese una opcion: ")

    if opcion == "1":
        print("********Registro********")
        nombres = input("Ingrese nombres: ")
        apellidos = input("Ingrese apellidos: ")
        sueldo_hora = int(input("Ingrese sueldo por hora: "))
        horas_trabajadas = int(input("Ingrese horas trabajadas: "))
        tipo = input("Ingrese tipo de empleado: ")

        libreria.registrar_nuevo_empleado(
            nombres, apellidos, sueldo_hora, horas_trabajadas, tipo)

    if opcion == "2":
        print("*****Reporte*****")
        libreria.reporte()
        
    if opcion == "3":
        chose = input("¿Quieres finalalizar el registro? S/N: ")
        if chose == "S":
            print("Hasta Luego :)")
            break
        else:
            print(opcion == "1")

            
