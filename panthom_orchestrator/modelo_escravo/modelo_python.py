import subprocess
import sqlite3
import time

# 1  = segunda via
# 2 = termino oferta
# 3 = falha de venda
# 4 = contestacao interrupcao de servicos
# 5 = proativo
# 6 = data de corte dacc
# 7 = devolucao cc
# 8 = abertura ars

banco = sqlite3.connect("C:/SVNRobo/desenvolvimento/tahto/proativo/credito/futuro/teste_python/panthom_orchestrator/rpa_vms")
cursor = banco.cursor()
	
def chama_processo(nm_sistema):
    if nm_sistema == '5':
        nm_sistema_f = 'proativo_credito_futuro.bat'

    elif nm_sistema == '8':
        nm_sistema_f = 'abertura_ars.bat'

    elif nm_sistema == '1':
        nm_sistema_f = 'segunda_via.bat'

    elif nm_sistema == '7':
        nm_sistema_f = 'devolucao_cc.bat'

    elif nm_sistema == '6':
        nm_sistema_f = 'data_corte.bat'

    elif nm_sistema == '3':
        nm_sistema_f = 'falha_venda.bat'

    elif nm_sistema == '2':
        nm_sistema_f = 'termino_oferta.bat'

    elif nm_sistema == '4':
        nm_sistema_f = 'contestacao_interrupcao_servicos.bat'

    else:
        print('O robo nao consegue encontrar')
        
    path = f'C:/SVNRobo/desenvolvimento/tahto/proativo/credito/futuro/teste_python/bats/{nm_sistema_f}'
    subprocess.call([path])

while True:
    lista = []
    query = cursor.execute("SELECT processo_atual, nm_sistema FROM virtualMachines WHERE id_vm='#1'")

    for i in query:
        lista=i

    if lista[1] != '':
        print('processando ' + str(lista[0]) + ', ' + str(lista[1]))
        chama_processo(lista[1])
        cursor.execute(f"UPDATE virtualMachines SET status_vm='LIVRE' WHERE id_vm='#1'")
        cursor.execute(f"UPDATE virtualMachines SET processo_atual = NULL, nm_sistema = '' WHERE id_vm='#1'")
        banco.commit()

    else:
        print('esperando')
        time.sleep(10)