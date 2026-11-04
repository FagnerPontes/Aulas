serve para isolar as dependências e bibliotecas de um projeto Python específico.

As principais utilidades e vantagens de utilizá-lo são:

Isolamento de Versões: Permite que diferentes projetos utilizem versões distintas da mesma biblioteca sem que ocorram conflitos (por exemplo, o Projeto A usa o Django 4.0 e o Projeto B usa o Django 5.0 na mesma máquina).

Limpeza do Sistema: Evita poluir o ambiente Python global do seu sistema operacional com pacotes que você só precisa para aquele projeto específico.

Reprodutibilidade e Compartilhamento: Facilita a criação de arquivos de dependências (como o requirements.txt), garantindo que qualquer pessoa (ou servidor) possa instalar exatamente as mesmas versões de pacotes necessárias para rodar o seu código.

# LINUX
# Instalação (apenas se a criação falhar com erro de ensurepip):
sudo apt install python3-venv

# Criação do ambiente:
python3 -m venv venv

# Ativação:
source venv/bin/activate

# WINDOWS:
## Criar o ambiente
python -m venv venv

## Ativar no PowerShell
venv\Scripts\Activate.ps1

## Ativar no CMD
venv\Scripts\activate.bat