from persona import Persona
from autor import Autor
from libro import Libro
from categoria import Categoria
from gestormantenimiento import GestorMantenimiento

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
            nuevo_pais = input("Ingrese el nuevo pais: ")
            nueva_editorial = input("Ingrese la nueva editorial: ")

            if gestor.modificar_autor(cod_autor, nuevo_nombre, nuevo_apellido_paterno, nuevo_apellido_materno,
                                        nueva_fecha_nacimiento, nuevo_pais, nueva_editorial):
                print("Datos del autor modificados con éxito.")
            else:
                print("No se encontró un autor con ese código.")
        else:
            print("No se encontró un autor con ese código.")
        pass
    elif opcion == "7":
        cod_autor = input("Ingrese el código del autor a eliminar: ")

        autor = gestor.buscar_autor(cod_autor)

        if autor:
            confirmacion = input(
                f"¿Está seguro de eliminar al autor {autor.nombre} {autor.apellido_paterno}? (S/N): ")
            if confirmacion.upper() == "S":
                if gestor.eliminar_autor(cod_autor):
                    print("Autor eliminado con éxito.")
                else:
                    print("No se encontró un autor con ese código.")
            else:
                print("Eliminación cancelada.")
        else:
            print("No se encontró un autor con ese código.")
        pass
    elif opcion == "8":
        cod_autor = input("Ingrese el código del autor a buscar: ")

        autor = gestor.buscar_autor(cod_autor)

        print(autor)
        pass
    elif opcion == "9":
        codigo_libro = input("Ingrese el código del libro: ")
        titulo = input("Ingrese el titulo del libro: ")
        año = input("Ingrese el año del libro: ")
        tomo = input("Ingrese el tomo del libro: ")

        nuevo_libro = Libro(codigo_libro, titulo, año, tomo)

        gestor.agregar_libro(nuevo_libro)
        print("Libro agregado con éxito.")
        pass
    elif opcion == "10":
        codigo_libro = input("Ingrese el código del libro a modificar: ")

        libro = gestor.buscar_libro(codigo_libro)

        if libro:
            nuevo_titulo = input("Ingrese el nuevo titulo del libro: ")
            nuevo_año = input("Ingrese el nuevo año del libro: ")
            nuevo_tomo = input("Ingrese el nuevo tomo del libro: ")

            if gestor.modificar_libro(codigo_libro, nuevo_titulo, nuevo_año, nuevo_tomo):
                print("Datos del libro modificados con éxito.")
            else:
                print("No se encontró un libro con ese código.")
        else:
            print("No se encontró un libro con ese código.")
        pass
    elif opcion == "11":
        codigo_libro = input("Ingrese el código del libro a eliminar: ")

        libro = gestor.buscar_libro(codigo_libro)

        if libro:
            confirmacion = input(
                f"¿Está seguro de eliminar el libro {libro.titulo}? (S/N): ")
            if confirmacion.upper() == "S":
                if gestor.eliminar_autor(codigo_libro):
                    print("Libro eliminado con éxito.")
                else:
                    print("No se encontró un libro con ese código.")
            else:
                print("Eliminación cancelada.")
        else:
            print("No se encontró un libro con ese código.")
        pass
    elif opcion == "12":
        codigo_libro = input("Ingrese el código del libro a buscar: ")

        libro = gestor.buscar_libro(codigo_libro)

        print(libro)
        pass
    elif opcion == "13":
        cod_categoria = input("Ingrese el código de la categoria: ")
        categoria = input("Ingrese el nombre de la categoria: ")

        nueva_categoria = Categoria(cod_categoria, categoria)

        gestor.agregar_categoria(nueva_categoria)
        print("Categoria agregada con éxito.")
        pass
    elif opcion == "14":
        cod_categoria = input("Ingrese el código de la categoria a modificar: ")

        categoria = gestor.buscar_categoria(cod_categoria)

        if categoria:
            nueva_categoria = input("Ingrese el nuevo nombre de la categoria: ")

            if gestor.modificar_categoria(cod_categoria, nueva_categoria):
                print("Datos de la categoria modificadas con éxito.")
            else:
                print("No se encontró una categoria con ese código.")
        else:
            print("No se encontró una categoria con ese código.")
        pass
    elif opcion == "15":
        cod_categoria = input("Ingrese el código de la categoria a eliminar: ")

        categoria = gestor.buscar_categoria(cod_categoria)

        if categoria:
            confirmacion = input(
                f"¿Está seguro de eliminar a la categoria {categoria.categoria}? (S/N): ")
            if confirmacion.upper() == "S":
                if gestor.eliminar_categoria(cod_categoria):
                    print("Categoria eliminada con éxito.")
                else:
                    print("No se encontró una categoria con ese código.")
            else:
                print("Eliminación cancelada.")
        else:
            print("No se encontró una categoria con ese código.")
        pass
    elif opcion == "16":
        cod_categoria = input("Ingrese el código de la categoria a buscar: ")

        categoria = gestor.buscar_categoria(cod_categoria)

        print(categoria)
        pass
    elif opcion == "17":
        gestor.generar_reporte_libros()
        pass
    elif opcion == "0":
        print("Adios")
        break
    else:
        print("Opción no válida. Por favor, selecciona una opción válida.")