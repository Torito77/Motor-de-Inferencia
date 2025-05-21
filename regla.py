from typing import List


class Regla:
    def __init__(self, nombre:str, antecedentes:List[str], consecuente:str):
        self.nombre = nombre
        self.antecedentes = set(antecedentes)
        self.consecuente = consecuente

    def es_disparable(self, hechos):
        return self.antecedentes.issubset(hechos)

    def __str__(self):
        ant = " y ".join(self.antecedentes)
        return f"{self.nombre}: {ant} -> {self.consecuente}"

def reglas_disparables(reglas, hechos, reglas_usadas):
    disparables = []
    for regla in reglas:
        if ( regla.es_disparable(hechos) ) and ( regla not in reglas_usadas ):
            disparables.append(regla)
        
    return disparables

def cargar_reglas_desde_archivo(ruta):
    """
    Carga las reglas, los hechos iniciales y la meta desde un archivo.

    Parámetros:
        ruta (str): Ubicación del archivo.

    Returns:
        tuple: (lista de reglas, set de hechos iniciales, meta)
    """
    reglas = []
    hechos_iniciales = set()
    meta = None

    with open(ruta, "r") as archivo:
        for linea in archivo:
            linea = linea.strip()
            if not linea:
                continue

            if linea.startswith("bh"):
                contenido = linea.split("=", 1)[1].strip().strip("{}")
                hechos_iniciales = {h.strip() for h in contenido.split(",") if h.strip()}
                
            elif linea.startswith("m"):
                meta = linea.split("=", 1)[1].strip()
                
            elif "->" in linea:
                nombre, cuerpo = linea.split(":", 1)
                antecedente_str, consecuente = cuerpo.split("->")
                antecedentes = [a.strip() for a in antecedente_str.strip().split("y")]
                reglas.append(Regla(nombre.strip(), antecedentes, consecuente.strip()))

    return reglas, hechos_iniciales, meta
