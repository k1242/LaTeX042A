import re
from os import listdir
from pathlib import Path


prefix = str(Path(__file__).parents[0]) + "\\"
prefix_2 = str(Path(__file__).parents[1]) + "\\"


files = [f for f in listdir(prefix+"keymaps")]
lines = []

for file in files:
    with open(prefix+"keymaps\\"+file, "r") as f:
        lines += f.readlines()
        lines += ["\n\n\n"]



print(len(lines))

for file in files:
    print(file.split(".")[0])


output = ""
with open(prefix_2+"Default.sublime-keymap", "w") as f:
    output += "[\n"
    for line in lines:
        output += "\t"+line
    output += "\n]"
    f.write(output)




