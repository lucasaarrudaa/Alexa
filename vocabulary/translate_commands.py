from googletrans import Translator
import json


class TranslateCommands:

    def __init__(self, json_file):
        self.json_file = json_file

    def translate_command(self, by, to):
        # Carrega o arquivo JSON
        with open(self.json_file, 'r', encoding='utf-8') as f:
            data = json.load(f)

        # Translate commands and responses to English
        translator = Translator()
        for command in data["commands"]:
            command["command"] = translator.translate(
                command["command"], src=f'{by}', dest=f'{to}').text
            command["response"] = translator.translate(
                command["response"], src=f'{by}', dest=f'{to}').text

        # Save the result in a new JSON file
        with open(rf'vocabulary\commands_{to}.json', 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)


json_file = r'vocabulary\commands_en.json'
