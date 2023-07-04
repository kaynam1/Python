import mysql.connector


def check_db_connection():
    try:
        # Estabelecer a conexão com o banco de dados
        conn = mysql.connector.connect(
            host='127.0.0.1',
            port=3306,
            user="root",
            password="87015119k",
            database="db_testemysql"
        )

        # Verificar se a conexão foi estabelecida com sucesso
        if conn.is_connected():
            print('Conexão com o banco de dados estabelecida com sucesso.')

            # Realizar alguma operação no banco de dados, se necessário
            # Exemplo: executar uma consulta
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM sua_tabela')
            rows = cursor.fetchall()

            # Exibir os resultados da consulta
            for row in rows:
                print(row)

            # Fechar a conexão
            cursor.close()
            conn.close()
        else:
            print('Falha ao conectar ao banco de dados.')

    except mysql.connector.Error as error:
        print('Erro ao conectar ao banco de dados:', error)


# Chamar a função para verificar a conexão com o banco de dados
check_db_connection()
