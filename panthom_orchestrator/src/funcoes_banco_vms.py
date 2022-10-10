import sqlite3
banco = sqlite3.connect("rpa_vms")

cursor = banco.cursor()

# # # cursor.execute("CREATE TABLE virtualMachines(id_vm text, status_vm text, processo_atual int)")
# # # cursor.execute("INSERT INTO virtualMachines VALUES ('#1','Livre',null)")
# # # informacoes = cursor.execute("DELETE FROM virtualMachines WHERE 'id_vm' = '#2'")
# # banco.commit()

def busca_vm():
    lista = []
    informacoes = cursor.execute("SELECT * FROM virtualMachines")
    for i in informacoes:
        lista.append(i)
    return lista

def altera_status(id_vm, id_processo, nm_sistema):
    cursor.execute(f"UPDATE virtualMachines SET status_vm='OCUPADA' WHERE id_vm='{id_vm}'")
    cursor.execute(f"UPDATE virtualMachines SET processo_atual = {id_processo}, nm_sistema = '{nm_sistema}' WHERE id_vm='{id_vm}'")
    # print(f"UPDATE virtualMachines SET processo_atual = {id_processo}, nm_sistema = '{nm_sistema}' WHERE id_vm='{id_vm}'")
    banco.commit()


# abc = cursor.execute("SELECT * FROM virtualMachines")
# for i in abc:
#     print(i)