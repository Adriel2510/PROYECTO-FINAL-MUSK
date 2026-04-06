import json
from src.client import Client
import pandas as pd

def leer_archivo_clientes():
    """""
    Se encarga de leer el archivo de clientes y devolverlo en forma de 
    un objeto de python.
    """""
    with open('data/clients.json') as archivo_clientes:
        return json.load(archivo_clientes)
    
def mapear_clientes():
    """""
    Se de trasnformar los clientes del objeto que genero la funcion leer_archivos_clientes()
    a objetos Client.
    """""
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
    """""
    Lee el archivo de ventas y lo devuelve convertido en un DataFrame.
    """""
    dataframe_ventas = pd.read_csv("data/sales.csv")
    return dataframe_ventas

        
