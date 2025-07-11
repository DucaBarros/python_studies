# Função que mostra informação dos clientes na tela
def display_clients(name, age, email, ltv):
    print(f'Cliente: {name} | Idade: {age} | login: {email} | LTV: R$ {ltv:.2f}')

display_clients("Mario", 55, 'itsmemario@gmail.com', 10577)


