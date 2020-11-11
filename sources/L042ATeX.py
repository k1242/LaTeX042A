import sublime
import sublime_plugin
import os
from distutils.dir_util import copy_tree


user_path = "User\\"
# user_path = ""
package_name = "L042ATeX"

path_change_layout = "\\sources\\vbs\\change_layout.vbs"
path_close_recent_file = "\\sources\\vbs\\close_recent_file.vbs"


env_names_list = ["align", "align*", "equation"]

endings_list = [
    " ", "\n", "\t", "|",
    "[", "(", "{",
    "`", "$", "^", "~",
     "-", "+" # но это сильно не точно.
]
# exceptions = ["_", "-", "+", "=", "*", "/"]
# 

nums_list = list("0123456789")

# def open_file(window, filename):
#     window.open_file(filename, sublime.ENCODED_POSITION)

# class OpenFileByNameCommand(sublime_plugin.WindowCommand):
#     def run(self):
#         fname = self.window.active_view().file_name()
#         if fname == None:
#             fname = ""

#         def done(filename):
#             open_file(self.window, filename)

#         self.window.show_input_panel(
#             "file to open: ", fname, done, None, None)


class AddvectorCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        sel = [(s.begin(), s.end()) for s in self.view.sel()]
        num = sel[0][0]
        self.view.insert(edit, num, "}")
        num -= 2
        self.view.insert(edit, num + 1, "\\vc{")


class AddenvCommand(sublime_plugin.TextCommand):
    def run(self, edit, env_name):
        sel = [(s.begin(), s.end()) for s in self.view.sel()]
        num = sel[0][0]
        self.view.insert(edit, num, "}")
        while (self.view.substr(num) not in (endings_list + nums_list) and num >= 0):
            if (self.view.substr(num) == "_"):
                # print(self.view.word(num))
                # print(type(self.view.word(num)))
                self.view.replace(edit, sublime.Region(num, num + 1), " ")
            num -= 1
        self.view.insert(edit, num + 1, "\\" + env_name + "{")


class TestsettingsCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        sel = [(s.begin(), s.end()) for s in self.view.sel()]
        num = sel[0][0]
        if self.view.settings().get('test_var_false'):
            self.view.insert(edit, num, "OK")
        else:
            self.view.insert(edit, num, "not OK")


class GooutCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        path = sublime.packages_path() + "\\" + user_path + \
            package_name + path_change_layout
        os.startfile(path)
        sel = [(s.begin(), s.end()) for s in self.view.sel()]
        num = sel[0][0]
        flag = 0
        skip = self.view.substr(num - 1)

        env_end_flag = False
        while (flag < 400 and self.view.substr(num) != "$"):
            skip += self.view.substr(num)
            flag += 1
            num += 1

            env_end_flag = False
            for env_names in env_names_list:
                if (skip.find("\\end{" + env_names + "}") != -1):
                    env_end_flag = True
                    break
            if env_end_flag:
                break

        if (env_end_flag):
            self.view.replace(edit, sublime.Region(sel[0][0], num), "")
            self.view.replace(edit,
                              sublime.Region(sel[0][0] - 1, sel[0][0]),
                              skip + "\n")
        elif (self.view.substr(num + 1) != "$"):
            self.view.replace(edit, sublime.Region(sel[0][0], num + 1), "")
            self.view.replace(edit,
                              sublime.Region(sel[0][0] - 1, sel[0][0]),
                              skip + "$")
        else:
            self.view.replace(edit, sublime.Region(sel[0][0], num + 2), "")
            self.view.replace(edit,
                              sublime.Region(sel[0][0] - 1, sel[0][0]),
                              skip + "$$\n")


class Changelayout(sublime_plugin.TextCommand):
    def run(self, edit):
        path = sublime.packages_path() + "\\" + user_path + \
            package_name + path_change_layout
        os.startfile(path)


class Createfolder(sublime_plugin.TextCommand):
    def run(self, edit):
        way_from_0 = sublime.packages_path() + "\\" + user_path + package_name + \
            "\\sources\\drafts\\0_draft_article"
        way_to = os.path.dirname(self.view.file_name())
        file_name = self.view.file_name()

        project_path = way_to + "\\project.sublime-project"

        os.makedirs(way_to + "\\settings")
        os.makedirs(way_to + "\\parts")
        # print("ok")
        os.remove(file_name)
        copy_tree(way_from_0, way_to)

        os.startfile(project_path)
        os.startfile(sublime.packages_path() + "\\User\\" +
                     package_name + path_close_recent_file)
        # print("ok x2")


class Createfile(sublime_plugin.TextCommand):
    def run(self, edit, folder):
        way_to = os.path.dirname(self.view.file_name())
        sel = [(s.begin(), s.end()) for s in self.view.sel()]
        num = sel[0][0] - 1
        file_name = ""
        while (self.view.substr(num) not in endings_list and num >= 0):
            file_name = self.view.substr(num) + file_name
            self.view.replace(edit, sublime.Region(num, num + 1), "")
            num -= 1
        file_name = file_name[:-1] + ".tex"
        f = open(way_to + "\\" + file_name, "w")
        f.close()


class Runpyfile(sublime_plugin.TextCommand):
    def run(self, edit, file_name):
        path = sublime.packages_path() + "\\" + user_path + \
            package_name + "\\sources\\" + file_name+".py"
        command = "python \"{}\"".format(path)
        print(command)
        os.system(command)


class Globalupdate(sublime_plugin.TextCommand):
    def run(self, edit):
        Runpyfile.run(self, edit, "snippets_generator")
        Runpyfile.run(self, edit, "keymaps_generator")
        Runpyfile.run(self, edit, "plugin_generator")

class Openkeymaps(sublime_plugin.TextCommand):
    def run(self, edit):
        keymaps_folder_path = sublime.packages_path() + "\\" + user_path + \
            package_name + "\\sources\\" + "keymaps"
        os.startfile(keymaps_folder_path)

class Updatesvg(sublime_plugin.TextCommand):
    def run(self, edit):
        tmp_path = self.view.project_name()
        print(tmp_path)
        print()






