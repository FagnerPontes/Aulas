'''
herança em Python: classes filhas herdando da classe pai.
A função super().__init__(), dentro do construtor da classe filha,
serve para reaproveitar todo o código de inicialização que já existe no pai,
'''

from veiculo import veiculo

class carro(veiculo):

  __slots__ = ('portas', 'cavalos')

  def __init__(self, marca, modelo, ano, chassi, portas, cavalos):
    # super().__init__ puxa o construtor da classe pai (veiculo)
    super().__init__(marca, modelo, ano, chassi)

    # Atributos específicos da classe carro
    self.portas = portas
    self.cavalos = cavalos

  # Sobrescrita opcional do __str__ para incluir os novos dados
  def __str__(self):
    return f"Carro: {self.marca} {self.modelo}, Ano: {self.ano}, Portas: {self.portas}, Cavalos: {self.cavalos}cv, {self.get_chassi()}"