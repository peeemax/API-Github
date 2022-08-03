

class Lead:

    def __init__(self, nome_completo, celular, email, data_nascimento, descricao):
        self.data_nascimento = data_nascimento
        self.email = email
        self.celular = celular
        self.nome_completo = nome_completo
        self.descricao = descricao


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
    comando = f'INSERT INTO form_lead (nome_completo, celular, email, data_nascimento, descricao) VALUES ' \
              f'("{lead.nome_completo}", "{lead.celular}", "{lead.email}", "{lead.data_nascimento}", "{lead.descricao}")'
    cursor.execute(comando)
    conexao.commit()


if __name__ == "__main__":
    lead = Lead('Vitor', '192391293129', 'asdasd@dfgkasdo','2190931290', 'Saber')
    lead1 = Lead('Pedro Maximiano', '19991002700', 'peeemax@hotmail.com', '13/09/1992', 'Saber de mais')

    registro_bd()

    print(lead1.nome_completo, lead1.celular, lead1.email, lead1.data_nascimento, lead1.descricao)



