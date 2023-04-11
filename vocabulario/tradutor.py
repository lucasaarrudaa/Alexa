from googletrans import Translator
import json

class TradutorComandos:
    
    def __init__(self, json_file):
        self.json_file = json_file

    def traduzir(self):
        # Carrega o arquivo JSON
        with open(self.json_file, 'r', encoding='utf-8') as f:
            dados = json.load(f)

        # Traduz os comandos e respostas para inglês
        tradutor = Translator()
        for comando in dados["comandos"]:
            comando["comando"] = tradutor.translate(comando["comando"], src='pt', dest='es').text
            comando["resposta"] = tradutor.translate(comando["resposta"], src='pt', dest='en').text

        # Salva o resultado em um novo arquivo JSON
        with open(r'vocabulario\commands_en.json', 'w', encoding='utf-8') as f:
            json.dump(dados, f, ensure_ascii=False, indent=4)
            
json_file = r'vocabulario\commands_pt.json' 
tradutor = TradutorComandos(json_file)
tradutor.traduzir()
