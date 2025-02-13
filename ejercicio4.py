class CuentaBancaria:
    def __init__(self, deposito, retirada, saldo, saldoTotal):
        self.deposito=deposito
        self.retirada=retirada
        self.saldo=saldo
        self.saldoTotal=saldoTotal

    def mostrar_deposito(self):
        print(f"Su deposito ha sido de {self.deposito}")

    def mostrar_retirada(self):
        print(f"Ha retirado usted {self.retirada}")

    def mostrar_saldo(self):
        print(f"Su saldo es {self.saldo}")   

    def saldo_total(self):
        self.saldoTotal=self.saldo-self.retirada+self.deposito
        print(f"Su saldo total es {self.saldoTotal}")

cuenta_actual=CuentaBancaria(500, 300, 1000, "")
cuenta_actual.saldo_total()