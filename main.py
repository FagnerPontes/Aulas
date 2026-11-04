# Importação:
# from arquivo import Classe # 1. Mesmo diretório:
# from pasta.arquivo import Classe # 2. Diretório filho (pasta abaixo):
# from ..arquivo import Classe  # 3. Diretório pai (pasta acima - UM nível acima):
# from ...arquivo import Classe # 4. Diretório avô (dois níveis acima):

from carro import carro
from moto import moto

# Criando objetos a partir do script externo

# Criando um objeto da classe filha 'carro'
meu_carro = carro("Ford", "Mustang", 2020, "123456QWERTY", 2, 450)

# Criando um objeto da classe filha 'moto'
minha_moto = moto("Honda", "CB 500", 2022, "098765POIUYT", 500)

# print(meu_carro.__dict__) #não funciona com __slots__
# print(minha_moto.__dict__)

print(meu_carro)
print(minha_moto)
print(minha_moto.get_chassi())


'''
veiculo_1 = veiculo("Ford", "Mustang", 2020, "KFJ5309")

# Usando os objetos normalmente
print(veiculo_1.marca)
print(veiculo_1.modelo)
print(veiculo_1.ano)
# print(veiculo_1.__chassi)
print(veiculo_1.get_chassi())

veiculo_1.modelo = "Focus"
print(veiculo_1.marca)
print(veiculo_1.modelo)
print(veiculo_1.ano)
# print(veiculo_1.__chassi)
print(veiculo_1.get_chassi())

veiculo_1.set_chassi("LDO6587")
print(veiculo_1.get_chassi())
'''
