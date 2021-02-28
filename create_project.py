import sublime
import sublime_plugin
import shutil
import subprocess
import os

package_name = "LaTeX042A"
path_d = "C:\\Users\\aleks\\Desktop\\tmp_JS"
path_s = "C:\\Users\\aleks\\AppData\\Roaming\\Sublime Text 3\\Packages\\LaTeX042A\\sources\\templates\\notes"

def copytree(src, dst, symlinks=False, ignore=None):
    for item in os.listdir(src):
        s = os.path.join(src, item)
        d = os.path.join(dst, item)
        if os.path.isdir(s):
            shutil.copytree(s, d, symlinks, ignore)
        else:
            shutil.copy2(s, d)

# sublime_lib.copytree
class Testtt(sublime_plugin.WindowCommand):
    def get_spath(self):
        return os.listdir("{}/{}/sources/templates".format(
                sublime.packages_path(), package_name))

    def tmp_path(self, tmp_name):
        path_s = "{}/{}/sources/templates/{}".format(
            sublime.packages_path(), package_name, tmp_name)
        return path_s

    def open_project(self, item):
        p = path_d+"//project.sublime-project"
        item = self.get_spath()[item]
        print(item)
        try:
            copytree(self.tmp_path(item), path_d)
            print("end")
        except:
            print("project already exists")
        subprocess.Popen(sublime.executable_path() + " " + p) 

    def run(self):
        print("start")
        self.window.show_quick_panel(
            self.get_spath(),
            self.open_project)
