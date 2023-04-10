import json

class Interpretacao:
    def __init__(self, arquivo_json):
        self.comandos = []
        with open(arquivo_json, 'r') as arquivo:
            dados = json.load(arquivo)
            if 'comandos' in dados:
                self.comandos = dados['comandos']

    def interpretar_comando(self, comando):
        resposta = "Desculpe, não entendi o comando."
        for cmd in self.comandos:
            if cmd['comando'] == comando:
                resposta = cmd['resposta']
                break
        return resposta

    def get_comando_info(self, comando):
        for cmd in self.comandos:
            if cmd['comando'] == comando:
                return cmd
        return None
