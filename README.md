## Alexa
O projeto Alexa é um assistente de voz em Python que permite aos usuários interagirem com o sistema usando comandos de voz. 

Ele é composto pelos seguintes arquivos e diretórios:

main.py: O arquivo principal do projeto, que contém a lógica principal do assistente de voz.
utils/: Um diretório que contém utilitários e funções auxiliares para o projeto.
- conexao_db.py: Um arquivo que contém funções relacionadas à conexão com um banco de dados (caso aplicável).
- limpeza.py: Um arquivo que contém funções para limpeza e processamento de dados de entrada do usuário.
- verificar_quarto.py: Um arquivo que contém funções para verificar o estado de um quarto (caso aplicável).
src/: Um diretório que contém o código-fonte do projeto.
- interpretacao.py: Um arquivo que contém funções para interpretar os comandos de voz do usuário.
idiomas/: Um diretório que contém arquivos relacionados à internacionalização e localização do projeto.
- en.py: Um arquivo que contém classes e funções relacionadas ao idioma inglês.
vocabulario/: Um diretório que contém arquivos relacionados ao vocabulário e às palavras-chave do projeto.
- commandos_en.json: Um arquivo JSON que contém os comandos de voz em inglês para o projeto.
- commands_pt.json: Um arquivo JSON que contém os comandos de voz em português para o projeto.
- commands_es.json: Um arquivo JSON que contém os comandos de voz em espanhol para o projeto.
tradutor.py: Um arquivo que contém funções para tradução de comandos de voz entre idiomas.
