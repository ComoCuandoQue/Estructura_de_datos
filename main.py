class Persona:
    def __init__(self, cod_persona, nombre, apellido_paterno, apellido_materno, fecha_nacimiento):
        self.cod_persona = cod_persona
        self.nombre = nombre
        self.apellido_paterno = apellido_paterno
        self.apellido_materno = apellido_materno
        self.fecha_nacimiento = fecha_nacimiento

    def __str__(self):
        return f"Código de Persona: {self.cod_persona}\nNombre: {self.nombre}\nApellido Paterno: {self.apellido_paterno}\nApellido Materno: {self.apellido_materno}\nFecha de Nacimiento: {self.fecha_nacimiento}"

    def cambiar_nombre(self, nuevo_nombre):
        self.nombre = nuevo_nombre

    def cambiar_apellido_paterno(self, nuevo_apellido_paterno):
        self.apellido_paterno = nuevo_apellido_paterno

    def cambiar_apellido_materno(self, nuevo_apellido_materno):
        self.apellido_materno = nuevo_apellido_materno

    def cambiar_fecha_nacimiento(self, nueva_fecha_nacimiento):
        self.fecha_nacimiento = nueva_fecha_nacimiento

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

class Categoria:
    def __init__(self, cod_categoria, categoria):
        self.cod_categoria = cod_categoria
        self.categoria = categoria

    def __str__(self):
        return f"Código de Categoría: {self.cod_categoria}\nCategoría: {self.categoria}"

    def cambiar_categoria(self, nueva_categoria):
        self.categoria = nueva_categoria

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

'''
# Ejemplo de cómo crear una instancia de Categoria
categoria1 = Categoria(1, "Ficción")

# Acceder a los atributos de la instancia
print(categoria1.categoria)  # Imprime "Ficción"

# Imprimir toda la información de la categoría
print(categoria1)

# Ejemplo de cómo crear una instancia de Libro
libro1 = Libro(101, "La Historia de la Tierra", 2023, "Tomo 1")

# Acceder a los atributos de la instancia
print(libro1.titulo)  # Imprime "La Historia de la Tierra"
print(libro1.año)  # Imprime 2023

# Imprimir toda la información del libro
print(libro1)

# Ejemplo de cómo crear una instancia de Autor
autor1 = Autor(1, "Juan", "Pérez", "Gómez", "2000-05-15", 101, "España", "Editorial ABC")

# Acceder a los atributos de la instancia
print(autor1.nombre)  # Imprime "Juan"
print(autor1.fecha_nacimiento)  # Imprime "2000-05-15"

# Imprimir toda la información del autor, incluyendo la heredada de Persona
print(autor1)

# Ejemplo de cómo cambiar el nombre de una persona
persona1 = Persona(1, "Juan", "Pérez", "Gómez", "2000-05-15")
print(persona1)
persona1.cambiar_nombre("Carlos")
print(persona1.nombre)  # Imprime "Carlos"
print(persona1)


gestor = GestorMantenimiento()

# Agregar una persona
persona1 = Persona(1, "Juan", "Perez", "Gomez", "2000-01-15")
gestor.agregar_persona(persona1)

persona_encontrada = gestor.buscar_persona(1)
print(persona_encontrada)
# Modificar una persona
gestor.modificar_persona(1, "Juan", "Perez", "Gomez", "1995-03-20")

# Eliminar una persona
#gestor.eliminar_persona(1)

# Buscar una persona
persona_encontrada = gestor.buscar_persona(1)

if persona_encontrada:
    print(persona_encontrada)
else:
    print("Persona no encontrada")

# Agregar algunos libros (esto es solo un ejemplo)
libro1 = Libro(1, "Libro 1", 2023, 1)
libro2 = Libro(2, "Libro 2", 2022, 2)
gestor.agregar_libro(libro1)
gestor.agregar_libro(libro2)

# Generar el reporte de libros
gestor.generar_reporte_libros()
'''
def mostrar_menu():
    print("Menú de Gestión:")
    print("1. Agregar Persona")
    print("2. Modificar Persona")
    print("3. Eliminar Persona")
    print("4. Buscar Persona")
    print("5. Agregar Autor")
    print("6. Modificar Autor")
    print("7. Eliminar Autor")
    print("8. Buscar Autor")
    print("9. Agregar Libro")
    print("10. Modificar Libro")
    print("11. Eliminar Libro")
    print("12. Buscar Libro")
    print("13. Agregar Categoría")
    print("14. Modificar Categoría")
    print("15. Eliminar Categoría")
    print("16. Buscar Categoría")
    print("17. Generar Reporte de Libros")
    print("0. Salir")

gestor = GestorMantenimiento()

