
from collections import defaultdict

#&  |  ~  ^ -> OPERADORES BINARIOS

try:
    from contextlib import contextmanager
    from mysql import connector
except ModuleNotFoundError:
    print("mysql connector nao instalado")
else:
    print("mysql connector instalado e pronto")

def maneira_um():
    conexao = connector.connect(
        host="localhost", 
        port=3306,
        user="",
        passwd=""
    )

    cursor = conexao.cursor()
    cursor.execute("CREATE DATABASE IF NOT EXISTS agenda")
    cursor.execute("SHOW DATABASES")

    for i,database in enumerate(cursor,start=1):
        print(f"BANCO DE DADOS {i}: {database[0]}")

def maneira_dois():
    @contextmanager
    def nova_conexao():
        conexao = connector.connect(**parametros)
        try:
            yield conexao
        finally:
            if conexao and conexao.is_connected():
                conexao.close()

    parametros = dict(
        host="localhost", 
        port=3306,
        user="",
        passwd=""
    )

    table_contato = """
        CREATE TABLE IF NOT EXISTS contatos(nome VARCHAR(50),tel VARCHAR(40))
    """
    
    table_emails = """
        CREATE TABLE IF NOT EXISTS emails(
            id INT AUTO_INCREMENT  PRIMARY KEY,
            dono VARCHAR(50)
        )
    """

    table_grupo = """
        CREATE TABLE IF NOT EXISTS grupos(
            id INT AUTO_INCREMENT PRIMARY KEY,
            descricao VARCHAR(30)
        )
    """

    alter_contato_ = """
        ALTER TABLE contatos ADD grupo_id INT
    """

    alter_contato = """
        ALTER TABLE contatos ADD FOREIGN KEY (group_id)
        REFERENCES grupos(id)
    """

    drop_table = "DROP TABLE emails"

    listar_tabelas = "SHOW TABLES"

    use_database = "USE agenda"

    update = "UPDATE contatos SET nome =%s WHERE id = %s"
    arg = ("ARTORIAS",0)

    alter = "ALTER TABLE contatos ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY"

    insert = "INSERT INTO contatos (nome,tel) VALUES (%s,%s)"
    args = ("ARTORiAS","9874572")
    args_ = (
                ("ARTORiAS 1","9874572"),
                ("ARTORiAS 2","9872"),
                ("ARTORiAS 3","98572"),
                ("ARTORiAS 4","984572"),
                ("ARTORiAS 5","874572")
             )
    
    select = "SELECT * FROM contatos"
    select_compacto = "SELECT nome,tel FROM contatos"
    select_where = "SELECT nome,tel FROM contatos WHERE nome = 'ARTORiAS'"
    select_where_like = "SELECT nome,tel FROM contatos WHERE nome LIKE '%A%'"
    select_where_like_order = "SELECT nome,tel FROM contatos ORDER BY nome DESC"
    select_where_limit = "SELECT nome,tel FROM contatos LIMIT 5 OFFSET 8"

    deletes = "DELETE FROM contatos WHERE id = 1"

    selecionar_grupo = "SELECT id FROM contatos WHERE descricao = %s"
    atualiza_contato = "UPDATE contatos SET grupo_id = %s WHERE nome = %s"
    contato_grupo = {
        "anas":"casa",
        "retor":"casa"
    }

    join = """
        SELECT
            grupos.descricao as grupo,
            contatos.nome as contato
        FROM contatos
        INNER JOIN grupos ON contatos.grupo_id = grupos.id
        ORDER BY grupo,contato
    """

    try:
        with nova_conexao() as conexao:
            try:
                if conexao.is_connected():
                    cursor = conexao.cursor()
                    cursor.execute(use_database)
                    cursor.execute(table_emails)
                    cursor.execute(table_contato)
                    cursor.execute(table_grupo)
                    cursor.execute(alter_contato_)
                    cursor.execute(alter_contato)
                    cursor.execute(alter)
                    cursor.executemany(insert,args_)
                    cursor.execute(insert,args)
                    conexao.commit()
                    
                    cursor.execute(select_compacto)
                    cursor.execute(select_where)
                    cursor.execute(select_where_like)
                    cursor.execute(select_where_like_order)
                    cursor.execute(select_where_limit)
                    contatos = cursor.fetchall(select)

                    for contato,grupo in contato_grupo:
                        cursor.execute(selecionar_grupo,(grupo,))
                        grupo_id = cursor.fetchone()[0]
                        cursor.execute(atualiza_contato,(grupo_id,contato))
                        conexao.commit()

                    cursor.execute(update,arg)

                    cursor.execute(deletes)

                    cursor.execute(listar_tabelas)
                    for i,database in enumerate(cursor,start=1):
                        print(f"BANCO DE DADOS {i}: {database[0]}")
                    
                    tables = [table[0] for table in cursor.fetchall()]
                    if 'emails' in tables:
                        cursor.execute(drop_table)
                        cursor.fetchall()

                    cursor.close()
                    cursor - conexao.cursor(dictionary=True)
                    cursor.execute(join)
                    contatos = cursor.fetchall()

                    agrupados = defaultdict(list)
                    for contato in contatos:
                        agrupados[contato["grupo"]].append(contato["nome"])
            except Exception as e:
                print("ERROR ", e)

            finally:
                cursor.close()
    except:
        print("ERROR POR FORA")
   
maneira_dois()