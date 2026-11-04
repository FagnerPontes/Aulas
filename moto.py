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