from pathlib import Path
import os

package_name = "LaTeX042A"


prefix = str(Path(__file__).parents[1]) + "\\"
snippets_list_path = prefix + "settings\\snippets_list.txt"
snippets_path = prefix + "sources\\snippets\\"

user_snippets_list_path = "{}/User/{}".format(
    str(Path(__file__).parents[2]), package_name)

if not os.path.exists(user_snippets_list_path):
    os.mkdir(user_snippets_list_path)
if not os.path.exists(user_snippets_list_path + "/snippets.txt"):
    open(user_snippets_list_path + "/snippets.txt", "a").close()

preambule_1 = "<snippet><content><![CDATA[\n{}\n]]></content>\n"
preambule_2 = "\t<tabTrigger>{}</tabTrigger>\n"
preambule_3 = "\t<scope>text.tex.latex </scope>\n</snippet>"
preambule = preambule_1 + preambule_2 + preambule_3

snip_start = "..[["
snip_end = "]].."

triggers = []
snippets = []

with open(snippets_list_path, "r") as f:
    lines = f.readlines()

with open(user_snippets_list_path + "/snippets.txt", "r") as f:
    user_lines = f.readlines()

lines += user_lines

for i in range(len(lines)):

    # declare triggers
    line = lines[i]
    if line[:7] == "trigger":
        trigger = line[line.find(":") + 1:-1]
        trigger = trigger.replace(" ", "")  # зачем здесь эта строка?
        triggers.append(trigger)

    # declare snippets
    if line.find(snip_start) >= 0:
        snippet = ""
        i += 1
        line = lines[i]
        while line.find(snip_end) < 0:
            snippet += line
            i += 1
            line = lines[i]
        snippets.append(snippet[:-1])


filelist = [f for f in os.listdir(
    snippets_path) if f.endswith(".sublime-snippet")]
for f in filelist:
    os.remove(snippets_path + f)

triggers_ = []
snippets_ = []

for (i, (trigger, snippet)) in enumerate(zip(triggers, snippets)):
    if trigger and snippet:
        with open(
                snippets_path + str(i) + ".sublime-snippet",
                "w") as f:
            triggers_.append(trigger)
            snippets_.append(snippet)
            f.write(preambule.format(snippet, trigger))
