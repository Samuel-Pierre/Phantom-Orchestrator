import cx_Oracle as cx

def select():
    dsn1 = cx.makedsn('172.31.3.251','1533','VAS11ANL')
    try:
        con = cx.connect(user=r'AMBDEV', password='AMB1TE_yT', dsn = dsn1)

        print('Conexão efetuada com sucesso')
        crsr = con.cursor()
<<<<<<< .mine
        select_in_banco = crsr.execute("SELECT id_protocolo,NR_PROTOCOLO FROM rpa_protocolo WHERE id_status = 1 ORDER BY DT_ABERTURA")
||||||| .r5256
        select_in_banco = crsr.execute("SELECT id_protocolo,nm_sistema FROM rpa_protocolo WHERE rpa_status_id = 1 ORDER BY DT_ABERTURA")
=======
        select_in_banco = crsr.execute("SELECT a.id_protocolo, a.id_projeto, b.nm_projeto FROM rpa_protocolo a, rpa_projeto b WHERE id_status = 1 AND a.id_projeto = b.id_projeto ORDER BY a.dt_abertura")
>>>>>>> .r5267
        for i in select_in_banco:
            id_protocolo = str(i[0])
            nm_sistema = str(i[1]) 
            break
        return id_protocolo, nm_sistema
    except:
<<<<<<< .mine
        print("Erro na conexão")


print(select())||||||| .r5256
        print("Erro na conexão")
=======
        print("Erro na conexão")>>>>>>> .r5267
