class Semaforo:
    def __init__(self, color_inicial="rojo"):
        if color_inicial in ("rojo", "verde", "amarillo"):
            self._color = color_inicial
        else:
            self._color = "rojo"

    def siguiente_estado(self):
        siguiente = {
            "rojo": "verde",
            "verde": "amarillo",
            "amarillo": "rojo",
        }
        self._color = siguiente[self._color]

    def puede_avanzar(self):
        return self._color == "verde"