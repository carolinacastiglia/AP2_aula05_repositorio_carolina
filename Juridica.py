from Pessoa import Pessoa

class Juridica(Pessoa):

    def __init__(self):
        Pessoa.__init__(self)
        self.__cnpj = '11222333444455'
        self.__inscricaoEstadual = '3456'
        self.quantidadeFuncionarios = None

    def imprimeCnpj(self):
        print("CNPJ:", self.__cnpj)

    def __emitirNotaFiscal(self):
        print("Nota Fiscal:")
    
    def getCnpj(self):
        return self.__cnpj
    
    def getInscricaoEstadual(self):
        return self.__inscricaoEstadual
       
    def getQuantidadeFuncionarios(self):
        return self.getQuantidadeFuncionarios
    
    def setQuantidadeFuncionarios(self, valor):
        self.quantidadeFuncionarios = valor