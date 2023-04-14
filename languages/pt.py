import json


class Portuguese:

    translations = {
        "Hello! I am the Virtual Assistant. How can I help you?": "Olá! Sou a Assistente Virtual. Posso te ajudar?",
        "Type 'yes' to start or 'no' to exit: ": "Digite 'sim' para começar ou 'nao' para sair: ",
        "Speak your command: ": "Fale um comando: ",
        "Goodbye!":  "Até mais!"
        # Add other translations here
    }

    @staticmethod
    def translate(text):

        return Portuguese.translations.get(text, text)

    @staticmethod
    def translate_commands(archive_json):
        # Function to translate the commands of a JSON file into Portuguese
        with open(archive_json, 'r') as archive:
            data = json.load(archive)
            commands = data.get('commands', [])
            for command in commands:
                command['command'] = Portuguese.translate(command['command'])
                command['response'] = Portuguese.translate(command['response'])
        with open(archive_json, 'w') as archive:
            json.dump(data, archive, indent=2)

    @staticmethod
    def translate_responses(archive_py):
        # Function to translate responses from a Python archive into Portuguese
        with open(archive_py, 'r') as archive:
            lines = archive.readlines()
        with open(archive_py, 'w') as archive:
            for line in lines:
                line_translated = Portuguese.translate(line)
                archive.write(line_translated)
