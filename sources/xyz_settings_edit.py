from pathlib import Path

package_name = "LaTeX042A"
required_setting = '"use_latex_quotes": false'
file = str(Path(__file__).parents[2]) + "\\User\\LaTeXYZ.sublime-settings"

def find_last_match(s, p):
    i = 0; flag = True

    while s.find(p) > 0:
        i = s.find(p) + i
        s = s[i+1:]
        flag = False

    if flag: i = -1

    return i

with open(file, "r") as f:
    lines = f.readlines()

full_text = ""
for line in lines:
    full_text += line

i = find_last_match(full_text, "}")

if full_text.find(required_setting) >= 0:
    pass
    print("042A: xyz settings acceptable")
elif i < 0:
    with open(file, "w") as f:
        f.write("{\n\t"+required_setting+"\n}")
    print("042A: xyz settings were created and edited")
else:
    tmp_text = ""
    k = find_last_match(full_text, ",")

    print(full_text[k+1:])
    if len(full_text[k+1:].replace("}", "").replace("\t", "").replace("\n", "").replace(" ", "")) > 2:
        add_comma_flag = True
    else:
        add_comma_flag = False


    for (j, line) in enumerate(lines):
        tmp_text += line
        if len(tmp_text) > i: break

        with open(file, "w") as f:
            for line in lines[:j+1]:
                f.write(line)
            if add_comma_flag: f.write(",")
            f.write("\n\t"+required_setting+"\n}")
    print("042A: xyz settings were edited")

