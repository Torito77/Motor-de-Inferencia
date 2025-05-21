# bh = base de hechos
# bc = base de conocimientos
# CC = conjunto conflicto
# M = meta a verificar
# R = regla del cc seleccionada
# nh = nuevo hecho
# nm = nueva meta

from typing import List
from regla import Regla
from regla import reglas_disparables


def encadenamiento_delante(reglas: List[Regla], hechos_iniciales, meta):
    reglas_disparadas = []
    bh = set(hechos_iniciales)
    cc: List[Regla] = [] + reglas_disparables(reglas, bh, reglas_disparadas)

    while (cc) and (meta not in bh):
        r:Regla = cc.pop(0)
        nh = r.consecuente
        bh.add(nh)
        reglas_disparadas.append(r)
        if meta not in bh:
            cc += reglas_disparables(reglas, bh, set(reglas_disparadas + cc))
    
    
    return (meta in bh), reglas_disparadas
    