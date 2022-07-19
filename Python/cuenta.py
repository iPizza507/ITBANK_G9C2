class Cuenta:
 
    def __init__(self, limiteExtraccion:float, limiteTransferenciaRecibida:float,monto:float, tipo, cajaPesos, cajaDolares, tarjetaDebito, costoTransferencias:float, saldoDescubiertoDisponible:float):
        self.limiteExtraccion = limiteExtraccion
        self.limiteTransferenciaRecibida = limiteTransferenciaRecibida
        self.monto = monto
        self.tipo = tipo     
        self.cajaPesos = cajaPesos
        self.cajaDolares = cajaDolares
        self.tarjetaDebito= tarjetaDebito        
        self.costoTransferencias = costoTransferencias
        self.saldoDescubiertoDisponible = saldoDescubiertoDisponible
    
    def mostrarTipo(self):
        return print(self.tipo)
    