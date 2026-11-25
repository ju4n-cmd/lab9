class Estudiante:
    def __init__(self, nombre, carrera):
        self.nombre = nombre
        self.carrera = carrera
        self._notas = []

    def agregar_nota(self, nota):
        self._notas.append(nota)

    def calcular_promedio(self):
        if len(self._notas) == 0:
            return 0
        return sum(self._notas) / len(self._notas)

    def mostrar_resumen(self):
        print(f"{self.nombre} ({self.carrera}) - Promedio: {self.calcular_promedio():.2f}")