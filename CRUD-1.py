def apresenteSe ():
    print('+-------------------------------------------------------------+')
    print('|                                                             |')
    print('| AGENDA PESSOAL DE ANIVERSÁRIOS E FORMAS DE CONTATAR PESSOAS |')
    print('|                                                             |')
    print('| Diogo                                                       |')
    print('| Yan                                                         |')
    print('| Abdom                                                       |')
    print('|                                                             |')
    print('| Versão 2.0 de 22/abril/2025                                 |')
    print('|                                                             |')
    print('+-------------------------------------------------------------+')

def umTexto (solicitacao, mensagem, valido):
    digitouDireito=False
    while not digitouDireito:
        txt=input(solicitacao)

        if txt not in valido:
            print(mensagem,'- Favor redigitar...')
        else:
            digitouDireito=True

    return txt

def opcaoEscolhida (mnu):
    print()

    opcoesValidas=[]
    posicao=0
    while posicao<len(mnu):
        print (posicao+1,') ',mnu[posicao],sep='')
        opcoesValidas.append(str(posicao+1))
        posicao+=1

    print()
    return umTexto('Qual é a sua opção? ', 'Opção inválida', opcoesValidas)


'''
Def de verificações abaixo
'''

def verificar_nome(frase):
    caracteres_invalidos = ['0','1','2','3','4','5','6','7','8','9','!','@','#','$','%','^','&','*','(',')','_','-','+','=','{','}','[',']','|',':','<','>','.','?','/','\\','"',"'",';']

    digitou_corretamente = False
    while not digitou_corretamente:
        nome = input(frase)
        
        posicao_nome = 0
        encontrou_invalido = False
        
        while posicao_nome < len(nome):
            posicao_caracter = 0
            while posicao_caracter < len(caracteres_invalidos):
                if nome[posicao_nome] in caracteres_invalidos[posicao_caracter]:
                    print('O nome não pode ter caractere especial ou número. Favor redigitar...')
                    encontrou_invalido = True
                    break  # achei um caracter, sai do while que verificava na primeira letra, se nãp ele vai para o proximo CARACTER INVALIDO
                posicao_caracter += 1

            if encontrou_invalido:
                break  # se eu encontrar o invalido, preciso finalizar o outro while, se nao eu verifico a PROXIMA LETRA
            posicao_nome += 1
            
        if nome in ' ':   #VERIFICAR DEPOIS
            print('O nome não pode estar vazio.Favor redigitar...') 
            encontrou_invalido=True
        if not encontrou_invalido: # não encontrei nada, nome ta correto
            digitou_corretamente = True

    return nome
    
def verificar_data(frase):
    digitou_corretamente=False
    while not digitou_corretamente:
        max = 0
        dia = 0
        mes = 0
        data=input(frase)
        if len(data)!=5 or data[2]!="/":
            print(' Sua data deve ser no formado Dia/Mês (exemplo: "25/02")')
        else:
            dia = int(data[:2])
            mes = int(data[3:])
            
            if mes < 1 or mes > 12:
                print("Mês invalido. Favor redigitar...")
            elif mes in [1,3,5,7,8,10,12]:
                max = 31
            elif mes in [4,6,9,11]:
                max = 30
            else: # so sobrou fevereiro que tem 29 dias
                max = 29
            
            if dia<1 or dia>max:
                print("Dia não existente nesse mes. Favor redigitar...")
            else:
                digitou_corretamente=True
    return (data)

def verificar_telefone(frase):
    
    digitos_validos = ['0','1','2','3','4','5','6','7','8','9']
    ddd_invalidos = [10, 20, 23, 25, 26, 29, 30, 36, 39, 40, 50, 52, 56, 57, 58, 59, 60, 70, 72, 76, 78, 80, 90]
   
    digitou_corretamente=False
    while not digitou_corretamente:
        encontrou_invalido = False
        posicao=0
        telefone=input(frase)
        
        if len(telefone) != 10:
            print("O número de telefone deve ter apenas números DDD + número (exemplo: 1940028922)")
            continue
        
        if len(telefone) == 10:
            while posicao < len(telefone):
                if telefone[posicao] not in digitos_validos:
                    encontrou_invalido = True
                    print("O telefone deve conter apenas números. Favor redigitar...")
                    break
                posicao += 1
                
        ddd=int(telefone[:2])
        if ddd in ddd_invalidos or ddd<10:
            print("Esse DDD digitado{ddd}, não é valido. Favor redigitar...")
            continue
        
        if not encontrou_invalido:
            digitou_corretamente = True
            
    return f"({telefone[:2]}){telefone[2:6]}-{telefone[6:]}"

