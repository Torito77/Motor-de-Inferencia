import regla
from encadenamiento import encadenamiento_delante, encadenamiento_detras


ruta = "./FormatoEsperado.txt"

#TODO: Pedir reglas y meta al usuario

while True:
    
    reglas, hechos_iniciales, meta = regla.cargar_reglas_desde_archivo(ruta)
    
    match input("\nSeleccione una opción: \n"
                "a) Encadenamiento hacia adelante\n"
                "b) Encadenamiento hacia atrás\n"
                "c) Cambiar ruta del archivo\n"
                "q) Salir\n").lower():
        case "a":
            exito = encadenamiento_delante(reglas,hechos_iniciales,meta)
            print("Éxito :)" if exito else "Fracaso :(")
            
        case "b":
            exito = encadenamiento_detras(reglas,hechos_iniciales,meta)
            print("Éxito :)" if exito else "Fracaso :(")
            
        case "c":
            while True:
                ruta = input("Ingrese la nueva ruta: ")
                try:
                    reglas, hechos_iniciales, meta = regla.cargar_reglas_desde_archivo(ruta)
                except FileNotFoundError as error:
                    print("File not found")
                else:
                    break
                
            print("Ruta guardada!")
        case "q":
            break
    
    