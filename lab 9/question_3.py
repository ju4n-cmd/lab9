class Libro:
    def __init__(self, titulo, autor, paginas, leidas=0):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas
        self._progreso = min(max(leidas, 0), paginas)

    def leer(self, cantidad):
        if cantidad > 0 and self._progreso + cantidad <= self.paginas:
            self._progreso += cantidad
        else:
            print("Cantidad inválida")

    def progreso(self):
        if self.paginas == 0:
            return 0
        return round(self._progreso * 100 / self.paginas)

    def resumen(self):
        texto = (
            f"{self.titulo} - {self.autor} ({self.progreso()}%): "
            f"{self._progreso} páginas leídas de {self.paginas}"
        )
        print(texto)
        return texto