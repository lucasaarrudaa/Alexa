import mysql.connector

class Conexao:
    
    def __init__(self):
        print("conectando ao banco")
        self.conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password='168843',
            database='alexa'
        )
        self.cursor = self.conn.cursor()

    def fechar_conexao(self):
        self.cursor.close()
        self.conn.close()
