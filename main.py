import subprocess
import json
from src.interpretacao import Interpretacao

class AssistenteVirtual:
    def __init__(self, arquivo_json):
        self.interpretacao = Interpretacao(arquivo_json)

    def iniciar(self):
        print("Olá! Sou a Assistente Virtual. Posso te ajudar?")
        while True:
            resposta = input("Digite 'sim' para começar ou 'nao' para sair: ")
            if resposta.lower() == 'sim':
                comando = input("Fale o seu comando: ")
                resposta = self.interpretacao.interpretar_comando(comando)
                print(resposta)
                comando_info = self.interpretacao.get_comando_info(comando)
                if comando_info and 'acao' in comando_info:
                    acao = comando_info['acao']
                    subprocess.run(["python", acao]) # Executa o arquivo especificado na chave 'acao' do JSON
            else:
                print("Até mais!")
                break

# Arquivo JSON com os comandos
arquivo_json = 'comandos.json'

# Instanciando a Assistente Virtual e iniciando a interação
assistente = AssistenteVirtual(arquivo_json)
assistente.iniciar()
