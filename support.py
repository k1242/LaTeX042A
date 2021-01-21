import sublime
import sublime_plugin
import os

package_name = "LaTeX042A"
lz_settings_file = "LaTeXPhys.sublime-settings"


# open folder
class Openfolder(sublime_plugin.TextCommand):
    def run(self, edit, folder_name):
        keymaps_folder_path = "{}/{}/{}".format(
            sublime.packages_path(), package_name, folder_name)
        os.startfile(keymaps_folder_path)


# run the python file
class Runpyfile(sublime_plugin.TextCommand):
    def run(self, edit, file_name):
        path = "{}\\{}\\sources\\{}.py".format(
            sublime.packages_path(), package_name, file_name)
        command = "python \"{}\"".format(path)
        print(command)
        os.system(command)


# update keymaps and snippets list
class Globalupdate(sublime_plugin.TextCommand):
    def run(self, edit):
        Runpyfile.run(self, edit, "snippets_generator")
        Runpyfile.run(self, edit, "keymaps_generator")


# test settings file
class Testсommand(sublime_plugin.TextCommand):
    def run(self, edit):
        # settings = sublime.load_settings(lz_settings_file)
        # t1 = settings.get("test_var_false")
        # t2 = settings.get("test_var_true")
        # print(t1)
        # print(t2)
        os.system("tasklist")














