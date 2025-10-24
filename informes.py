import datetime as dt

class Informe :
 def __init__(self,nombre,posicion,remate,bloqueo,saque,cobertura,recepcion,colocacion,fallos):
  self.nombre=nombre
  self.posicion=posicion
  self.remate=remate
  self.bloqueo=bloqueo
  self.saque=saque
  self.cobertura=cobertura
  self.recepcion=recepcion
  self.colocacion=colocacion
  self.fallos=fallos
  self.fecha=dt.date.today()

 def ajustar_posicion(self):
  if self.posicion.lower() in ["libero"]:
   self.remate=0
   self.bloqueo=0
   self.saque=0
   self.colocacion=0
  elif self.posicion.lower() in ["central"]:
   self.recepcion=0
   self.colocacion=0
 def mostrar_informe(self):
  print(f"--------\nnombre: {self.nombre}\nposicion: {self.posicion}\nremate: {self.remate}\nbloqueo: {self.bloqueo}\nsaque: {self.saque}\ncobertura: {self.cobertura}\nrecepcion: {self.recepcion}\ncolocacion: {self.colocacion}\nfallos: {self.fallos}\nfecha del informe: {self.fecha}")
  
