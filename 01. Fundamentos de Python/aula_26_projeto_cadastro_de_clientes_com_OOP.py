# Projeto: Cadastro de Clientes
# Regras:
# - Classe Pessoa (nome e idade)
# - Classe CLiente (email e LTV = Lifetime Value)
# Cadastre 2 clientes diferentes em uma lista
# Exiba a lista de todos os clientes cadastrados
# Extra: Exiba a soma dos LTV de todos os clientes

# Função Global Cabeçalho Tela de Cadastro de Clientes
def head():
    print('###### SISTEMA DE CADASTRO DE CLIENTES ######')
    print('---------------------------------------------')
    print('                                             ')

# Criando classe de pessoas e definindo método construtor
class People:
    def __init__(self, name, age):
        self.name = name
        self.age = age

# Criando classe de clientes e definindo método construtor
class Client(People):
    def __init__(self, name, age, email, ltv):
        super().__init__(name, age)
        self.email = email
        self.ltv = float(ltv)

    # Função que mostra informação dos clientes na tela
    def display_clients(self):
        print(f'Cliente: {self.name} | Idade: {self.age} | login: {self.email} | LTV: R$ {self.ltv:.2f}')

# list_of_clients = [] 
# clients.append(Client('João', 27, 'joao1998@gmail.com', 8960))

# Lista de Clientes
list_of_clients = [
    Client('João', 27, 'joao1998@gmail.com', 8960),
    Client('Maria', 35, 'maria_maria@gmail.com', 3300)
]

# Solicitando os dados do novo cliente a cadastrar
# name = input('Digite o nome do cliente: ').title()
# age = int(input('Digite a idade do cliente: '))
# email = input('Digite o email do cliente: ')
# ltv = float(input('Digite o LTV do cliente: '))

# # Adicionando novos clientes na lista list_of_clients[]
# new_client = Client(name, age, email, ltv)
# list_of_clients.append(new_client)

# Tela do cadastro de clientes
head()

# Soma de LTV Total
sum_total_ltv = 0

# Mostrando Lista de Clientes na tela
for client in list_of_clients:
    client.display_clients()
    sum_total_ltv += client.ltv

# Exibindo Soma dos LTV de todos os clientes
print('                                             ')
print('---------------------------------------------')
print(f'A soma total dos LTV é: {sum_total_ltv:.2f}')
print('---------------------------------------------')

