'''
herança em Python:
Criar as classes filhas herdando da classe pai veiculo.
O segredo principal na herança é usar a função super().__init__() dentro do construtor da classe filha. Isso serve para reaproveitar todo o código de inicialização que já existe no pai, evitando que você precise reescrever a atribuição de marca, modelo, ano e placa.
'''

from veiculo import veiculo

class moto(veiculo):

  def __init__(self, marca, modelo, ano, placa, cilindradas):
    # Puxa o construtor do pai
    super().__init__(marca, modelo, ano, placa)

    # Atributo específico da classe moto
    self.cilindradas = cilindradas

  # Sobrescrita opcional do __str__
  def __str__(self):
    return f"Moto: {self.marca} {self.modelo}, Ano: {self.ano}, Cilindradas: {self.cilindradas}cc"