'''
Para criar as classes filhas herdando da classe pai veiculo, você vai usar a herança em Python.

O segredo principal na herança é usar a função super().__init__() dentro do construtor da classe filha. Isso serve para reaproveitar todo o código de inicialização que já existe no pai, evitando que você precise reescrever a atribuição de marca, modelo, ano e placa.
'''

from veiculo import veiculo

class carro(veiculo):

  def __init__(self, marca, modelo, ano, placa, portas, cavalos):
    # super().__init__ puxa o construtor da classe pai (veiculo)
    super().__init__(marca, modelo, ano, placa)

    # Atributos específicos da classe carro
    self.portas = portas
    self.cavalos = cavalos

  # Sobrescrita opcional do __str__ para incluir os novos dados
  def __str__(self):
    return f"Carro: {self.marca} {self.modelo}, Ano: {self.ano}, Portas: {self.portas}, Cavalos: {self.cavalos}cv"