from pyswip import Prolog
prolog = Prolog()

def prolog_query(query, id = None):
    values = list(prolog.query(query))

    out = []
    if id is not None:
        for value in values:
            out.append(value[id])
    else:
        return values
    
    return out