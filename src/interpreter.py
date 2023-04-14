import json


class Interpreter:

    def __init__(self, json_archive):
        self.commands = []
        with open(json_archive, 'r') as archive:
            data = json.load(archive)
            if 'commands' in data:
                self.commands = data['commands']

    def interpret_command(self, command):
        response = "Sorry, I didn't understand the command."
        for cmd in self.commands:
            if cmd['command'] == command:
                response = cmd['response']
                break
        return response

    def get_command_info(self, command):
        for cmd in self.commands:
            if cmd['command'] == command:
                return cmd
        return None
