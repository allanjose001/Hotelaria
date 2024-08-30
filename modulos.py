'Projeto de IP 1º periodo'
'Feito por Alcielma Luzinete e Allan Jose'

def linha():
    print('\033[33m======================================\033[m')

def arquivo_existe():
    #verifica a existencia de um arquivo "hospd.csv" e se não houver cria um
    try:
        with open('hospd.csv', 'r'):
            return True
    except FileNotFoundError:
        with open('hospd.csv', 'w') as file:
            pass
        return False
    
def verificar():
    #verifica se há algo dentro do arquivo
    hospd = ler()
    return bool(hospd)

def escrever(hospd):
    #põe uma virgula entre os dados e os escreve no arquivo
    with open('hospd.csv', 'w') as arquivo:
            for hospede in hospd:
                arquivo.write(','.join(hospede) + '\n') 

def salvar(input):
    #salva um novo dado sem sobrepor dados antigos no arquivo
    with open ('hospd.csv', 'a') as arquivo:
        for conteudo in input:
            arquivo.write(','.join(conteudo) + '\n')

def ler():
    #le o arquivo e retorna ele como uma list comprehension
    with open('hospd.csv','r') as arquivo:
        tabela = arquivo.readlines()
        conteudo = [linha.strip().split(',') for linha in tabela]
        return conteudo

def visualizar():
    #percorre o arquivo de hospd e imprime todos os hospedes
    hospd = ler()
    print('\033[33m==============Hospedes=============\033[m')
    for nome, contato, quarto in hospd: #percorre todas as tuplas de nome, contato e quarto na list comprehension
        print(f'Nome: {nome}\nContato: {contato}\nQuarto: {quarto}')
        linha()

def buscar():
    hospd = ler()
    #compara o input inserido com todos os valores dentro da lista de hospedes,
    #imprime e retorna o hospede encontrado
    print('\033[33m=============================================\033[m')
    print('Digite o nome, contato ou quarto do hóspede: ')
    print('\033[33m=============================================\033[m')
    busca = input()
    
    encontrado = []
    
    #percorre a list "hospd" e verifica se o valor inserido em busca é igual a algo
    #se qualquer similaridade for encontrada adiciona o hospede a lista "encontrado" 
    for hospede in hospd: 
        if busca in hospede[0] or busca in hospede[1] or busca in hospede[2]:
            encontrado.append(hospede) 
    
    if encontrado:
        #imprime os hospedes encontrados
        print('\033[32mHóspede encontrado com sucesso!\033[m')
        linha()
        for x in encontrado:
            print(f'Nome: {x[0]}\nContato: {x[1]}\nQuarto: {x[2]}')
            linha()
        return encontrado

    else:
        print('\033[31mHóspede não encontrado.\033[m')

def cadastrar():
    #verifica se todos os itens foram inseridos corretamente, e os adiciona ao arquivo
    lista_erro = []
    hospd = []
    
    print('\033[33m===========================================\033[m')
    print('Insira o nome, contato e quarto do hóspede:')
    print('\033[33m===========================================\033[m')
    nome = input('Nome: ')
    contato = input('Contato: ')
    quarto = input('Quarto: ')

    #sessão de condições de erros
    if len(nome) > 50:
        lista_erro.append('- O nome deve ter no maximo 50 caracteres.')

    if not contato.isdigit():
        lista_erro.append('- O contato deve ter apenas números: ')

    if len(quarto)>3:
        lista_erro.append('- O quarto deve ter no maximo 2 caracteres.')
    
    if not quarto.isdigit():
        lista_erro.append('- O quarto deve ter somente números.')
    
    #verifica se o quarto inserido ja esta ocupado
    arquivo = ler()    
    quarto_ocupado = False
    for hospede in arquivo:
        if quarto == hospede[2]:
            quarto_ocupado = True
    
    if quarto_ocupado: 
        lista_erro.append('- Quarto ocupado.')
    
    if lista_erro:
        linha()
        print('Erro: ')
        for erro in lista_erro:
            print(erro)
        print('\033[31mCadastro cancelado.\033[m')
        linha()

    else: #se não houver erro algum, insere os dados dentro de hospd
        hospd.append([nome, contato, quarto])
        salvar(hospd)
        print('\033[32mHospede cadastrado com sucesso!\033[m')
        linha()

