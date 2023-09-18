class GestorMantenimiento:
    def __init__(self):
        self.personas = []
        self.autores = []
        self.libros = []
        self.categorias = []

    # Métodos para gestionar Personas
    def agregar_persona(self, persona):
        self.personas.append(persona)

    def modificar_persona(self, cod_persona, nuevo_nombre, nuevo_apellido_paterno, nuevo_apellido_materno, nueva_fecha_nacimiento):
        for persona in self.personas:
            if persona.cod_persona == cod_persona:
                persona.cambiar_nombre(nuevo_nombre)
                persona.cambiar_apellido_paterno(nuevo_apellido_paterno)
                persona.cambiar_apellido_materno(nuevo_apellido_materno)
                persona.cambiar_fecha_nacimiento(nueva_fecha_nacimiento)
                return True
        return False

    def eliminar_persona(self, cod_persona):
        for persona in self.personas:
            if persona.cod_persona == cod_persona:
                self.personas.remove(persona)
                return True
        return False

    def buscar_persona(self, cod_persona):
        for persona in self.personas:
            if persona.cod_persona == cod_persona:
                return persona
        return None

    # Métodos para gestionar Autores
    def agregar_autor(self, autor):
        self.autores.append(autor)

    def modificar_autor(self, cod_autor, nuevo_nombre, nuevo_apellido_paterno, nuevo_apellido_materno, nueva_fecha_nacimiento, nuevo_pais, nueva_editorial):
        for autor in self.autores:
            if autor.cod_autor == cod_autor:
                autor.cambiar_nombre(nuevo_nombre)
                autor.cambiar_apellido_paterno(nuevo_apellido_paterno)
                autor.cambiar_apellido_materno(nuevo_apellido_materno)
                autor.cambiar_fecha_nacimiento(nueva_fecha_nacimiento)
                autor.cambiar_pais(nuevo_pais)
                autor.cambiar_editorial(nueva_editorial)
                return True
        return False

    def eliminar_autor(self, cod_autor):
        for autor in self.autores:
            if autor.cod_autor == cod_autor:
                self.autores.remove(autor)
                return True
        return False

    def buscar_autor(self, cod_autor):
        for autor in self.autores:
            if autor.cod_autor == cod_autor:
                return autor
        return None

    # Métodos para gestionar Libros
    def agregar_libro(self, libro):
        self.libros.append(libro)

    def modificar_libro(self, codigo_libro, nuevo_titulo, nuevo_año, nuevo_tomo):
        for libro in self.libros:
            if libro.codigo_libro == codigo_libro:
                libro.cambiar_titulo(nuevo_titulo)
                libro.cambiar_año(nuevo_año)
                libro.cambiar_tomo(nuevo_tomo)
                return True
        return False

    def eliminar_libro(self, codigo_libro):
        for libro in self.libros:
            if libro.codigo_libro == codigo_libro:
                self.libros.remove(libro)
                return True
        return False

    def buscar_libro(self, codigo_libro):
        for libro in self.libros:
            if libro.codigo_libro == codigo_libro:
                return libro
        return None

    # Métodos para gestionar Categorías
    def agregar_categoria(self, categoria):
        self.categorias.append(categoria)

    def modificar_categoria(self, cod_categoria, nueva_categoria):
        for categoria in self.categorias:
            if categoria.cod_categoria == cod_categoria:
                categoria.cambiar_categoria(nueva_categoria)
                return True
        return False

    def eliminar_categoria(self, cod_categoria):
        for categoria in self.categorias:
            if categoria.cod_categoria == cod_categoria:
                self.categorias.remove(categoria)
                return True
        return False

    def buscar_categoria(self, cod_categoria):
        for categoria in self.categorias:
            if categoria.cod_categoria == cod_categoria:
                return categoria
        return None

    def generar_reporte_libros(self, nombre_archivo="reporte_fecha.txt"):
        try:
            with open(nombre_archivo, "w") as archivo:
                archivo.write("Reporte de Libros\n\n")
                for libro in self.libros:
                    archivo.write(f"Código: {libro.codigo_libro}\n")
                    archivo.write(f"Título: {libro.titulo}\n")
                    archivo.write(f"Año: {libro.año}\n")
                    archivo.write(f"Tomo: {libro.tomo}\n")
                    archivo.write("\n")
                print(f"El reporte de libros ha sido generado en {nombre_archivo}")
        except Exception as e:
            print(f"Error al generar el reporte de libros: {str(e)}")