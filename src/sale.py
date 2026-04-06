class Sale():

    """
    Crea la estructura de una venta.

    Atributos:
        sale_id: Indetificador unico en cada venta.
        client_id: Identificador del cliente al que pertenece la venta.
        product: Tipo de producto que se compro en la venta.
        category: Categoria a la que pertene el produccto de la venta.
        amount: Monto total de la venta.
        date: Fecha en la que se realizo la venta.

    Metodos:
       -to_dict():
        Convierte un objeto Sale a un diccionario.
        Devuelve:
            Dict: Una venta transformada a diccionario
    """

    def __init__(self, sale_id, client_id, product, category, amount, date):
        self.sale_id = sale_id
        self.client_id = client_id
        self.product = product
        self.category = category
        self.amount = amount
        self.date = date

    def to_dict(self):
        return {
            "sale_id" : self.sale_id,
            "client_id" : self.client_id,
            "product" : self.product,
            "category" : self.category,
            "amount" : self.amount,
            "date" : self.date
        }