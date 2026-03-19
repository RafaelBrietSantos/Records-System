import csv
import os
from datetime import datetime


        

def limpar_tela():
    
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


limpar_tela()
print('Sistema de Loja Iniciado!')


def visualizar():
    limpar_tela()
    arquivo = 'treino.csv'
    if not os.path.exists(arquivo):
        print('📭 O arquivo ainda não existe.')
        return
    print(f'{'NOME':<20} | {'PROTOCOLO':<12} | {'STATUS':<12} | {'DATA'}')
    print('-' * 70)

    with open(arquivo, 'r', encoding='utf-8') as csvfile:
        leitor = csv.DictReader(csvfile, delimiter=';')
        for linha in leitor:
            
            print(f'{linha['name']:<20} | {linha['protocolo']:<12} | {linha['status']:<12} | {linha['data']}')
    
    input('\nPressione Enter para voltar ao menu...')



def introduzir():
    colnas = ['name', 'protocolo', 'status', 'data']
    arquivo = 'treino.csv'
    data_hoje_completa = datetime.now().strftime('%d/%m/%Y %H:%M')
    dia_atual = datetime.now().strftime('%d/%m/%Y')

    ultima_data_gravada = None
    if os.path.isfile(arquivo):
        with open(arquivo, 'r', encoding='utf-8') as f:
            leitor = list(csv.DictReader(f, delimiter=';'))
            if leitor:
                
                ultima_linha = leitor[-1]['data']
                ultima_data_gravada = ultima_linha.split(' ')[0]
    

    with open(arquivo, 'a', newline='', encoding='utf-8') as csvfile:
        escritor = csv.DictWriter(csvfile, fieldnames=colnas, delimiter=';')

        
        if ultima_data_gravada != dia_atual:
            separador = {
                'name': f'---------- {dia_atual} ----------', 
                'protocolo': '----------', 
                'status': '----------', 
                'data': dia_atual
                }
            escritor.writerow(separador)


        name = input('Nome: ')
        protocolo = input('Protocolo: ') 
        stats = input('Status: ')
        
            

        escritor.writerow({'name': name, 'protocolo': protocolo, 'status': stats, 'data': data_hoje_completa})

        print(f'✅ {name} salvo com sucesso!')
        input('\nPressione Enter para voltar ao menu...')

def excluir():
    limpar_tela()
    arquivo = 'treino.csv'

    file_exists = os.path.isfile('treino.csv')
    if not file_exists:
            print('Nao existe Nenhum dado de hj ') 
            return
    
    colnas = ['name', 'protocolo', 'status','data']

    tabela_antiga = []
    
    with open(arquivo, 'r', newline='', encoding='utf-8') as csvfile:
        leitor = csv.DictReader(csvfile, delimiter=';')
        for ID in leitor:
            tabela_antiga.append(ID)

    new_tabela = []

    print('Digite o Protocolo para excluir')
    algo = input('Protocolo: ')
    

    for item in tabela_antiga:
        if item['name'].startswith('---') :
            new_tabela.append(item)
            continue
        if item['protocolo'] != algo:
            new_tabela.append(item)

    with open(arquivo, 'w', newline='', encoding='utf-8') as csvfile:
        escritor = csv.DictWriter(csvfile, fieldnames=colnas, delimiter=';')
        escritor.writeheader()
        for passar in new_tabela:
            escritor.writerow(passar)

    print('❌Excluido coom sucesso!❌')
    input('\nPressione Enter para voltar ao menu...')
    

        
        


# MENU PRINCIPAL 


while True:
    limpar_tela()
    print('Sabesp Records System... ')
    print('1-  Introdzir Cadastro  ')
    print('2-  Excluir Cadastro ')
    print('3-  Editar Cadastro')
    print('4-  Visualizar')
    print('0-  Sair \n')

    user = input('Digite um dos numeros cima: ')

    if user == '1':
        introduzir()

    elif user == '2':
        excluir()

    elif user == '4':
        visualizar()

    elif user == '0':
        print('Saindo do sistema...')
        break


    
     

    
   