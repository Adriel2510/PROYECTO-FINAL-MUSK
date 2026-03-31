import json
import pandas as pd
from src.funcionals_utils import mapear_clientes, leer_archivo_ventas, normalizar_clientes
from src.sales_collection import SalesCollection
from src.client_collection import ClientCollection
from decimal import Decimal, ROUND_HALF_UP



#1.Número total de clientes

def calcular_total_clientes(clientes):
    total_clientes = len(clientes)
    return total_clientes

#2.Numero total de ventas

def calcular_total_ventas(ventas):
    total_ventas = len(ventas)
    return total_ventas

#3.Total de ingresos por cliente

def total_ingresos_cliente(ventas):
    ingresos_por_cliente = ventas.groupby("client_id")["amount"].sum()
    return ingresos_por_cliente.to_dict()

#4.Numero de ventas por cliente

def total_ventas_cliente(client_id):
    ventas_por_cliente = SalesCollection.sales_by_client(client_id)
    return len(ventas_por_cliente)

#5.Ingreso promedio por cada venta de cada cliente

def promedio_venta_cliente(ventas):
    promedio = ventas.groupby("client_id")["amount"].mean()
    return promedio

#6.Cliente con mayor gasto por pais

def cliente_mayor_gasto_pais(ventas, clientes):
    paises = {}
    mayores_clientes_pais = {}
    for cliente in clientes:
        if cliente.country in paises.keys():
            paises[cliente.country].append(cliente)
        else:
            paises[cliente.country] = [cliente]

    for pais, lista_clientes in paises.items():
        mayor_gasto = 0
        mayor_cliente = None
        for cliente in lista_clientes:
            ventas_cliente = ventas[ventas["client_id"] == cliente.client_id]
            if mayor_gasto < ventas_cliente["amount"].sum():
                mayor_gasto = ventas_cliente["amount"].sum()
                mayor_cliente = cliente.name
        mayores_clientes_pais[pais] = mayor_cliente

    return mayores_clientes_pais

#7.Total de ventas por categoria

def total_ventas_categoria(ventas):
    return ventas.groupby("category")["amount"].sum()

#8.Cliente con mas ventas en una categoria espefica

def cliente_mas_ventas_categoria(ventas, categoria):
    ventas_filtradas = ventas[ventas["category"].str.lower() == categoria.lower()]
    numero_ventas_cliente = ventas_filtradas["client_id"].value_counts()
    return numero_ventas_cliente.idxmax()

#9.Clientes que superan un gasto minimo

def cliente_supera_gasto_min(cliente, ventas, gasto_min):
    clientes_encima_min = []
    ventas_cliente = ventas[ventas["client_id"] == cliente.client_id]
    if ventas_cliente["amount"].sum() > gasto_min:
            clientes_encima_min.append(cliente.name) 

    return clientes_encima_min


#10.Ventas acumuladas mes a mes

def ventas_acumuladas(ventas):
    ventas["date"] = pd.to_datetime(ventas["date"])
    ventas["anio_mes"] = ventas["date"].dt.to_period("M")
    ventas_acum_meses = ventas.groupby("anio_mes")["amount"].sum()

    return {str(k): round(v, 2) for k, v in ventas_acum_meses.items()}



def generate_report():
    clientes = mapear_clientes()
    clientes_normalizados = normalizar_clientes(clientes)
    ventas = leer_archivo_ventas()

    col_clientes = ClientCollection(clientes)
    col_ventas = SalesCollection(ventas)

    informe = {
        "summary" : {},
        "clients" : [],
        "top_client_by_country" : {},
        "sales_by_category" : {},
        "high_spending_clients" : [],
        "monthly_sales" : {}
        }

    informe["summary"]["total_clients"] = len(clientes)
    informe["summary"]["total_sales"] = len(ventas)
    informe["summary"]["total_revenue"] = ventas["amount"].sum()

    for cliente in clientes:
        informe["clients"].append({
            "client_id" : cliente.client_id,
            "name" : cliente.name,
            "total_spent" : col_ventas.total_amount_by_client(cliente.client_id),
            "sale_count" : len(col_ventas.sales_by_client(cliente.client_id)),
            "average_sale" : col_ventas.average_sale_by_client(cliente.client_id)
             })

    informe["top_client_by_country"] = cliente_mayor_gasto_pais(ventas, clientes)


    for categoria in ventas["category"]:
        informe["sales_by_category"][categoria] = col_ventas.total_amount_by_category(categoria)

    for cliente in clientes:
        if cliente_supera_gasto_min(cliente, ventas, 500):
            informe["high_spending_clients"].append(cliente.name)

    informe["monthly_sales"] = ventas_acumuladas(ventas)

    return informe