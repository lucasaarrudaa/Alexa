import subprocess
import json
from src.interpreter import Interpreter
from languages.en import English
from languages.es import Spanish
from languages.pt import Portuguese
from vocabulary.translate_commands import TranslateCommands


class VirtualAssistant:

    def __init__(self, language):
        if language == 'en':
            self.language = 'en'
            self.translator = English()
            self.arquivo_json = r'vocabulary\commands_en.json'

        elif language == 'pt':
            self.language = 'pt'
            self.translator = Portuguese()
            TranslateCommands(
                r'vocabulary\commands_en.json').translate_command('en', 'pt')

            self.arquivo_json = r'vocabulary\commands_pt.json'

        elif language == 'es':
            self.language = 'es'
            self.translator = Spanish()
            TranslateCommands(
                r'vocabulary\commands_en.json').translate_command('en', 'es')
            self.arquivo_json = r'vocabulary\commands_es.json'

        else:
            raise ValueError("language not supported.")

        self.interpreter = Interpreter(self.arquivo_json)

    def start(self):
        print(self.translator("Hello! I'm the Virtual assistant. I can help you?"))
        while True:
            response = input(self.translator(
                "Type 'yes' to start or 'no' to quit:"))
            if response.lower() in ['sim', 'yes']:
                command = input(self.translator("Speak your command:"))
                response = self.interpreter.interpretar_command(command)
                print(self.translator(response))
                command_info = self.interpreter.get_command_info(command)
                if command_info and 'action' in command_info:
                    action = command_info['action']
                    subprocess.run(["python", action])
            else:
                print(self.translator("Até mais!"))
                break


# Ask the user to choose the language
while True:
    language = input("Choose language (en/pt/es): ")
    if language in ['en', 'pt']:
        break
    else:
        print("invalid language. Please choose 'en' for English, 'pt' para Português, 'es' para Español")

assistant = VirtualAssistant(language)
assistant.start()
