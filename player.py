class Integrante():
    def __init__(self,nombre,edad,altura,pocision):
        self.nombre=nombre
        self.edad=edad
        self.altura=altura
        self.pocision=pocision
    def mostrar_datos(self):
        print(f"Nombre: {self.nombre}\nEdad: {self.edad} años\nAltura: {self.altura}cm\nPocision: {self.pocision}")