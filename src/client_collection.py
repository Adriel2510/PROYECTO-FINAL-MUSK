class ClientCollection():

    def __init__(self, clientes):
        self.clientes = clientes

    def get_client_by_id(self, id):
        for cliente in self.clientes:
            if cliente.client_id == id:
                return cliente
        return None
    
    def clients_by_country(self, country):
        return [cliente for cliente in self.clientes if cliente.country.lower() == country.lower()]
