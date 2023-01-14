import mysql.connector

conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='Quimera!ms0',
    database='financas',
)
cursor = conexao.cursor()

# CRUD

# CREATE
#idlancamentos = 4
#origem = "Elo"
#valor = 1005.98

#comando = f'INSERT INTO lancamentos (idlancamentos, origem, valor) VALUES ({idlancamentos}, "{origem}", {valor})'
#cursor.execute(comando)
#conexao.commit() # edita o banco de dados


# READ
comando = f'SELECT * FROM lancamentos'
cursor.execute(comando)
resultado = cursor.fetchall() # ler o banco de dados
print(resultado)


# UPDATE
#valor = 59.6
#comando = f'UPDATE lancamentos SET valor = {valor} WHERE idlancamentos = 1'
#cursor.execute(comando)
#conexao.commit() # edita o banco de dados

# DELETE
#comando = f'DELETE FROM lancamentos WHERE idlancamentos = 1'
#cursor.execute(comando)
#conexao.commit() # edita o banco de dados


cursor.close()
conexao.close()
