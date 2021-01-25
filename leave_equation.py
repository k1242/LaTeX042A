import sublime
import sublime_plugin
import os

package_name = "LaTeX042A"

env_names_list = ["align", "align*",
                  "equation", "equation*",
                  "gather", "gather*"]


class GooutCommand(sublime_plugin.TextCommand):
    def run(self, edit):
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
        path_change_layout = "{}/{}/sources/vbs/change_layout.vbs".format(
            sublime.packages_path(), package_name)
        print(path_change_layout)
        os.startfile(path_change_layout)
