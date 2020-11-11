# Запустите этот .py файл. 
# Так исполняемый плагин станет на место и всё заработает.

from pathlib import Path


plugin_name = "L042ATeX.py"
user_path = str(Path(__file__).parents[2])
fin_path = user_path + "\\" + plugin_name


with open(plugin_name, "r") as f:
    lines = f.readlines()


with open(fin_path, "w") as f:
    output = ""
    for line in lines:
        output += line
    f.write(output)