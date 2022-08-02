

class Lead:

    def __init__(self, nome_completo, celular, email, data_nascimento, descricao):
        self.descricao = descricao
        self.data_nascimento = data_nascimento
        self.email = email
        self.celular = celular
        self.nome_completo = nome_completo


def registro_bd():
    # Conexão com banco de dados
    import mysql.connector
    conexao = mysql.connector.connect(
        host='localhost',
        user='Maximiano',
        password='Pemax1992',
        database='bdcadastrofamilia',
    )

    cursor = conexao.cursor()

    # Comando para inserir e salvar dados inputados no banco de dados
    comando = f'INSERT INTO formulario-lead (nome_completo, celular, email, data_nascimento, descricao) VALUES '
    cursor.execute(comando)
    conexao.commit()


if __name__ == "__main__":
    lead1 = Lead('Pedro Maximiano', '19991002700', 'peeemax@hotmail.com', '13/09/1992', 'Saber mais sobre o serviços')
    print(lead1.nome_completo, lead1.celular, lead1.email, lead1.data_nascimento, lead1.descricao)



