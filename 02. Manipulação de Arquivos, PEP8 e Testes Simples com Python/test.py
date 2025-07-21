with open('aula04-lista_de_compra.txt', 'r') as shop_list:
    for line in shop_list:
        print(f'{line.strip()}')

with open('aula04-lista_de_compra.txt', 'a') as shop_list:
    new_item = input('Digite o item: ')
    if new_item != "":
        shop_list.write(f'-{new_item}\n')
        print('')
        print('Item adicionado com sucesso!')
    else:
        print('Nenhum item foi inserido na lista!')
