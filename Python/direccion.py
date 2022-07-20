class Direccion:
    calle: str = ""
    nombre: str = ""
    ciudad: str = ""
    provincia: str = ""
    pais: str = ""

    def __init__(self, calle: str, nombre: str, ciudad: str, provincia: str, pais: str):
        self.calle = calle
        self.nombre = nombre
        self.ciudad = ciudad
        self.provincia = provincia
        self.pais = pais

    def validate(self) -> bool:
        return True

    def outputAsLabel(
        self,
    ) -> str:
        return ""
