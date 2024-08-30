'Projeto de IP 1º periodo'
'Feito por Alcielma Luzinete e Allan Jose'

import modulos

while True: #Menu em loop
    modulos.arquivo_existe()
    modulos.imprimir()
    
    try:
        menu = int(input())
    except ValueError:
        print('Entrada inválida.')
        continue

    if menu == 6: #parar sistema
        break

    elif menu == 1: #imprimir todos os hóspedes
        if modulos.verificar():
            modulos.visualizar()

            action = int(input('Digite 1 para retornar ao Menu\n'))
            if action == 1:
                continue
        else:
            print('Não há hóspedes cadastrados.')

    elif menu == 2: #buscar hospede
        while True:
            if modulos.verificar:
                modulos.buscar()
                
                action = int(input('1 - Retornar ao Menu\n2 - Buscar outro hospede\n'))
                if action == 1:
                    break
            else:
                print('Não há hóspedes cadastrados.')

    elif menu == 3: #cadastrar novo hospede
        while True:
            modulos.cadastrar()
           
            action = int(input('1 - Retornar ao Menu\n2 - Cadastrar outro hóspede\n'))
            if action == 1:
                break

    elif menu == 4: #editar hospede
        while True:
            if modulos.verificar:
                modulos.editar()
                
                action = int(input('1 - Retornar ao Menu\n2 - Editar outro hóspede\n'))
                if action == 1:
                    break
            else:
                print('Não há hóspedes cadastrados.')

    elif menu == 5: #excluir hospede
        while True:
            if modulos.verificar:
                modulos.excluir()
                
                action = int(input('1 - Retornar ao Menu\n2 - Excluir outro hóspede\n'))
                if action == 1:
                    break
            else:
                print('Não há hóspedes cadastrados.')

    else:
        print('Opção invalida.')