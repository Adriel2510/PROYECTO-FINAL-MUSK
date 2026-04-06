class ClientCollection():

    """
    Se encarga de gestionar las instancias de los objetos Client.

    Atributos:
        clientes: Una lista de todos los clientes.

    Metodos:
       -get_client_by_id(id):
            Dado un id, buscara un cliente el cual su client_id coincida id.
        Devuelve:
            Client: Cliente con el mismo client_id que id.
            None: Si no encontro ningun cliente que su client_id coincidiera con id.

       -clients_by_country(country):
        Dado el nombre de un pais, buscara a todos los clientes que sean de ese pais.
        Devuelve:
            List: Una lista con todos los clientes que son de ese pais, si no hay ninguno
            que sea de ese pais, la lista estara vacia.
    """

    def __init__(self, clientes):
        self.clientes = clientes

    def get_client_by_id(self, id):
        for cliente in self.clientes:
            if cliente.client_id == id:
                return cliente
        return None
    
    def clients_by_country(self, country):
        return [cliente for cliente in self.clientes if cliente.country.lower() == country.lower()]
