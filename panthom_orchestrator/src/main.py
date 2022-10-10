from datetime import datetime
import time

import conexao_banco_tahto
import funcoes_banco_vms


def main():
    resultQuery = conexao_banco_tahto.select()
    print(resultQuery)
    escolhe_vm(resultQuery[0], resultQuery[1])

    with open(f'C:\\SVNRobo\\desenvolvimento\\tahto\\proativo\\credito\\futuro\\teste_python\\logs\\logs.txt', 'a') as arquivo:
        arquivo.write("Processo Executado \n")
        arquivo.write(str(datetime.now()) + '\n'+ str(resultQuery[0])+ ' '+ str(resultQuery[1]) + "\n\n")
        arquivo.close()


def escolhe_vm(id_processo, nm_sistema):
    vm_livres = funcoes_banco_vms.busca_vm()
    contador = 0
    for i in vm_livres:
        if str(i[1]) == 'LIVRE':
            funcoes_banco_vms.altera_status(i[0], id_processo, nm_sistema)
            break


        contador+=1
        if contador == len(vm_livres):
            print('Não há vms disponiveis')
            time.sleep(2*60)


while True:
    main()