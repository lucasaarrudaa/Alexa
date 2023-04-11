import json
class Interpretacao:
    """
    Classe responsável pela interpretação de comandos a partir de um arquivo JSON.
    """    
    def __init__(self, arquivo_json):
        """
        Construtor da classe Interpretacao.

        Parâmetros:
            - arquivo_json (str): Caminho do arquivo JSON contendo os comandos.

        """
        self.comandos = []
        with open(arquivo_json, 'r') as arquivo:
            dados = json.load(arquivo)
            if 'comandos' in dados:
                self.comandos = dados['comandos']

    def interpretar_comando(self, comando):
        """
        Interpreta um comando a partir do arquivo JSON carregado.

        Parâmetros:
            - comando (str): Comando a ser interpretado.

        Retorna:
            - resposta (str): Resposta correspondente ao comando, ou uma mensagem de erro caso o comando não seja encontrado.

        """        
        resposta = "Desculpe, não entendi o comando."
        for cmd in self.comandos:
            if cmd['comando'] == comando:
                resposta = cmd['resposta']
                break
        return resposta

    def get_comando_info(self, comando):
        """
        Obtém informações detalhadas de um comando a partir do arquivo JSON carregado.

        Parâmetros:
            - comando (str): Comando para o qual se deseja obter informações.

        Retorna:
            - cmd_info (dict): Dicionário contendo as informações do comando, ou None caso o comando não seja encontrado.

        """        
        for cmd in self.comandos:
            if cmd['comando'] == comando:
                return cmd
        return None
