import pandas as pd
from decimal import Decimal, ROUND_HALF_UP
class SalesCollection():

    """
    Se encarga de gestionar las instancias de Sale, y normaliza la entrada de ellos convirtiendolos en un DataFrame.

    Atributos:
        ventas: Lista o DataFrame de todas las ventas.

    Metodos:
       -sales_by_client(client_id):
        Busca un cliente a partir de su client_id y muestra todas las ventas de un cliente en particular.
        Devuelve:
            List: Una lista de diccionarios con todas las ventas de un cliente en particular,
            si no hay ningun cliente que tenga el client_id que se busca, la lista estera vacia.
        
       -total_amount_by_client(client_id)::
        Busca un cliente a partir de su client_id y muestra el gasto total sumando todas sus ventas.
        Devuelve:
            Float: Total gastado por dicho cliente

       -total_amount_by_category(category):
        Dada una categoria, mostrara la suma de todas las ventas en dicha categoria.
        Devuelve:
            Float: Suma total de las ventas en dicha categoria.

       -avarage_sale_by_client(client_id):
        Busca un cliente a partir de su client_id y muestra el promedio del gasto de sus ventas.
        Devuelve:
            float:El promedio gastado de este cliente redondeado aritmeticamente. Si no se encuentra
            el cliente devolvera 0.0
    """

    def __init__(self, ventas):
        if isinstance(ventas, pd.DataFrame):
            self.ventas = ventas
        else:
            self.ventas = pd.DataFrame([v.to_dict() for v in ventas])
    def sales_by_client(self, client_id):
        return self.ventas[self.ventas["client_id"] == client_id].to_dict(orient='records')
    
    def total_amount_by_client(self, client_id):
        ventas_filtradas = self.ventas[self.ventas["client_id"] == client_id]
        return ventas_filtradas["amount"].sum()

    def total_amount_by_category(self, category):
        ventas_filtradas_categoria = self.ventas[self.ventas["category"] == category]
        return ventas_filtradas_categoria["amount"].sum()

    def average_sale_by_client(self, client_id):
        ventas_filtradas = self.ventas[self.ventas["client_id"] == client_id]["amount"]
        if ventas_filtradas.empty:
            return 0.0
        
        promedio = ventas_filtradas.mean()

        promedio_decimal = Decimal(str(promedio)).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
        return  float(promedio_decimal)