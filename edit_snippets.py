import sublime
import sublime_plugin
import os

package_name = "LaTeX042A"


class Edit_snippets(sublime_plugin.WindowCommand):
    def run(self):

        file_path = "{}/User/{}".format(sublime.packages_path(), package_name)
        file_name = file_path + "/snippets.txt"
        default_file_name = "{}/{}/settings/snippets_list.txt".format(
            sublime.packages_path(), package_name)

        if not os.path.exists(file_path):
            os.mkdir(file_path)
            print("042A: created user's directory")
        if not os.path.exists(file_name):
            open(file_name, "a").close()
            print("042A: created user's snippets file")

        self.window.run_command("new_window")
        new_window = sublime.windows()[-1]
        new_window.open_file(default_file_name)
        new_window.run_command("set_layout",
                               {
                                   "cells": [[0, 0, 1, 1], [1, 0, 2, 1]],
                                   "cols": [0.0, 0.5, 1.0],
                                   "rows": [0.0, 1.0]
                               })
        new_window.open_file(file_name)


class Edit_keymaps(sublime_plugin.WindowCommand):
    def run(self):

        file_path = "{}/User/{}".format(sublime.packages_path(), package_name)
        file_name = file_path + "/keymaps.json"
        default_file_name = "{}/{}/support/Default.sublime-keymap".format(
            sublime.packages_path(), package_name)

        if not os.path.exists(file_path):
            os.mkdir(file_path)
            print("042A: created user's directory")
        if not os.path.exists(file_name):
            open(file_name, "a").close()
            print("042A: created user's keymaps file")

        self.window.run_command("new_window")
        new_window = sublime.windows()[-1]
        new_window.open_file(default_file_name)
        new_window.run_command("set_layout",
                               {
                                   "cells": [[0, 0, 1, 1], [1, 0, 2, 1]],
                                   "cols": [0.0, 0.5, 1.0],
                                   "rows": [0.0, 1.0]
                               })
        new_window.open_file(file_name)


# self.window.status_message("042A: test status message")
# print("num_groups =", w.num_groups())
# print("active_group =", w.active_group())
# w.focus_group(1)
# print(w.active_sheet())
# self.window.status_message("042A: opened snippets file")
