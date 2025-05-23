import regla
from encadenamiento import encadenamiento_delante, encadenamiento_detras


def helper(encadenamiento):
    if not reglas:
        print("No se encontraron reglas")
        return
    if not hechos_iniciales:
        print("No se encontraron hechos iniciales")
        return
    if not meta:
        print("No se encontro una meta")
        return
    
    exito = encadenamiento(reglas, hechos_iniciales, meta)
    print("Éxito :)" if exito else "Fracaso :(")


# - - - - - - - - - - Main program - - - - - - - - - - >

ruta = "./FormatoEsperado.txt"
reglas, hechos_iniciales, meta = regla.cargar_reglas_desde_archivo(ruta)

while True:
    
    match input("\nSeleccione una opción: \n"
                "1) Encadenamiento hacia adelante\n"
                "2) Encadenamiento hacia atrás\n"
                "3) Definir ruta del archivo\n"
                "4) Definir hechos iniciales\n"
                "5) Definir meta\n"
                "q) Salir\n").lower():
        
        case "1":
            helper(encadenamiento_delante)
            
        case "2":
            helper(encadenamiento_detras)
            
        case "3":
            ruta = input("Ingrese la nueva ruta: ")
            try:
                reglas = regla.cargar_reglas_desde_archivo(ruta)
            except FileNotFoundError as error:
                print("Archivo no encontrado")
            else:
                print("Ruta guardada!")
        
        case "4":
            contenido = input("Ingrese los hechos iniciales separados por ',': ").strip().strip("{}")
            hechos_iniciales = { h.strip().upper() for h in contenido.split(",") if h.strip() }
            
        case "5":
            meta = input("Ingrese la meta: ").strip().upper()
            
        case "q":
            break

