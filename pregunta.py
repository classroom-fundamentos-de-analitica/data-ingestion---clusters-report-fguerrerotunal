"""
Ingestión de datos - Reporte de clusteres
-----------------------------------------------------------------------------------------

Construya un dataframe de Pandas a partir del archivo 'clusters_report.txt', teniendo en
cuenta que los nombres de las columnas deben ser en minusculas, reemplazando los espacios
por guiones bajos; y que las palabras clave deben estar separadas por coma y con un solo 
espacio entre palabra y palabra.


"""
import pandas as pd

def ingest_data():
    
    import re
    
    with open('clusters_report.txt') as cosaMaluca:
        table = cosaMaluca.readlines()
    
    
    header = ['cluster', 'cantidad_de_palabras_clave', 'porcentaje_de_palabras_clave', 'principales_palabras_clave']
    nueva = []
    fila = []
    
    table = table[4:]
    
    for line in table:
        
        #primeras
        if re.match("^ +\d", line):
            cluster, cantidad, porcentaje, *palabras = line.split()
            palabras = " ".join(palabras[1:])
            fila = [int(cluster), int(cantidad), float(porcentaje.replace(",",".")), palabras]
        
        #intermedias
        elif re.match("^ +\w", line):
            palabras = line.split()
            palabras = " ".join(palabras)
            fila[3] += " " + palabras
            
        #separador
        else:
            fila[3] = fila[3].replace(".", "")
            nueva.append(fila)
    
    df = pd.DataFrame(nueva,columns=header)
    
    return df