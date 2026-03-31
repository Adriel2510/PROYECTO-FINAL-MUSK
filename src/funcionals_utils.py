import json
from src.client import Client
import pandas as pd

def leer_archivo_clientes():
    with open('data/clients.json') as archivo_clientes:
        return json.load(archivo_clientes)
    
def mapear_clientes():
    clientes = leer_archivo_clientes()
    lista_clientes = []
    for cliente in clientes:
        cliente = Client(client_id= cliente["client_id"],
                         name= cliente["name"],
                         country= cliente["country"],
                         signup_date= cliente["signup_date"])
        
        lista_clientes.append(cliente)
    return lista_clientes

def leer_archivo_ventas():
    dataframe_ventas = pd.read_csv("data/sales.csv")
    return dataframe_ventas

def normalizar_clientes(clientes):
    lista_clientes = []
    for cliente in clientes:
        if isinstance(cliente, Client):
            lista_clientes.append(cliente.to_dict())
        else:
            lista_clientes.append(cliente)
    return lista_clientes
        
