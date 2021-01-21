import re
import ctypes
from pathlib import Path

snip_start = "..[["
snip_end = "]].."

prefix = str(Path(__file__).parents[1]) + "\\"
snippets_list_path = prefix+"settings\\snippets_list.txt"
snippets_path = prefix + "sources\\snippets\\"

preambule_1 = "<snippet><content><![CDATA[\n{}\n]]></content>\n"
preambule_2 = "\t<tabTrigger>{}</tabTrigger>\n"
preambule_3 = "\t<scope>text.tex.latex </scope>\n</snippet>"
preambule = preambule_1 + preambule_2 + preambule_3

triggers = []
snippets = []

with open(snippets_list_path) as f:
    lines = f.readlines()

for i in range(len(lines)):

    # declare triggers
    line = lines[i]
    if line[:7] == "trigger":
        trigger = line[line.find(":")+1:-1]
        trigger = re.sub(" +", "", trigger)
        triggers.append(trigger)

    # declare snippets
    if line.find(snip_start) >= 0:
        snippet = ""
        i += 1; line = lines[i]
        while line.find(snip_end) < 0:
            snippet += line
            i += 1; line = lines[i]
        snippets.append(snippet[:-1])

if len(triggers) != len(snippets):
    ctypes.windll.user32.MessageBoxW(None, u"Error", u"Error", 0)

triggers_ = []
snippets_ = []

for (i, (trigger, snippet)) in enumerate(zip(triggers, snippets)):
    if trigger and snippet:
        with open(
            snippets_path + str(i)+".sublime-snippet", 
            "w") as f:
            triggers_.append(trigger)
            snippets_.append(snippet)
            f.write(preambule.format(snippet, trigger))