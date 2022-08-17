class Direccion:
    def __init__(self, calle: str, numero: str, ciudad: str, provincia: str, pais: str):
        self.calle = calle
        self.numero = numero
        self.ciudad = ciudad
        self.provincia = provincia
        self.pais = pais

    def __str__(self):
        return '{} {}, {} {}, {}.'.format(self.calle, self.numero, self.ciudad, self.provincia, self.pais)

    def validate(self) -> bool:
        return True

    def outputAsLabel(
        self,
    ) -> str:
        return ""
