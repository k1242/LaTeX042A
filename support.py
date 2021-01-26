import sublime
import sublime_plugin
import os

package_name = "LaTeX042A"
settings_file = "LaTeX042A.sublime-settings"


def generate_snippets():
    print("-snippets generating started")

    snippets_list_path = "{}/{}/settings/snippets_list.txt".format(
        sublime.packages_path(), package_name)
    user_snippets_list_path = "{}/User/{}".format(
        sublime.packages_path(), package_name)
    snippets_path = "{}/{}/sources/snippets/".format(
        sublime.packages_path(), package_name)

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
    lines = []

    # check settings file
    settings = sublime.load_settings(settings_file)
    if settings.get("use_packet_snippets"):
        with open(snippets_list_path, "r") as f:
            lines += f.readlines()

    if settings.get("use_user_snippets"):
        with open(user_snippets_list_path + "/snippets.txt", "r") as f:
            lines += f.readlines()

    # parse into the triggers
    for i in range(len(lines)):

        # declare triggers
        line = lines[i]
        if line[:7] == "trigger":
            trigger = line[line.find(":") + 1:-1]
            trigger = trigger.replace(" ", "")
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

    print("-snippets generating finished")


def generate_keymaps():
    print("-keymaps generating started")
    prefix = "{}/{}/".format(
        sublime.packages_path(), package_name)
    user_file = "{}/User/{}/keymaps.json".format(
        sublime.packages_path(), package_name)

    files = [f for f in os.listdir(prefix + "sources/keymaps")]
    lines = []

    settings = sublime.load_settings(settings_file)
    # packet files
    if settings.get("use_packet_keymaps"):
        for file in files:
            with open(prefix + "sources/keymaps/" + file, "r") as f:
                lines += f.readlines()
                lines += ["\n\n\n"]

    # user keymaps file
    if settings.get("use_user_keymaps"):
        lines += ["\n\n\n\t// ---- user keymaps ----\n"]
        with open(user_file, "r") as f:
            lines += f.readlines()
            lines += ["\n\n\n"]

    output = ""

    # writing to system file
    with open(prefix + "support/Default.sublime-keymap", "w") as f:
        output += "[\n"
        for line in lines:
            output += "\t" + line
        output += "\n]"
        f.write(output)
    print("-keymaps generating finished")


def xyz_settings_edit():
    file = "{}/User/LaTeXYZ.sublime-settings".format(
        sublime.packages_path(), package_name)
    required_setting = '"use_latex_quotes": false'

    def find_last_match(s, p):
        i = 0
        flag = True
        while s.find(p) > 0:
            i = s.find(p) + i
            s = s[i + 1:]
            flag = False
        if flag: i = -1
        return i

    if not os.path.exists(file):
        open(file, "w").close()

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
            f.write("{\n\t" + required_setting + "\n}")
        print("042A: xyz settings were created and edited")
    else:
        tmp_text = ""
        k = find_last_match(full_text, ",")

        print(full_text[k + 1:])
        if len(full_text[k + 1:].replace("}", "").replace("\t", "").replace("\n", "").replace(" ", "")) > 2:
            add_comma_flag = True
        else:
            add_comma_flag = False

        for (j, line) in enumerate(lines):
            tmp_text += line
            if len(tmp_text) > i:
                break

            with open(file, "w") as f:
                for line in lines[:j + 1]:
                    f.write(line)
                if add_comma_flag:
                    f.write(",")
                f.write("\n\t" + required_setting + "\n}")
        print("042A: xyz settings were edited")


# open folder
class Openfolder(sublime_plugin.TextCommand):
    def run(self, edit, folder_name):
        keymaps_folder_path = "{}/{}/{}".format(
            sublime.packages_path(), package_name, folder_name)
        os.startfile(keymaps_folder_path)



# update keymaps and snippets list
class Globalupdate(sublime_plugin.WindowCommand):
    def run(self):

        generate_snippets()
        generate_keymaps()
        xyz_settings_edit()

        self.window.status_message("042A: recources updated")
