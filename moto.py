'''
herança em Python: classes filhas herdando da classe pai.
A função super().__init__(), dentro do construtor da classe filha,
serve para reaproveitar todo o código de inicialização que já existe no pai,
'''

from veiculo import veiculo

class moto(veiculo):

  __slots__ = ('cilindradas')

  def __init__(self, marca, modelo, ano, chassi, cilindradas):
    # Puxa o construtor do pai
    super().__init__(marca, modelo, ano, chassi)

    # Atributo específico da classe moto
    self.cilindradas = cilindradas

  # Sobrescrita opcional do __str__
  def __str__(self):
    return f"Moto: {self.marca} {self.modelo}, Ano: {self.ano}, Cilindradas: {self.cilindradas}cc, {self.get_chassi()}"