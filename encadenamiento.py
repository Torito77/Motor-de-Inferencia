# bh = base de hechos
# bc = base de conocimientos == reglas
# CC = conjunto conflicto
# M = meta a verificar
# R = regla del cc seleccionada
# nh = nuevo hecho
# nm = nuevaS metaS

from typing import List, Set
from regla import Regla, reglas_disparables, equiparacion
from prettytable import PrettyTable

def encadenamiento_delante(reglas: List[Regla], hechos_iniciales, meta: str):
    table = PrettyTable(["CC","NH","M","R","BH"])
    
    reglas_disparadas = []
    bh = set(hechos_iniciales)
    cc: List[Regla] = [] + reglas_disparables(reglas, bh, reglas_disparadas)

    table.add_row([str(cc),"",meta,"",str(bh)])

    while (cc) and (meta not in bh):
        r = cc.pop(0)
        nh = r.consecuente
        bh.add(nh)
        reglas_disparadas.append(r)
        
        if meta not in bh:
            cc += reglas_disparables(reglas, bh, set(reglas_disparadas + cc))
        
        table.add_row([str(cc),nh,"",r.nombre,str(bh)])
    
    print(table)
    
    # return reglas disparadas
    return meta in bh


def encadenamiento_detras(reglas: List[Regla], hechos_iniciales, meta: str) -> bool:
    bh = set(hechos_iniciales)
    table = PrettyTable(["CC","NM","M","R","BH"])
    
    def verificar( meta:str, bh:Set[str] ) -> bool:
        
        nonlocal reglas
        nonlocal table
        
        # - - - - - - - Algorithm starts here :) - - - - - - - >
        
        verificado = False
        
        if meta in bh:
            return True
        
        cc = equiparacion(reglas, meta)
        
        while cc and not verificado:
            r = cc.pop(0)
            nm = r.antecedentes - bh
            verificado = True
            
            # Table printing code - - - - >
            table.add_row([str(cc if cc else ""),str(nm if nm else ""),meta,f"{r.nombre}",str(bh)])
            # - - - - - - - - - - - - - - >
            
            while nm and verificado:
                
                meta = nm.pop()
                verificado = verificar(meta, bh)
                
                if verificado:
                    bh.add(meta)
                    
        return verificado

    resultado = verificar(meta, bh)
    # Table printing code - - - - >
    # NOTE: Adds a bh row right
    if resultado:
        table.add_row(["","","","",str(bh)])
        table.add_row(["","","","",str(bh.union({meta}))])
    # - - - - - - - - - - - - - - >
    
    print(table)
    return resultado