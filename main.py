import regla
from encadenamiento import encadenamiento_delante, encadenamiento_detras

reglas, hechos_iniciales, meta = regla.cargar_reglas_desde_archivo("./FormatoEsperado.txt")

#exito, reglas_disparadas = encadenamiento_delante(reglas,hechos_iniciales,meta)


exito = encadenamiento_detras(reglas,hechos_iniciales,meta)
if exito:
    print("Éxito :)")
else:
    print("Fracaso :(")