def verificar_endereco(frase):
    digitou_corretamente = False
    
    while not digitou_corretamente:
        is_invalid = False
        street = input(frase)
        if not frase:
            is_invalid = True
            print("Digite alguma rua valida!! Favor Redigitar")
        elif len(street.strip()) < 3: # Verifica se a rua tem ao menos 3 carac
            is_invalid = True
            print("Endereço tem que possuir ao menos 3 caracteres! Favor Redigitar")

        clean_street = ''.join(i for i in street if i.isalpha() or i.isspace()) # Tira caracts especiais e numero, mantendo espaçamentos
        if not clean_street.strip():
            is_invalid = True
            print("A rua tem que conter caracteres alfabeticos! Favor Redigitar")

        if not is_invalid:
            digitou_corretamente = True
    return street
        
            
def verificar_celular(frase):

    digitos_validos = ['0','1','2','3','4','5','6','7','8','9']
    ddd_invalidos = [10, 20, 23, 25, 26, 29, 30, 36, 39, 40, 50, 52, 56, 57, 58, 59, 60, 70, 72, 76, 78, 80, 90]
   
    digitou_corretamente=False
    while not digitou_corretamente:
        encontrou_invalido = False
        posicao=0
        celular=input(frase)
        
        if len(celular) != 11:
            print("O número de telefone deve ter números contendo DDD + número (exemplo: 19999100688)")
            continue
        
        if len(celular) == 11:
            while posicao < len(celular):
                if celular[posicao] not in digitos_validos:
                    encontrou_invalido = True
                    print("O telefone deve conter apenas números. Favor redigitar...")
                    break
                posicao += 1
                
        ddd=int(celular[:2])
        if ddd in ddd_invalidos or ddd<10:
            print("Esse DDD digitado{ddd}, não é valido. Favor redigitar...")
            continue
        
        if not encontrou_invalido:
            digitou_corretamente = True
            
    return f"({celular[:2]}){celular[2:7]}-{celular[7:]}"

def verificar_email(frase):
    digitou_corretamente = False
    
    while not digitou_corretamente:
        email = input(frase)
        
        if ' ' in email:
            print("O e-mail não pode ter espaços. Favor redigitar...")
            continue
        
        if '@' not in email or '.' not in email:
            print("O e-mail deve conter '@' e '.' (exemplo: nome@email.com). Favor redigitar...")
            continue
        else:
            digitou_corretamente = True

    return email
    
    
'''cada parte do menu está abaixo.'''

def ondeEsta (nom,agd):
    inicio=0
    final =len(agd)-1
    
    while inicio<=final:
        meio=(inicio+final)//2
        
        if nom.upper()==agd[meio][0].upper():
            return [True,meio]
        elif nom.upper()<agd[meio][0].upper():
            final=meio-1
        else: # nom.upper()>agd[meio][0].upper()
            inicio=meio+1
            
    return [False,inicio]

def cadastrar (agd):
    digitouDireito=False
    while not digitouDireito:
        nome=verificar_nome('\nNome.......: ')

        resposta=ondeEsta(nome,agd)
        achou   = resposta[0]
        posicao = resposta[1]

        if achou:
            print ('Pessoa já existente - Favor redigitar...')
        else:
            digitouDireito=True
            
    aniversario=verificar_data('Aniversário: ')
    endereco   =verificar_endereco('Endereço...: ')
    telefone   =verificar_telefone('Telefone...: ')
    celular    =verificar_celular('Celular....: ')
    email      =verificar_email('e-mail.....: ')
    
    contato=[nome,aniversario,endereco,telefone,celular,email]
    
    agd.insert(posicao,contato)
    print('Cadastro realizado com sucesso!')

def procurar (agd):  #CONCLUIDO OQUE FOI PEDIDO
    # Ficar pedindo para digitar um nome até digitar um nome que existe
    # cadastrado;
    # mostrar então na tela TODOS os demais dados encontrados 
    # sobre aquela pessoa.
    digitouDireito=False
    while not digitouDireito:
        nome=input('\nNome.......: ')

        resposta=ondeEsta(nome,agd)
        achou   = resposta[0]
        posicao = resposta[1]

        if not achou:
            print ('Pessoa não cadastrada - Favor redigitar...')
        else:
            digitouDireito=True

    print('Aniversario:',agd[posicao][1])
    print('Endereço...:',agd[posicao][2])
    print('Telefone...:',agd[posicao][3])
    print('Celular....:',agd[posicao][4])
    print('e-mail.....:',agd[posicao][5])

