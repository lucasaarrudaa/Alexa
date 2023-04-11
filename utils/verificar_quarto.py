from conexao_db import Conexao

class VerificarDisponibilidadeQuarto(Conexao):
    
    def verificar_disponibilidade(self):
        print('verificar_disponibilidade')
        query = "SELECT * FROM quartos WHERE disponivel = 'S'"
        self.cursor.execute(query)
        quartos_disponiveis = self.cursor.fetchall()

        if quartos_disponiveis:
            # Se houver quartos disponíveis
            output = ""
            for quarto in quartos_disponiveis:
                output += f"Quarto {quarto[0]}: Disponível (não reservado).\n"
            return output
        else:
            query = "SELECT * FROM quartos ORDER BY data_saida ASC LIMIT 1"
            self.cursor.execute(query)
            primeiro_quarto_desocupado = self.cursor.fetchone()
            if primeiro_quarto_desocupado:
                return f"Nenhum quarto disponível. O quarto {primeiro_quarto_desocupado[0]} será desocupado primeiro em {primeiro_quarto_desocupado[2]}"
            else:
                return "Nenhum quarto disponível e não há previsão de desocupação."

verifica = VerificarDisponibilidadeQuarto()
resultado = verifica.verificar_disponibilidade()
print(resultado)
