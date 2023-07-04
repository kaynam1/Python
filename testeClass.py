class _Conta:
    def __init__(self, id: object, cpf: object, nome: object, saldo: object) -> object:
        self._id = id
        self._cpf = cpf
        self._nome = nome
        self._saldo = saldo
    @property
    def get_saldo(self):
        return self._saldo

    def __str__(self):
        return f"Conta [id= {self._id}, cpf= {self._cpf}, nome= {self._nome}, saldo= {self._saldo}]"

    def set_deposito(self, valor):
        self._saldo += valor

    def set_saque(self, valor):
        self._saldo -= valor

conta1 = _Conta(151, 123456789, "Kay", 1900.50)

conta2 = _Conta(123, 987653412, 'Ana', 1243.09)

valor_deposito = float(input('Digite o valor do deposito: '))
conta1.set_deposito(valor_deposito)

print(conta1.get_saldo)

valor_saque = float(input('Digite o valor de saque: '))
conta2.set_saque(valor_saque)

print(conta2.get_saldo)
