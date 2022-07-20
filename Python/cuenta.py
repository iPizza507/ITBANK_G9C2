class Cuenta:
    def __init__(self, limiteExtraccion: float, limiteTransferenciaRecibida: float, monto: float, costoTransferencias: float, saldoDescubiertoDisponible: float):
        self.limiteExtraccion = limiteExtraccion
        self.limiteTransferenciaRecibida = limiteTransferenciaRecibida
        self.monto = monto
        self.costoTransferencias = costoTransferencias
        self.saldoDescubiertoDisponible = saldoDescubiertoDisponible
