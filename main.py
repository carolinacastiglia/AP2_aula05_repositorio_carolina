from Pessoa import Pessoa

print('-----PESSOA------')
p1 = Pessoa()
p1.setNome("Arnaldo")
p1.setEndereco("Rua Angelo Crivellaro")
p1.imprimeNome()

print("Endereço de", p1.nome,":", p1._endereco)
print('--------------------\n')