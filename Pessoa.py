class Pessoa:

    def __init__(self):
        self.__codigo = 123
        self.nome = None
        self._endereco = None
        self.__telefone = None
    
    def imprimeNome(self):
        print("Nome: ", self.nome)
    
    def __imprimeTelefone(self):
        print("Telefone: ", self.telefone)
    
    def getCodigo(self):
        return self.__codigo

    def getNome(self):
        return self.nome
    
    def setNome(self, valor):
        self.nome = valor
    
    def getEndereco(self):
        return self._endereco
    
    def setEndereco(self, valor):
        self._endereco = valor

    def getTelefone(self):
        return self.__telefone