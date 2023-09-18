from persona import Persona

class Autor(Persona):
    def __init__(self, cod_persona, nombre, apellido_paterno, apellido_materno, fecha_nacimiento, cod_autor, pais, editorial):
        super().__init__(cod_persona, nombre, apellido_paterno, apellido_materno, fecha_nacimiento)
        self.cod_autor = cod_autor
        self.pais = pais
        self.editorial = editorial

    def __str__(self):
        persona_info = super().__str__()
        return f"{persona_info}\nCódigo de Autor: {self.cod_autor}\nPaís: {self.pais}\nEditorial: {self.editorial}"

    def cambiar_cod_autor(self, nuevo_cod_autor):
        self.cod_autor = nuevo_cod_autor

    def cambiar_pais(self, nuevo_pais):
        self.pais = nuevo_pais

    def cambiar_editorial(self, nueva_editorial):
        self.editorial = nueva_editorial