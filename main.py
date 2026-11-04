# Importação:
# 1. Mesmo diretório:
# from arquivo import Classe

# 2. Diretório filho (pasta abaixo):
# from pasta.arquivo import Classe

# 3. Diretório pai (pasta acima - UM nível acima):
# from ..arquivo import Classe  

# 4. Diretório avô (dois níveis acima):
# from ...arquivo import Classe

from veiculo import veiculo
from carro import carro
from moto import moto

# Criando objetos a partir do script externo

# Criando um objeto da classe filha 'carro'
meu_carro = carro("Ford", "Mustang", 2020, "ABC-1234", 2, 450)

# Criando um objeto da classe filha 'moto'
minha_moto = moto("Honda", "CB 500", 2022, "XYZ-9876", 500)

print(meu_carro.__dict__)
print(minha_moto.__dict__)




'''
veiculo_1 = veiculo("Ford", "Mustang", 2020, "KFJ5309")

# Usando os objetos normalmente
print(veiculo_1.marca)
print(veiculo_1.modelo)
print(veiculo_1.ano)
# print(veiculo_1.__placa)
print(veiculo_1.get_placa())

veiculo_1.modelo = "Focus"
print(veiculo_1.marca)
print(veiculo_1.modelo)
print(veiculo_1.ano)
# print(veiculo_1.__placa)
print(veiculo_1.get_placa())

veiculo_1.set_placa("LDO6587")
print(veiculo_1.get_placa())
'''
