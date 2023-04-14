import json


class Spanish:

    translations = {
        "Hello! I am the Virtual Assistant. How can I help you?": "¡Hola! Soy el Asistente Virtual. ¿Puedo ayudarte?",
        "Type 'yes' to start or 'no' to exit: ": "Escriba 'sí' para comenzar o 'no' para salir: ",
        "Speak your command: ": "Di tu comando: ",
        "Goodbye!":  "Hasta Luego!"
        # Add other translations here
    }

    @staticmethod
    def translate(text):

        return Spanish.translations.get(text, text)

    @staticmethod
    def translate_commands(archive_json):
        # Function to translate the commands of a JSON file into Spanish
        with open(archive_json, 'r') as archive:
            data = json.load(archive)
            commands = data.get('commands', [])
            for command in commands:
                command['command'] = Spanish.translate(command['command'])
                command['response'] = Spanish.translate(command['response'])
        with open(archive_json, 'w') as archive:
            json.dump(data, archive, indent=2)

    @staticmethod
    def translate_responses(archive_py):
        # Function to translate responses from a Python archive into Spanish
        with open(archive_py, 'r') as archive:
            lines = archive.readlines()
        with open(archive_py, 'w') as archive:
            for line in lines:
                line_translated = Spanish.translate(line)
                archive.write(line_translated)
