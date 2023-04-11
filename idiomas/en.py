import json

class Ingles:
    
    traducoes = {
        "Olá! Sou a Assistente Virtual. Posso te ajudar?": "Hello! I am the Virtual Assistant. How can I help you?",
        "Digite 'sim' para começar ou 'nao' para sair: ": "Type 'yes' to start or 'no' to exit: ",
        "Fale o seu comando: ": "Speak your command: ",
        "Até mais!": "Goodbye!",
        # Adicionar outras traduções aqui
    }

    @staticmethod
    def traduzir(texto):
        # Função para traduzir um texto para inglês
        # lógica de tradução para o inglês
        # Retorna o texto traduzido para o inglês
        return Ingles.traducoes.get(texto, texto)

    @staticmethod
    def traduzir_comandos(arquivo_json):
        # Função para traduzir os comandos de um arquivo JSON para inglês
        with open(arquivo_json, 'r') as arquivo:
            dados = json.load(arquivo)
            comandos = dados.get('comandos', [])
            for comando in comandos:
                comando['comando'] = Ingles.traduzir(comando['comando'])
                comando['resposta'] = Ingles.traduzir(comando['resposta'])
        with open(arquivo_json, 'w') as arquivo:
            json.dump(dados, arquivo, indent=2)
            
    @staticmethod
    def traduzir_respostas(arquivo_py):
        # Função para traduzir as respostas de um arquivo Python para inglês
        with open(arquivo_py, 'r') as arquivo:
            linhas = arquivo.readlines()
        with open(arquivo_py, 'w') as arquivo:
            for linha in linhas:
                linha_traduzida = Ingles.traduzir(linha)
                arquivo.write(linha_traduzida)
