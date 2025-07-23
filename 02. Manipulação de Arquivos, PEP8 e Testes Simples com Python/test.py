
# Classe List
class List:                             # Criando a classe lista
    def __init__(self, name):           # Definindo o método construtor da lista
      self._filename = f'{name}.txt'    # Salvando o nome do arquivo em uma variável protegida

    def get_list(self):                             # Definindo a função para pegar a list
        list = []                                   # Criando a lista
        with open(self._filename, 'r') as file:     # Usando um métido para ler os itens da lista
          for item in file:                         # Loop para verificar os itens da lista após a abertura
            list.append(item.strip())               # Adicionando os itens na lista
        return list                                 # Retorna a lista pronta
    

list = List('Lista')
for item in list.get_list():
   print(f'- {item}')

