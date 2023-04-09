import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import SnowballStemmer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import SVC
from sklearn.pipeline import Pipeline

class AssistenteVirtual:
    '''
    Dados para treinar a assistente virtual. Neste caso, usei uma lista de frases como dados de treinamento.
    '''
    def __init__(self):
        nltk.download('punkt')
        # Baixar os dados de stopwords do NLTK
        nltk.download('stopwords')
        # Instanciar o stemmer
        self.stemmer = SnowballStemmer('portuguese')
        # Definir as regras de resposta
        self.regras_respostas = {
            'cumprimento': 'Olá! Como posso ajudar?',
            'nome': 'Meu nome é Alexia.',
            'piada': 'Por que o peixe não gosta de computador? Porque ele tem medo do mouse!',
            'noticias': 'Desculpe, não tenho acesso às notícias no momento.',
            'lembrete': 'Lembrete adicionado: Comprar leite.',
            'clima': 'Desculpe, não posso verificar o clima no momento.',
            'funcoes': 'Eu sou um assistente virtual que pode responder a perguntas simples e realizar tarefas básicas.',
            'desligar_luzes': 'Desculpe, não tenho a capacidade de controlar dispositivos físicos.'
            }

        # Treinar o modelo de detecção de intenções
        self.modelo_intencoes = self.treinar_modelo_intencoes()

    def preprocessamento(self, texto):
        '''
        Pré-processamento de texto
        Torná-lo adequado para o processamento de linguagem natural. Vamos realizar as seguintes etapas:
        Tokenização: Dividir o texto em palavras individuais.
        Remoção de stopwords: Remover palavras comuns que não contêm muita informação, como "é", "de", "em", etc.
        Stemming: Reduzir as palavras às suas raízes, para agrupar palavras similares juntas.
        '''
        # Tokenização
        palavras = word_tokenize(texto.lower())
        # Remoção de stopwords
        palavras = [palavra for palavra in palavras if palavra not in stopwords.words('portuguese')]
        # Stemming
        palavras = [self.stemmer.stem(palavra) for palavra in palavras]
        return palavras

    def treinar_modelo_intencoes(self):
        # Dados de treinamento para o modelo de detecção de intenções
        perguntas_treinamento = ['Qual é o seu nome?', 'Me conte uma piada', 'O que você pode fazer?']
        intencoes_treinamento = ['nome', 'piada', 'funcoes']

        # Criar pipeline para vetorização de texto e classificação usando SVM
        pipeline = Pipeline([
            ('vetorizacao', TfidfVectorizer(tokenizer=self.preprocessamento)),
            ('classificacao', SVC(kernel='linear', C=1, probability=True))
        ])

        # Treinar o modelo
        pipeline.fit(perguntas_treinamento, intencoes_treinamento)

        return pipeline

    def detectar_intencao(self, pergunta):
        # Predizer a intenção da pergunta usando o modelo treinado
        intencao_predita = self.modelo_intencoes.predict([pergunta])[0]
        return intencao_predita

    def responder_pergunta(self, pergunta):
        '''
        recebe uma pergunta como entrada e utiliza o modelo de detecção de intenções treinado para identificar a intenção da pergunta. 
        Em seguida, a resposta correspondente é buscada na lista de regras de resposta com base na intenção detectada. 
        Se a intenção não for reconhecida, uma mensagem padrão de "Desculpe, não entendi a pergunta" é retornada.
        '''
        # Detectar a intenção da pergunta
        intencao = self.detectar_intencao(pergunta)

        # Procurar pela intenção na lista de regras de resposta e retornar a resposta correspondente
        if intencao in self.regras_respostas:
            return self.regras_respostas[intencao]
        else:
            return 'Desculpe, não entendi a pergunta.'

    def iniciar_conversa(self):
        '''
        É responsável por iniciar a interação com o assistente virtual. 
        Ele exibe uma mensagem de boas-vindas e entra em um loop que permite ao usuário fazer perguntas e receber respostas do assistente virtual. 
        O loop é interrompido quando o usuário digita "sair".
        '''
        print("Olá! Eu sou a Alexia, seu assistente virtual. Como posso ajudar você hoje?")
        while True:
            pergunta = input("Você: ")
            resposta = self.responder_pergunta(pergunta)
            print("Alexia: " + resposta)

            # Condição de saída do loop
            if pergunta.lower() == 'sair':
                print("Alexia: Até mais!")
                break

# Instanciar o assistente virtual e iniciar a conversa
assistente = AssistenteVirtual()
assistente.iniciar_conversa()
