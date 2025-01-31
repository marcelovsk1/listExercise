
lista_de_compras = []

while True:
    print('''
        [1] Adicionar item
        [2] Remover item
        [3] Substiuir item
        [4] Sair
        ''')
    opcao = int(input('Digite uma opcao:')) 
    if opcao == 1:
        item = input('Digite o item que deseja adicionar:')
        lista_de_compras.append(item)
        print(f'UHULLL {item} foi adicionado a lista de compras 🍺')
        print("=====================================================================")
        print(f'Lista de compras: {lista_de_compras}')

    elif opcao == 2:
        item = input('Digite o item que deseja remover:')
        if item not in lista_de_compras:
            print(f'FI {item} nem esta na sua lista de compras 😵‍💫')
        elif item in lista_de_compras:
            lista_de_compras.remove(item)
            print(f'PUTSSS {item} foi removido da lista de compras 🥴')
            print("=================================================================")
            print(f'Lista de compras: {lista_de_compras}')
        elif lista_de_compras == []:
            print('Sua lista de compras esta vazia')

    elif opcao == 3:
        print(f'Sua lista de compras até agora: {lista_de_compras}')
        item = input('Digite o item que deseja substituir:')
        if item not in lista_de_compras:
             print(f'FI {item} nem esta na sua lista de compras 😵‍💫')
        elif item in lista_de_compras:
            novo_item = input('Digite o novo item:')
            lista_de_compras[lista_de_compras.index(item)] = novo_item
            print(f'Você trocou {item} por {novo_item} na sua lista de compras 🤯')
            print("=================================================================")
            print(f'Lista de compras: {lista_de_compras}')

    elif opcao == 4:
        print(lista_de_compras)
        print("=================================================================")
        pagamento = input('CREDITO OU DEBITO MEU PATRAO?\n[1] CREDITO\n[2] DEBITO\n[3] FIADO\n')
        while True:
            try:
                opcao_pagamento = int(pagamento)
                if opcao_pagamento == 1:
                    print('Só nao parcela em 12x meu patrao que eh nois flw')
                    print(lista_de_compras)
                    lista_de_compras.clear()
                    break 
                elif opcao_pagamento == 2:
                    print('DEBITO ai sim em fi ta podendo, vlw eh nois')
                    print(lista_de_compras)
                    lista_de_compras.clear()
                    break
                elif opcao_pagamento == 3:
                    print('FIADO? VAI TRABALHAR VAGABUNDO')
                    lista_de_compras.clear()
                    break
                else:
                    print('Opcao invalida. Tente novamente.')
            except ValueError:
                print('Entrada invalida. Digite um numero.')


# Whi
