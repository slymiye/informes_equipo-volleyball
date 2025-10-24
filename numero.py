def pedir_numero(msg):
    while True:
     try:
       numero=int(input(msg))
       return numero
     except ValueError:
        print("por favor ingresar solo numeros")
