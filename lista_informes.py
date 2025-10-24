
import pandas as pd
import csv
from modulo_rendimiento.informes import Informe
import time
import datetime
class ListaRendimientos():
    def __init__(self,lista_informes="proyectos propios/basicos de practica/jugadores/archivos app/lista de informes.csv"):
        self.lista_informes = lista_informes
        self.rendimento = []
        self.Cargar_informes()

    def Cargar_informes (self):
        try:
            with open(self.lista_informes, "r") as archivo_csv:
                lector = csv.reader(archivo_csv)
                next(lector)
                for fila in lector:
                    if len(fila) == 10:
                        nombre,pocision,remate,bloqueo,saque,cobertura,recepcion,colocacion,fallos,fecha = fila
                        informe = Informe(nombre,pocision,int(remate),int(bloqueo),int(saque),int(cobertura),int(recepcion),int(colocacion),int(fallos))
                        informe.fecha = datetime.datetime.strptime(fecha, "%Y-%m-%d").date()
                        self.rendimento.append(informe)
                file_path="proyectos propios/basicos de practica/jugadores/archivos app/jugadores.xlsx"
                excel = pd.DataFrame([vars(informe) for informe in self.rendimento])
                excel.to_excel(file_path,index=False)
        except FileNotFoundError:
            print(f"el archivo {self.lista_informes} no se encontro")
    def guardar_jugadores (self):
        with open(self.lista_informes,"w",newline="") as archivo_csv:
         escritor=csv.writer(archivo_csv)
         escritor.writerow(["Nombre","Pocision","Remate","Bloqueo","Saque","Cobertura","Recepcion","Colocacion","Fallos","Fecha"])
         for informe in self.rendimento:
             escritor.writerow([informe.nombre,informe.posicion,informe.remate,informe.bloqueo,
                                informe.saque,informe.cobertura,informe.recepcion,informe.colocacion,
                                informe.fallos,informe.fecha])
    def subir_informe(self,informe):
        self.rendimento.append(informe)
        self.guardar_jugadores()
    def mostrar_reporte(self):
        with open (self.lista_informes,"r") as archivo_csv:
         df = pd.DataFrame(archivo_csv)
         print(df)

    def borrar_informe(self,informe_borrar,fecha_informe):
        try:
              fecha = datetime.datetime.strptime(fecha_informe, "%Y-%m-%d").date()
        except ValueError:
               print("Formato de fecha incorrecto. Usa AAAA-MM-DD.")
               return
        for informe in self.rendimento:
            if informe.nombre == informe_borrar and informe.fecha == fecha:
                self.rendimento.remove(informe)
                print(f"El informe del dia {informe.fecha} \n del jugador {informe.nombre} ha sido eliminado.")
                return
        print("ese nombre no esta en los registros")