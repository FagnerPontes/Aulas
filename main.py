# Importação:
# from arquivo import Classe # 1. Mesmo diretório
# from pasta.arquivo import Classe # 2. um diretório abaixo
# from ..arquivo import Classe  # 3. um diretório acima
# from ...arquivo import Classe # 4. dois diretórios acima

from carro import carro
from moto import moto

# Criando objetos a partir do script externo

# Criando um objeto da classe filha 'carro'
c1 = carro("Ford", "Mustang", 2020, "123456QWERTY", 2, 450)

# Criando um objeto da classe filha 'moto'
m1 = moto("Honda", "CB 500", 2022, "098765POIUYT", 500)

# print(c1.__dict__) #não funciona com __slots__
# print(m1.__dict__)

print(c1)
print(m1)
print(m1.get_chassi())


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
