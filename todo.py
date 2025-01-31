
toDo = []

while True:
    print('bem vindo a sua agenda de tarefas')
    print('''
        [1] Adicionar tarefa
        [2] Remover tarefa
        [3] Substituir tarefa
        [4] Sair
        ''')
    opcao = int(input('Selecione uma opcao:'))
    if opcao == 1:
        tarefa = input('Escreva a tarefa que deseja adicionar:')
        toDo.append(tarefa)
        print(f'PARABENS FI {tarefa} foi adicionado a sua lista de tarefas 🍺') 
        print('=====================================================================')
        print(f'Lista de tarefas: {toDo}')  

    elif opcao == 2:
        tarefa = input('Escreva a tarefa que deseja remover:')
        if tarefa not in toDo:
            print(f'FI {tarefa} nem esta na sua lista de tarefas 😵‍💫')
        elif tarefa in toDo:
            toDo.remove(tarefa)
            print(f'PUTSSS {tarefa} foi removido da lista de tarefas 🥴')
            print('=====================================================================') 
            print(f'Lista de tarefas: {toDo}')

    elif opcao == 3:
        print(f'Sua lista de tarefas até agora: {toDo}')
        tarefa = input('Escreva a tarefa que deseja substituir:')
        if tarefa not in toDo:
            print(f'FI {tarefa} nem esta na sua lista de tarefas 😵‍💫')
        elif tarefa in toDo:
            nova_tarefa = input('Escreva a nova tarefa:')
            toDo[toDo.index(tarefa)] = nova_tarefa
            print(f'Você trocou {tarefa} por {nova_tarefa} na sua lista de tarefas 🤯')
            print('=====================================================================') 
            print(f'Lista de tarefas: {toDo}')

    elif opcao == 4:
        print(toDo)
        print('=====================================================================') 
        print('Obrigado por usar a agenda de tarefas')
        break