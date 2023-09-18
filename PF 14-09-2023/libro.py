class Libro:
    def __init__(self, codigo_libro, titulo, año, tomo):
        self.codigo_libro = codigo_libro
        self.titulo = titulo
        self.año = año
        self.tomo = tomo

    def __str__(self):
        return f"Código del Libro: {self.codigo_libro}\nTítulo: {self.titulo}\nAño: {self.año}\nTomo: {self.tomo}"

    def cambiar_titulo(self, nuevo_titulo):
        self.titulo = nuevo_titulo

    def cambiar_año(self, nuevo_año):
        self.año = nuevo_año

    def cambiar_tomo(self, nuevo_tomo):
        self.tomo = nuevo_tomo