def editar():
    #busca hospedes pelo indice, armazena o indice e o manipula para editar o arquivo
    hospd = ler()
    print('\033[33m==============================================================\033[m')
    print('Digite o nome, contato ou quarto do hópede que deseja editar: ')
    print('\033[33m==============================================================\033[m')
    busca = input()
   
    encontrado = None

    #separa a lista em indice e "conteudo", verifica se é igual ao input inserido em busca
    #se existir compatibilidade, armazena o indice em encontrado
    for indice, hospede in enumerate(hospd):
        if busca in hospede[0] or busca in hospede[1] or busca in hospede[2]:
            encontrado = indice
            
    if encontrado is not None:
        linha()
        print('\033[32mHóspede encontrado.\033[m')
        print(f'Nome: {hospd[encontrado][0]}')
        print(f'Contato: {hospd[encontrado][1]}')
        print(f'Quarto: {hospd[encontrado][2]}')
        linha()
        
        #recebe os novos valores
        print('Digite as nova propriedades')
        nome = input('Novo nome: ')
        contato = input('Novo contato: ')
        quarto = input('Novo quarto: ')
        
        #sessão de condições de erros
        lista_erro = []

        if len(nome) > 50:
            lista_erro.append('- O nome deve ter no maximo 50 caracteres.')
    
        if not contato.isdigit():
            lista_erro.append('- O contato deve ter somente números. ')

        if len(quarto) > 3:
            lista_erro.append('- O quarto deve ter 2 números.')
        
        if not quarto.isdigit():
            lista_erro.append('- O quarto deve ter somente números.')
                    
        quarto_ocupado = False
        for hospede in hospd:
            #verifica se o quarto inserido ja esta ocupado
            #e se o quarto inserido é o mesmo que o hospede ja estava
            if quarto == hospede[2] and hospd[encontrado][2] != quarto:
                quarto_ocupado = True
        
        if quarto_ocupado: 
            lista_erro.append('- Quarto ocupado.')
        
        if lista_erro:
            linha()
            print('\033[31mErro\033[m')
            for erro in lista_erro:
                print(erro)
            print('\033[31mEdição cancelada.\033[m')
            linha()
              
        else:
            linha()
            print('Deseja mesmo editar este hóspede?\ndigite "\033[31msim\033[m" para confirmar.')
            linha()
            confirma = input()    

            if confirma.lower() == 'sim':    
                #se não houver nenhum erro edita a list comprehension
                hospd[encontrado][0] = nome
                hospd[encontrado][1] = contato
                hospd[encontrado][2] = quarto

                #sobrepõe o arquivo pela list comprehension    
                escrever(hospd)
                print('\033[32mHospede editado com sucesso!\033[m')
                linha()
            else:
                print('\033[31mEdição cancelada por usuario.\033[m')
    else:
        print('\033[31mNenhum hóspede encontrado.\033[m')

def excluir():
    #busca por um hospede e o remove do arquivo
    hospd = ler()
    busca = buscar() 
    
    if busca:
        print('deseja mesmo remover este hospede?\ndigite "\033[31msim\033[m" para confirmar')
        linha()
        confirma = input()
        if confirma.lower() == "sim": 
            #percorre o arquivo e o clona em formato de list comprehension,
            #se encontrar os dados inseridos na busca, não os copia, e prossegue com a clonagem
            novo_hospd = [conteudo for conteudo in hospd if conteudo not in busca]
            
            #sobrepõe o arquivo pela nova list comprehension 
            escrever(novo_hospd)
            print('\033[32mHospede removido com sucesso!\033[m')
            linha()
        else:
            print('\033[31mExclusão cancelada por usuario.\033[m')
    else:
        print('\033[31mNenhum hóspede excluido.\033[m')

def imprimir():
    print('''\033[33m===============\033[mMENU\033[33m================\033[m
1 - Visualisar todos os hóspedes
2 - Buscar hóspede
3 - Registrar novo hóspede
4 - Editar hóspede
5 - Excluir hóspede
6 - Parar sistema 
\033[33m==================================\033[m''')