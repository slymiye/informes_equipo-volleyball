
def main():
 from numero import pedir_numero
 from modulo_jugadores import listaJ
 from modulo_jugadores import player
 from modulo_rendimiento import informes,lista_informes
 import menu
 import os

 players = player
 lista=listaJ.ListaJugadores()
 lista_reporte=lista_informes.ListaRendimientos()
 interfaz = menu.Menu()
 reporte=informes 
 while True :
      print("\nMENU PRINCIPAL\n")
      opcion_inicial=interfaz.mostrar_Opciones()
      os.system('clear')
      if opcion_inicial == 1:
       opcion_listas=interfaz.mostrar_Opciones_lista()
       os.system('clear')
       if opcion_listas== 1:
        while True:
         print("\nlista de jugadores\n")
         opcion_jugador=interfaz.mostrar_Opciones_jugador()

         if opcion_jugador ==1:
          jugador=players.Integrante(input("porfavor ingresar datos del jugador\n" \
          "nombre: "),pedir_numero("edad: "),pedir_numero("altura (cm): "),input("pocision: "))
          lista.agregar_Jugador(jugador)

         elif opcion_jugador==2:
          lista.mostrar_Jugadores() 

         elif opcion_jugador == 3:
          lista.borrar_Jugador(input("nombre:"))
         elif opcion_jugador == 4:
          break

       elif opcion_listas == 2:

        while True:
         print("\nlista de informes\n")
         opcion_informe=interfaz.mostrar_Opciones_informe()
         if opcion_informe ==1:
            informe=reporte.Informe(input("nombre: "),
                           input("posicion: "),
                           pedir_numero("remate: "),
                           pedir_numero("bloqueo: "),
                           pedir_numero("saque: "),
                           pedir_numero("cobertura: "),
                           pedir_numero("recepcion: "),
                           pedir_numero("colocacion: "),
                           pedir_numero("fallos: "))
            informe.ajustar_posicion()
            lista_reporte.subir_informe(informe)

         elif opcion_informe ==2:
           lista_reporte.mostrar_reporte()
         elif opcion_informe == 3:
           lista_reporte.borrar_informe(input("nombre a borrar: "),input("fecha del informe.\n"))
         elif opcion_informe == 4:
           break
           
       elif opcion_listas == 3:
        print("cerrando programa....")
        break
      elif opcion_inicial == 2:
        pass
if __name__=="__main__":
  main()
