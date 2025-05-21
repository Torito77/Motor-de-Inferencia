class Regla:
    def __init__(self, nombre, antecedentes, consecuente):
        self.nombre = nombre
        self.antecedentes = set(antecedentes)
        self.consecuente = consecuente

    def es_disparable(self, hechos):
        return self.antecedentes.issubset(hechos)

    def __str__(self):
        ant = " y ".join(self.antecedentes)
        return f"{self.nombre}: {ant} -> {self.consecuente}"


def cargar_reglas_desde_archivo(ruta):
    """
    Carga las reglas desde un archivo

    Parametetros:
    ruta (str): Ubicación del archivo

    Returns:
    lista[Reglas]: Listado de las reglas extraidas

    """
    reglas = []
    with open(ruta, "r") as archivo:
        for linea in archivo:
            linea = linea.strip()
            if not linea or "->" not in linea:
                continue

            nombre, cuerpo = linea.split(":", 1)
            antecedente_str, consecuente = cuerpo.split("->")
            antecedentes = [a.strip() for a in antecedente_str.strip().split("y")]
            reglas.append(Regla(nombre.strip(), antecedentes, consecuente.strip()))
    return reglas
