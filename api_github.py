import json
import requests

# Entrada de dado do usuário que deseja obter os dados do Github
usuario_github = input('Digite o nome de seu usuário do github para registrar seus dados. ')

link_github = f'https://api.github.com/users/{usuario_github}'

# Conexão para acessar os dados da API do Github
request = requests.get(link_github)

# Dados transformados em Json para visualização
dados_github = json.loads(request.content)


def registro_bd():  # Função para registrar os dados do usuário no Banco de dados
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
