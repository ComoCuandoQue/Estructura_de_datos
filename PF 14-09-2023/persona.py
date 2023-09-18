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