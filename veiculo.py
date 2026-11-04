# classe veiculo
class veiculo:
    # Define rigidamente quais atributos a classe pode ter
    # Restring memória e destroi o __dict__
    __slots__ = ('marca', 'modelo', 'ano', '__chassi')

    # Método construtor (__init__)
    def __init__(self, marca, modelo, ano, chassi):

        # Atribuir valores dos parâmetros públicos
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        # Atribuir valores dos parâmetros privados
        self.__chassi = chassi 

    # Método genérico para exibir as informações do objeto
    def exibir_veiculo(self):
        # Chamar atributos dentro de strings: f"string {atrubuto}"
        print(f"veiculo: {self.marca} {self.modelo}, Ano: {self.ano}")

    # Método padrão para retornar uma string formatada do objeto
    def __str__(self):
        return f"veiculo: {self.marca} {self.modelo}, Ano: {self.ano}"

    def get(self):
        return(self.__dict__) #não funciona com __slots__ atributo interno da classe.

    def get_chassi(self):
        return self.__chassi

    def set_chassi(self, chassi):
        self.__chassi = chassi

"""
# Criando um objeto veiculo com os valores "Ford", "Mustang" e 2020
veiculo_1 = veiculo("Ford", "Mustang", 2020)

veiculo_1.exibir_veiculo()
print(veiculo_1)
print(veiculo_1.__dict__)
dict_veiculo_1 = veiculo_1.get()
print(dict_veiculo_1)
print(veiculo_1.marca)
print(veiculo_1.modelo)
print(veiculo_1.ano)


'''
Qual o significado do "__" antes e depois do nome?
Em Python, os dois sublinhados antes e depois do nome (como em __init__) são chamados de dunder (abreviação de double underscore, ou sublinhado duplo).

Eles indicam métodos especiais
Métodos reservados pelo interpretador
funções internas e de controle de fluxo que ele mesmo gerencia nos bastidores.

Execução automática:

Prevenção de conflitos: Esse formato serve para evitar que o programador crie acidentalmente um método customizado com o mesmo nome de funções internas do sistema.
'''


'''
Qual a função do self no parâmetro do construtor?
O self representa a instância atual do objeto que está sendo criada ou manipulada.

É uma ponte para que o objeto consiga acessar e modificar os seus próprios atributos e métodos.

Por que ele é necessário?
Quando você define uma classe, você está criando um "molde". A partir desse molde, você pode criar dezenas de objetos diferentes (vários veiculos, por exemplo). O Python precisa de uma forma de saber qual objeto específico está executando o código naquele momento.

Referência à instância criada e separação de dados: Se você criar dois veiculos diferentes (veiculo1 e veiculo2), o self garante que os dados do veiculo1 fiquem guardados nele próprio, sem misturar com os dados do veiculo2.
'''


'''
.items() pega todos os pares e 
.keys() pega todos os pares e list(...) 
.values() pega todos os pares e list(...) 
list(...) transforma oo dicionário em uma lista indexável
'''

#pegar os pares: atributo e valor:
primeiro_item = list(dict_veiculo_1.items())[0]
print(primeiro_item)

#pegar apenas o atributo:
primeira_chave = list(dict_veiculo_1.keys())[0]
print(primeira_chave)

#pegar apenas o valor:
primeiro_valor = list(dict_veiculo_1.values())[0]
print(primeiro_valor)

#lista: mutável - usamos []
Mustang = ["Ford", "Mustang", 2020]
veiculo_2 = veiculo(Mustang[0], Mustang[1], Mustang[2])
print(veiculo_2.__dict__)
Mustang[2] = 2021
veiculo_3 = veiculo(Mustang[0], Mustang[1], Mustang[2])
print(veiculo_3.__dict__)

#tupla: imutável - usamos ()
Corolla = ("Toyota", "Corolla", 2022)
#TypeError: 'tuple' object does not support item assignment
# Corolla[2] = 2021 
veiculo_4 = veiculo("Toyota", "Corolla", 2022)
print(veiculo_4.__dict__)

"""