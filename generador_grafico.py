import matplotlib.pyplot as plt
import pandas as pd

class GeneradorGraficoJugador:
    def __init__ (self, archivo_csv = "proyectos propios/basicos de practica/jugadores/archivos app/lista de informes.csv"):
        self.archivo_csv = pd.read_csv(archivo_csv)
        self.columnas = list(self.archivo_csv.columns)
           
    def selccionar_columna(self):
        while True:
          for columna in (self.columnas): print(f"{columna}")
          columna_elegida = input("ingrese la columna que desea graficar:\n").capitalize()

          if not columna_elegida in self.columnas:
             print("ingrese una opcion valida")
          else:
             return columna_elegida
        
    def Graficos (self):
        while True:
         try:
          opcion_tipo_grafico = int(input("que tipo de grafico desea hacer?\n1.barras\n2.lineas"))
         except ValueError:
            print("ingrese un digito valido")
            continue
            
         if opcion_tipo_grafico == 1:
             plt.bar(self.archivo_csv["Nombre"] , self.archivo_csv[f"{self.selccionar_columna()}"])
             plt.title(f"INFORME")
             plt.xlabel("Nombres")
         elif opcion_tipo_grafico == 2:
            plt.plot(self.archivo_csv["Nombre"],self.archivo_csv[f"{self.selccionar_columna()}"],marker="o")
            plt.title(f"INFORME")
            plt.xlabel("Nombres")
         plt.show()
         

g = GeneradorGraficoJugador()
g.Graficos()


