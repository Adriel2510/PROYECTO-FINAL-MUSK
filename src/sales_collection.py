import pandas as pd
from decimal import Decimal, ROUND_HALF_UP
class SalesCollection():
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