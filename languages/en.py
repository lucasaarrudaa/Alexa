import json


class English:

    translations = {
        "Olá! Sou a Assistente Virtual. Posso te ajudar?": "Hello! I am the Virtual Assistant. How can I help you?",
        "Digite 'sim' para começar ou 'nao' para sair: ": "Type 'yes' to start or 'no' to exit: ",
        "Fale o seu comando: ": "Speak your command: ",
        "Até mais!": "Goodbye!",
        # Adicionar outras traduções aqui
    }

    @staticmethod
    def translate(text):
        # Função para translate um text para inglês
        # lógica de tradução para o inglês
        # Retorna o text traduzido para o inglês
        return English.translations.get(text, text)

    @staticmethod
    def translate_commands(arquivo_json):
        # Função para translate os commands de um arquivo JSON para inglês
        with open(arquivo_json, 'r') as arquivo:
            dados = json.load(arquivo)
            commands = dados.get('commands', [])
            for comando in commands:
                comando['comando'] = English.translate(comando['comando'])
                comando['resposta'] = English.translate(comando['resposta'])
        with open(arquivo_json, 'w') as arquivo:
            json.dump(dados, arquivo, indent=2)

    @staticmethod
    def translate_respostas(arquivo_py):
        # Função para translate as respostas de um arquivo Python para inglês
        with open(arquivo_py, 'r') as arquivo:
            linhas = arquivo.readlines()
        with open(arquivo_py, 'w') as arquivo:
            for linha in linhas:
                linha_traduzida = English.translate(linha)
                arquivo.write(linha_traduzida)
