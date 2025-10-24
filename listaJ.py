import csv
from modulo_jugadores.player import Integrante
class ListaJugadores():
    def __init__(self,lista_de_jugadores="proyectos propios/basicos de practica/jugadores/archivos app/lista de jugadores.csv"):
        self.lista_jugadores = lista_de_jugadores
        self.jugadores = []
        self.cargar_Jugadores()

    def cargar_Jugadores(self):
        try:
            with open(self.lista_jugadores, "r") as archivo_csv:
                lector = csv.reader(archivo_csv)
                next(lector)
                for fila in lector:
                    if len(fila) == 4:
                        nombre, edad, altura, pocision = fila
                        jugador = Integrante(nombre, int(edad), float(altura), pocision)
                        self.jugadores.append(jugador)
        except FileNotFoundError:
            print(f"El archivo {self.lista_jugadores} no se encontro.")
    def guardar_Jugadores(self):
        with open(self.lista_jugadores,"w",newline="") as archivo_csv:
            escritor=csv.writer(archivo_csv)
            escritor.writerow(["Nombre","Edad","Altura","Pocision"])
            for jugador in self.jugadores:
                escritor.writerow([jugador.nombre,jugador.edad,jugador.altura,jugador.pocision])
    def agregar_Jugador(self,jugador):
        self.jugadores.append(jugador)
        self.guardar_Jugadores()


    def mostrar_Jugadores(self):
        if not self.jugadores:
            print("No hay jugadores en la lista.")
            return
        for jugador in self.jugadores:
            jugador.mostrar_datos()
            print("-----")
    def borrar_Jugador(self,nombre_borrar):
        for jugador in self.jugadores:
            if jugador.nombre == nombre_borrar:
                self.jugadores.remove(jugador)
                self.guardar_Jugadores()
            print(f"El jugador {jugador.nombre} ha sido eliminado.")
            return

