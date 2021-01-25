import sublime
import sublime_plugin


package_name = "LaTeX042A"
lz_settings_file = "LaTeX042A.sublime-settings"


endings_list = [
    " ", "\n", "\t", "|",
    "[", "(", "{", "}", ")", "]",
    "`", "$", "^", "~", "'",
    "-", "+"
]
nums_list = list("0123456789")


# add environment to the previous word
class AddenvCommand(sublime_plugin.TextCommand):
    def run(self, edit, env_name):
        print("add env: OK")
        sel = [(s.begin(), s.end()) for s in self.view.sel()]
        num = sel[0][0] - 1
        self.view.insert(edit, num + 1, "}")
        while (self.view.substr(num) not in (endings_list + nums_list) and num >= 0):
            if (self.view.substr(num) == "_"):
                self.view.replace(edit, sublime.Region(num, num + 1), " ")
            num -= 1
        self.view.insert(edit, num + 1, "\\" + env_name + "{")
