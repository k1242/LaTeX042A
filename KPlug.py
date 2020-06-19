import sublime
import sublime_plugin
import os
from distutils.dir_util import copy_tree


change_language_way = "D:\\Kami\\sourses\\change_language.vbs"
sublime_exe = "C:\\Program Files\\Sublime Text 3\\sublime_text.exe"
close_recent_file_way = "D:\\Kami\\sourses\\close_recent_file.vbs"
package_name = "KPlug"
path_change_layout = "\\sources\\vbs\\change_layout.vbs"
path_close_recent_file = "\\sources\\vbs\\close_recent_file.vbs"


env_names_list = ["align", "equation"]

endings_list = [
    " ", "\n", "\t",
    "[", "(", "{",
    "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", 
    "`", "$", "^"
]
exceptions = ["_", "-", "+", "=", "*", "/"]

num_list = list("0123456789")

# eng_lowercase = "qwertyuiop[]asdfghjkl;'zxcvbnm,./"
# eng_upercase  = 'QWERTYUIOP{}ASDFGHJKL:"ZXCVBNM<>?'
# eng_list = list(eng_lowercase + eng_upercase)
# rus_lowercase = "йцукенгшщзхъфывапролджэячсмитьбю."
# rus_upercase  = "ЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮ,"
# rus_list = list(rus_lowercase + rus_upercase)


class AddvectorCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        sel = [(s.begin(), s.end()) for s in self.view.sel()]
        num = sel[0][0]
        self.view.insert(edit, num, "}")
        num -= 2
        self.view.insert(edit, num + 1, "\\vc{")

class AddtextitCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        sel = [(s.begin(), s.end()) for s in self.view.sel()]
        num = sel[0][0]
        self.view.insert(edit, num, "}")
        while (self.view.substr(num) not in endings_list and num >= 0):
            if (self.view.substr(num) == "_"):
                print(self.view.word(num))
                print(type(self.view.word(num)))
                self.view.replace(edit, sublime.Region(num, num+1), " ")
            num -= 1
        self.view.insert(edit, num + 1, "\\" + "textit" + "{")


# class ChangelanguageCommand(sublime_plugin.TextCommand):
#     def run(self, edit):
#         sel = [(s.begin(), s.end()) for s in self.view.sel()]
#         num = sel[0][0]
#         while (self.view.substr(num-1) not in endings_list and num >= 0):
#             char = self.view.substr(num)
#             if (char in eng_list):
#                 ind = eng_list.index(char)
#                 self.view.replace(edit, sublime.Region(num, num+1), rus_list[ind])
#             if (char in rus_list):
#                 ind = rus_list.index(char)
#                 self.view.replace(edit, sublime.Region(num, num+1), eng_list[ind])
#             if (self.view.substr(num) == "_"):
#                 print(self.view.word(num))
#                 print(type(self.view.word(num)))
#                 self.view.replace(edit, sublime.Region(num, num+1), " ")
#             num -= 1
#         char = self.view.substr(num)
#         if (char in eng_list):
#             ind = eng_list.index(char)
#             self.view.replace(edit, sublime.Region(num, num+1), rus_list[ind])
#         if (char in rus_list):
#             ind = rus_list.index(char)
#             self.view.replace(edit, sublime.Region(num, num+1), eng_list[ind])

class GooutCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        os.startfile(change_language_way)
        sel = [(s.begin(), s.end()) for s in self.view.sel()]
        num = sel[0][0]
        flag = 0
        skip = self.view.substr(num-1)

        env_end_flag = False
        while (flag < 400 and self.view.substr(num) != "$"):
            skip += self.view.substr(num)
            flag += 1
            num  += 1

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
                sublime.Region(sel[0][0]-1, sel[0][0]), 
                skip + "\n")
            # print("case №0")
        elif (self.view.substr(num+1) != "$"):
            self.view.replace(edit, sublime.Region(sel[0][0], num+1), "")
            self.view.replace(edit, 
                sublime.Region(sel[0][0]-1, sel[0][0]), 
                skip + "$ ")
            # print("case №1")
        else:
            self.view.replace(edit, sublime.Region(sel[0][0], num+2), "")
            self.view.replace(edit, 
                sublime.Region(sel[0][0]-1, sel[0][0]), 
                skip + "$$\n")
            # print("case №2")

# class GoinCommand(sublime_plugin.TextCommand):
#     def run(self, edit):
#         os.startfile(change_language_way)
#         sel = [(s.begin(), s.end()) for s in self.view.sel()]
#         num = sel[0][0]
#         char = self.view.substr(num)
#         self.view.replace(edit, sublime.Region(num, num+1), "$ ")
#         self.view.insert(edit, num+2, "$" + char)


class NumtreatmentCommand(sublime_plugin.TextCommand):
    def run(self, edit, numeral):
        sel = [(s.begin(), s.end()) for s in self.view.sel()]
        num = sel[0][0]
        char = self.view.substr(num-1)
        if (char not in endings_list + exceptions):
            self.view.insert(edit, num, "_{" + str(numeral) + "}")
        else:
            self.view.insert(edit, num, str(numeral))


class Changelayout(sublime_plugin.TextCommand):
    def run(self, edit):
        path = sublime.packages_path() + "\\User\\" + package_name + path_change_layout
        os.startfile(path)

class Createfolder(sublime_plugin.TextCommand):
    def run(self, edit):
        way_from_0 = sublime.packages_path() + "\\User\\KPlug\\sources\\drafts\\0_draft_article"
        way_to   = os.path.dirname(self.view.file_name())
        file_name =  self.view.file_name()

        project_path = way_to + "\\project.sublime-project"

        os.makedirs(way_to + "\\settings")
        os.makedirs(way_to + "\\parts")
        print("ok")
        os.remove(file_name)
        copy_tree(way_from_0, way_to)

        os.startfile(project_path)
        os.startfile(sublime.packages_path() + "\\User\\" + package_name + path_close_recent_file)
        print("ok x2")



class DeletespaceCommand(sublime_plugin.TextCommand):
    def run(self, edit, char):
        sel = [(s.begin(), s.end()) for s in self.view.sel()]
        num = sel[0][0]
        end_char = self.view.substr(num-1)
        if (end_char in [" "]):
            self.view.replace(edit, sublime.Region(num-1, num), char + " ")
        else:
            self.view.insert(edit, num, char)