while True:
    mostrar_menu()
    opcion = input("Selecciona una opción: ")

    if opcion == "1":
        cod_persona = input("Ingrese el código de la persona: ")
        nombre = input("Ingrese el nombre de la persona: ")
        apellido_paterno = input("Ingrese el apellido paterno de la persona: ")
        apellido_materno = input("Ingrese el apellido materno de la persona: ")
        fecha_nacimiento = input("Ingrese la fecha de nacimiento de la persona: ")

        # Crear una instancia de Persona con los datos ingresados
        nueva_persona = Persona(cod_persona, nombre, apellido_paterno, apellido_materno, fecha_nacimiento)

        # Agregar la persona al gestor de mantenimiento
        gestor.agregar_persona(nueva_persona)
        print("Persona agregada con éxito.")

        pass
    elif opcion == "2":
        cod_persona = input("Ingrese el código de la persona a modificar: ")

        # Buscar la persona por su código
        persona = gestor.buscar_persona(cod_persona)

        if persona:
            nuevo_nombre = input("Ingrese el nuevo nombre de la persona: ")
            nuevo_apellido_paterno = input("Ingrese el nuevo apellido paterno de la persona: ")
            nuevo_apellido_materno = input("Ingrese el nuevo apellido materno de la persona: ")
            nueva_fecha_nacimiento = input("Ingrese la nueva fecha de nacimiento de la persona: ")

            # Modificar los datos de la persona
            if gestor.modificar_persona(cod_persona, nuevo_nombre, nuevo_apellido_paterno, nuevo_apellido_materno,
                                        nueva_fecha_nacimiento):
                print("Datos de la persona modificados con éxito.")
            else:
                print("No se encontró una persona con ese código.")
        else:
            print("No se encontró una persona con ese código.")

        pass
    elif opcion == "3":
        cod_persona = input("Ingrese el código de la persona a eliminar: ")

        # Buscar la persona por su código
        persona = gestor.buscar_persona(cod_persona)

        if persona:
            # Confirmar la eliminación
            confirmacion = input(
                f"¿Está seguro de eliminar a la persona {persona.nombre} {persona.apellido_paterno}? (S/N): ")
            if confirmacion.upper() == "S":
                # Eliminar la persona
                if gestor.eliminar_persona(cod_persona):
                    print("Persona eliminada con éxito.")
                else:
                    print("No se encontró una persona con ese código.")
            else:
                print("Eliminación cancelada.")
        else:
            print("No se encontró una persona con ese código.")

        pass
    elif opcion == "4":
        cod_persona = input("Ingrese el código de la persona a buscar: ")

        # Buscar la persona por su código
        persona = gestor.buscar_persona(cod_persona)

        print(persona)
        pass
    elif opcion == "5":
        cod_persona = input("Ingrese el código de la persona: ")
        nombre = input("Ingrese el nombre de la persona: ")
        apellido_paterno = input("Ingrese el apellido paterno de la persona: ")
        apellido_materno = input("Ingrese el apellido materno de la persona: ")
        fecha_nacimiento = input("Ingrese la fecha de nacimiento de la persona: ")
        cod_autor = input("Ingrese el codigo como autor: ")
        pais = input("Ingrese el pais: ")
        editorial = input("Ingrese la editorial: ")

        nuevo_autor = Autor(cod_persona, nombre, apellido_paterno, apellido_materno, fecha_nacimiento, cod_autor, pais, editorial)

        gestor.agregar_autor(nuevo_autor)
        print("Autor agregado con éxito.")
        pass
    elif opcion == "6":
        cod_autor = input("Ingrese el código del autor a modificar: ")

        autor = gestor.buscar_autor(cod_autor)

        if autor:
            nuevo_nombre = input("Ingrese el nuevo nombre del autor: ")
            nuevo_apellido_paterno = input("Ingrese el nuevo apellido paterno del autor: ")
            nuevo_apellido_materno = input("Ingrese el nuevo apellido materno del autor: ")
            nueva_fecha_nacimiento = input("Ingrese la nueva fecha de nacimiento del autor: ")
            

            if gestor.modificar_persona(cod_persona, nuevo_nombre, nuevo_apellido_paterno, nuevo_apellido_materno,
                                        nueva_fecha_nacimiento):
                print("Datos de la persona modificados con éxito.")
            else:
                print("No se encontró una persona con ese código.")
        else:
            print("No se encontró una persona con ese código.")
        pass
    elif opcion == "7":
        # Eliminar Autor
        # Solicitar el código de autor y eliminarlo del gestor
        pass
    elif opcion == "8":
        # Buscar Autor
        # Solicitar el código de autor y mostrar la información del autor
        pass
    elif opcion == "9":
        # Agregar Libro
        # Solicitar datos y crear una instancia de Libro, luego agregarla al gestor
        pass
    elif opcion == "10":
        # Modificar Libro
        # Solicitar el código de libro y los nuevos datos, luego llamar a modificar_libro
        pass
    elif opcion == "11":
        # Eliminar Libro
        # Solicitar el código de libro y eliminarlo del gestor
        pass
    elif opcion == "12":
        # Buscar Libro
        # Solicitar el código de libro y mostrar la información del libro
        pass
    elif opcion == "13":
        # Agregar Categoría
        # Solicitar datos y crear una instancia de Categoria, luego agregarla al gestor
        pass
    elif opcion == "14":
        # Modificar Categoría
        # Solicitar el código de categoría y la nueva categoría, luego llamar a modificar_categoria
        pass
    elif opcion == "15":
        # Eliminar Categoría
        # Solicitar el código de categoría y eliminarla del gestor
        pass
    elif opcion == "16":
        # Buscar Categoría
        # Solicitar el código de categoría y mostrar la información de la categoría
        pass
    elif opcion == "17":
        gestor.generar_reporte_libros()
        pass
    elif opcion == "0":
        print("Adios")
        break
    else:
        print("Opción no válida. Por favor, selecciona una opción válida.")
