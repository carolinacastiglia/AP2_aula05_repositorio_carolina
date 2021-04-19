from Pessoa import Pessoa
from Fisica import Fisica

print('-----PESSOA------')
p1 = Pessoa()
p1.setNome("Arnaldo")
p1.setEndereco("Rua Angelo Crivellaro")
p1.imprimeNome()

print("Endereço de", p1.nome,":", p1._endereco)
print('--------------------\n')

print('-----FÍSICA------')
f1 = Fisica()
f1.setAltura(154)
f1.setIdade(28.0)
f1.setPeso(60.2)

f1.setNome("Rubens")
f1.setEndereco("Avenida Protasio Alves")

f1.imprimeNome()
f1.imprimeCpf()
print("Endereço de",f1.nome,":", f1._endereco)

print("Altura:",f1.altura,"cm - Idade:",f1.idade,"anos - Peso:",f1.peso,"kg")
print('--------------------\n')