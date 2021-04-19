from Pessoa import Pessoa

class Fisica:

    def __init__():
        self.__cpf = 123.456.789-00
        self.idade = None
        self.peso = None
        self.altura = None
    
    def imprimeCpf():
        print("CPF:", self.__cpf)
    
    def __calculaImc(self):
        resultado = self.peso/(self.altura*self.altura)
        print("IMC:", resultado)

    def getCpf(self):
        return self.__cpf
      
    def getIdade(self):
        return self.idade
    
    def setIdade(self, valor):
        self.idade = valor
    
    def getPeso(self):
        return self.peso
    
    def setPeso(self, valor):
        self.peso = valor
    
    def getAltura(self):
        return self.altura
    
    def setAltura(self, valor):
        self.altura = valor
