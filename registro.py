class Estudiante:
    def __init__(self, leg, nom, cur, aula, cca):
        self.legajo = leg
        self.nombre = nom
        self.curso = cur
        self.aula = aula
        self.cuestionarios = cca

    def __str__(self):
        r = ''
        r += 'Legajo: {} - Nombre: {} - Curso: 1K{} - Aula: {} - Cuestionarios: {}'
        r = r.format(self.legajo, self.nombre, self.curso, self.aula, self.cuestionarios)
        return r


