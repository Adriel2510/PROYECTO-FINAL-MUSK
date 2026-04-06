class Client():
    """
    Crea la estructura de un cliente.

    Atributos:
        client_id: Identificador unico en cada cliente.
        name: Nombre del cliente.
        country: Pais de origen del cliente.
        signup_date: Fecha de registro del cliente.

    Metodos:
       -to_dict():
        Convierte un objeto client a un diccionario.
        Devuelve:
            Dict: Un objeto Client transformado en dict.
    """
    def __init__(self, client_id, name, country, signup_date):
        self.client_id = client_id
        self.name = name
        self.country = country
        self.signup_date = signup_date
        pass

    def to_dict(self):
        return {
            "client_id" : self.client_id,
            "name" : self.name,
            "country" : self.country,
            "singup_date" : self.signup_date
        }
        
