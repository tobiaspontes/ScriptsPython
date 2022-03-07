# importando SQLite
import sqlite3 as lite

# criando conexão
con = lite.connect('dados.db')

# inserindo dados
def inserir(lista):
    with con:
        cur = con.cursor()
        query = 'INSERT INTO formulario (nome, email, telefone, dia_em, estado, assunto) VALUES (?, ?, ?, ?, ?, ?)'
        cur.execute(query, lista)

# consultando dados
def consulta():
    lista = []
    with con:
        cur = con.cursor()
        query = 'SELECT * FROM formulario'
        cur.execute(query)
        info = cur.fetchall()
        
        for i in info:
            lista.append(i)
    
    return lista


# atualizando dados
def atualizar(lista):
    with con:
        cur = con.cursor()
        query = 'UPDATE formulario SET nome=?, email=?, telefone=?, dia_em=?, estado=?, assunto=? WHERE id=?'
        cur.execute(query, lista)

# deletando dados
def deletar(id):
    with con:
        cur = con.cursor()
        query = 'DELETE FROM formulario WHERE id=?'
        cur.execute(query, id)