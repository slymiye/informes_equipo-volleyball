import time as tm

class Menu():
    def mostrar_Opciones_lista(self):
        print("BIENVENIDO\nque desea administrar\n1.listas de jugador\n2." \
        "listas de rendimiento\n3. SALIR")
        try:
            opcion=int(input("Seleccione una opción: "))
            return opcion

        except ValueError :
            print("\n" \
            "dato invalido por favor ingrese un numero mostrado")
            tm.sleep(4)
        

    def mostrar_Opciones_jugador(self):
        print("1. Agregar jugador\n2. Mostrar jugadores" \
        "\n3. Borrar jugador\n4. volver")
        try:
            opcion = int(input("Seleccione una opción: "))
            return opcion

        except ValueError :
            print("\n" \
            "dato invalido por favor ingrese un numero mostrado")
            tm.sleep(4)
    def mostrar_Opciones_informe(self):
        print("1. Agregar informe\n2. Mostrar informes" \
        "\n3. Borrar informe\n4. Salir")
        try:
            opcion = int(input("Seleccione una opción: "))
            return opcion
        except ValueError :
            print("\n" \
            "dato invalido por favor ingrese uno de los numeros mostrado")
            tm.sleep(4)
    
    def mostrar_Opciones(self):
        print("1.jugadores \n2.equipo\n3.salir")
        try:
            opcion = int(input("Seleccione una opción: "))
            return opcion
        except ValueError :
            print("\n" \
            "dato invalido por favor ingrese uno de los numeros mostrado")
            tm.sleep(4)
