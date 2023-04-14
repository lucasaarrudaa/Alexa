## Alexa
The Alexa project is a Python voice assistant that allows users to interact with the system using voice commands.

- It consists of the following files and directories:
  - ```main.py```: The main file of the project, which contains the main logic of the voice assistant.
  - utils/: A directory that contains utilities and helper functions for the project.
    - ```conn_db.py```: A file that contains functions related to connecting to a database (if applicable).
    - ```limpeza.py```: A file that contains functions for cleaning and processing user input data.
    - ```check_rooms.py```: A file containing functions to check the status of a room (if applicable).
  - src/:
    - ```interpreter.py```: A file that contains functions to interpret the user's voice commands.
  - languages/: A directory containing files related to internationalization and localization of the project.
    - ```en.py```: A file that contains classes and functions related to the English language.
    - ```pt.py```: A file that contains classes and functions related to the Portuguese language.
    - ```es.py```: A file that contains classes and functions related to the Spanish language.
  - vocabulary/: A directory containing files related to the project's vocabulary and keywords.
    - ```commmands_en.json```: A JSON file that contains the English voice commands for the project.
    - ```commands_en.json```: A JSON file that contains the Portuguese voice commands for the project.
    - ```commands_es.json```: A JSON file that contains the Spanish voice commands for the project.
    - ```translate_commands.py```: A file that contains functions for translating voice commands between languages.
