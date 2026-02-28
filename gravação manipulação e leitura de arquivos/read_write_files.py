"""
    Por que usar arquivos?
    
    Função open()
        escreve e lê arquvios
"""

with open('dados.txt', 'w') as f:
    f.write("Olá mundo")

with open('dados.txt', 'r') as f:
    conteudo = f.read()

print(conteudo)