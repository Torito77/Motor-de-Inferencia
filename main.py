from prettytable import PrettyTable
import regla
from encadenamiento import encadenamiento_delante

reglas, hechos_iniciales, meta = regla.cargar_reglas_desde_archivo("./FormatoEsperado.txt")

exito, reglas_disparadas = encadenamiento_delante(reglas,hechos_iniciales,meta)

if exito:
    for regla in reglas_disparadas:
        print(f"{regla}")