from conexao_db import Conexao
import datetime
import threading

class Limpeza(Conexao):
    def __init__(self):
        super().__init__()  # Chama o construtor da classe Conexao
        self.connection = self.conn  # Atribui a conexão à variável connection
        self.lock = threading.Lock()  # Lock para garantir a sincronização de acesso ao banco de dados

    def iniciar_limpeza(self, id_quarto):
        query = f"SELECT limpeza, data_entrada FROM quartos WHERE id_quartos = {id_quarto}"
        self.cursor.execute(query)
        quarto = self.cursor.fetchone()

        if not quarto:
            return "Quarto não encontrado."

        limpeza = quarto[0]
        data_entrada = quarto[1]

        if limpeza == 'S':
            return "Quarto já está limpo."

        # Obter o momento de início da limpeza
        limpeza_inicio = datetime.datetime.now()

        # Iniciar a limpeza em uma thread separada
        t = threading.Thread(target=self.realizar_limpeza, args=(id_quarto, data_entrada, limpeza_inicio))
        t.start()

        return "Limpeza iniciada em uma thread separada."

    def realizar_limpeza(self, id_quarto, data_entrada, limpeza_inicio):
        with self.lock:
            # Iniciar a limpeza
            print("Iniciando a Limpeza")
            query = f"UPDATE quartos SET limpeza = 'S', limpeza_inicio = '{limpeza_inicio}' WHERE id_quartos = {id_quarto}"
            self.cursor.execute(query)
            self.conn.commit()

        # Calcular data de limpeza final (30 minutos após a data de entrada)
        data_limpeza_final = data_entrada + datetime.timedelta(minutes=30)

        # Cronometrar 30 minutos de limpeza
        while datetime.datetime.now() < data_limpeza_final:
            pass

        with self.lock:
            # Obter o momento de término da limpeza
            limpeza_fim = datetime.datetime.now()

            # Finalizar a limpeza
            query = f"UPDATE quartos SET limpeza = 'S', data_saida = '{data_limpeza_final}', limpeza_fim = '{limpeza_fim}' WHERE id_quartos = {id_quarto}"
            self.cursor.execute(query)
            self.conn.commit()

            print(f"Limpeza concluída para o quarto {id_quarto}.")

limpeza = Limpeza()
id_quarto = int(input("Digite o ID do quarto a ser limpo: "))  # ID do quarto a ser limpo, informado pelo usuário
resultado = limpeza.iniciar_limpeza(id_quarto)
print(resultado)
