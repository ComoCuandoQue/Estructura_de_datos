class Categoria:
    def __init__(self, cod_categoria, categoria):
        self.cod_categoria = cod_categoria
        self.categoria = categoria

    def __str__(self):
        return f"Código de Categoría: {self.cod_categoria}\nCategoría: {self.categoria}"

    def cambiar_categoria(self, nueva_categoria):
        self.categoria = nueva_categoria