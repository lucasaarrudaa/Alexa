import subprocess
import json
from src.interpretacao import Interpretacao
from idiomas.en import Ingles 

class AssistenteVirtual:
    
    def __init__(self, idioma):
        if idioma == 'en':
            self.idioma = 'en'
            self.tradutor = Ingles()
            self.arquivo_json = r'vocabulario\commands_en.json'
            
        elif idioma == 'pt':
            self.idioma = 'pt'
            # self.tradutor = Portugues()
            self.arquivo_json = r'vocabulario\commands_pt.json'
        else:
            raise ValueError("Idioma não suportado.")
            
        self.interpretacao = Interpretacao(self.arquivo_json)

    def iniciar(self):
        print(self.tradutor.traduzir("Olá! Sou a Assistente Virtual. Posso te ajudar?"))
        while True:
            resposta = input(self.tradutor.traduzir("Digite 'sim' para começar ou 'nao' para sair: "))
            if resposta.lower() in ['sim', 'yes']:  
                comando = input(self.tradutor.traduzir("Fale o seu comando: "))
                resposta = self.interpretacao.interpretar_comando(comando)
                print(self.tradutor.traduzir(resposta))
                comando_info = self.interpretacao.get_comando_info(comando)
                if comando_info and 'acao' in comando_info:
                    acao = comando_info['acao']
                    subprocess.run(["python", acao]) 
            else:
                print(self.tradutor.traduzir("Até mais!"))
                break

# Solicitar ao usuário que escolha o idioma
while True:
    idioma = input("Escolha o idioma (en/pt): ")
    if idioma in ['en', 'pt']:
        break
    else:
        print("Idioma inválido. Por favor, escolha 'en' para inglês ou 'pt' para português.")

# Instanciar a Assistente Virtual com o idioma escolhido e iniciar a interação
assistente = AssistenteVirtual(idioma)
assistente.iniciar()
