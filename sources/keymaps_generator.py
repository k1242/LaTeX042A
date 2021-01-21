from os import listdir
from pathlib import Path


prefix = str(Path(__file__).parents[1]) + "\\"
files = [f for f in listdir(prefix+"sources\\keymaps")]
lines = []

for file in files:
    with open(prefix+"sources\\keymaps\\"+file, "r") as f:
        lines += f.readlines()
        lines += ["\n\n\n"]

# for file in files:
#     print(file.split(".")[0])

output = ""
with open(prefix+"Default.sublime-keymap", "w") as f:
    output += "[\n"
    for line in lines:
        output += "\t"+line
    output += "\n]"
    f.write(output)



