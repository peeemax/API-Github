import json

import requests

usuario_github = input('Digite o nome de seu usuário do github para registrar seus dados. ')

link_github = f'https://api.github.com/users/{usuario_github}'

request = requests.get(link_github)

dados_github = json.loads(request.content)


def registro_bd():
    # Conexão com banco de dados
    import mysql.connector
    conexao = mysql.connector.connect(
        host='localhost',
        user='Maximiano',
        password='Pemax1992',
        database='formulario-lead',
    )

    cursor = conexao.cursor()

    # Comando para inserir e salvar dados inputados no banco de dados
    comando = f'INSERT INTO github_data (githubdata) VALUES ' \
              f'("{dados_github}")'
    cursor.execute(comando)
    conexao.commit()

registro_bd()