def atualizar (agd): #CONCLUIDO O QUE FOI PEDIDO
    # Ficar mostrando um SUBMENU oferecendo as opções de atualizar aniversário, ou
    # endereco, ou telefone, ou celular, ou email, ou finalizar as
    # atualizações; ficar pedindo para digitar a opção até digitar uma
    # opção válida; realizar a atulização solicitada; até ser escolhida a
    # opção de finalizar as atualizações.
    # USAR A FUNÇÃO opcaoEscolhida, JÁ IMPLEMENTADA, PARA FAZER O MENU
    digitouDireito=False
    while not digitouDireito:
        nome=input('\nNome.......: ')

        resposta=ondeEsta(nome,agd)
        achou   = resposta[0]
        posicao = resposta[1]

        if not achou:
            print ('Pessoa não cadastrada - Favor redigitar...')
        else:
            digitouDireito=True

    deseja_terminar_o_programa=False
    while not deseja_terminar_o_programa:

        resposta=int(opcaoEscolhida(mini_menu))
    
        if resposta== 1:
            nome=verificar_nome('\nNovo Nome.......: ')
            agd[posicao][0]=nome
            print('\nCadastro atualizado com sucesso!')
        elif resposta== 2:
            aniversario=verificar_data('\nNovo Aniversário:  ')
            agd[posicao][1]=aniversario
            print('\nCadastro atualizado com sucesso!')
        elif resposta== 3:
            endereco=verificar_endereco('\nNovo Endereço...: ')
            agd[posicao][2]=endereco
            print('\nCadastro atualizado com sucesso!')
        elif resposta== 4:
            telefone=verificar_telefone('\nNovo Telefone...: ')
            agd[posicao][3]=telefone
            print('\nCadastro atualizado com sucesso!')
        elif resposta== 5:
            celular=verificar_celular('\nNovo Celular....: ')
            agd[posicao][4]=celular
            print('\nCadastro atualizado com sucesso!')
        elif resposta== 6:
            email=verificar_email('\nNovo e-mail.....: ')
            agd[posicao][5]=email
            print('\nCadastro atualizado com sucesso!')
        else:
            deseja_terminar_o_programa=True


    
def listar (agd): #CONCLUIDO OQUE FOI PEDIDO
    # implementar aqui a listagem de todos os dados de todos
    # os contatos cadastrados
    # printar aviso de que não há contatos cadastrados se
    # esse for o caso
    posicao=0
    while posicao<len(agd):
        
        print('Nome:......:',agd[posicao][0].upper())
        print('Aniversario:',agd[posicao][1])
        print('Endereço...:',agd[posicao][2])
        print('Telefone...:',agd[posicao][3])
        print('Celular....:',agd[posicao][4])
        print('e-mail.....:',agd[posicao][5])
        print()
        posicao+=1
        
def excluir (agd):
    print()
    
    digitouDireito=False
    while not digitouDireito:
        nome=input('Nome.......: ')
        
        resposta=ondeEsta(nome,agd)
        achou   = resposta[0]
        posicao = resposta[1]
        
        if not achou:
            print ('Pessoa inexistente - Favor redigitar...')
        else:
            digitouDireito=True
    
    print('Aniversario:',agd[posicao][1])
    print('Endereco...:',agd[posicao][2])
    print('Telefone...:',agd[posicao][3])
    print('Celular....:',agd[posicao][4])
    print('e-mail.....:',agd[posicao][5])

    resposta=umTexto('Deseja realmente excluir? ','Você deve digitar S ou N',['s','S','n','N'])
    
    if resposta in ['s','S']:
        del agd[posicao]
        print('Remoção realizada com sucesso!')
    else:
        print('Remoção não realizada!')

# daqui para cima, definimos subprogramas (ou módulos, é a mesma coisa)
# daqui para baixo, implementamos o programa
# (nosso CRUD, C=create(cadastrar), R=read(recuperar),
# U=update(atualizar), D=delete(remover,apagar)

apresenteSe()

agenda=[]

menu=['Cadastrar Contato',\
      'Procurar Contato',\
      'Atualizar Contato',\
      'Listar Contatos',\
      'Excluir Contato',\
      'Sair do Programa']

mini_menu=['Nome:',\
      'Aniversario:',\
      'Endereco',\
      'Telefone',\
      'Celular',\
      'e-mail',\
      'Finalizar alterações']

deseja_terminar_o_programa=False
while not deseja_terminar_o_programa:
    opcao = int(opcaoEscolhida(menu))

    if opcao==1:
        cadastrar(agenda)
    elif opcao==2:
        procurar(agenda)
    elif opcao==3:
        atualizar(agenda)
    elif opcao==4:
        listar(agenda)
    elif opcao==5:
        excluir(agenda)
    else: # opcao==6
        deseja_terminar_o_programa=True
        
print('PROGRAMA ENCERRADO COM SUCESSO!')
