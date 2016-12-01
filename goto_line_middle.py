import sublime_plugin


class GoLineMiddle(sublime_plugin.TextCommand):
    def run(self, edit):
        view = self.view
        line = view.substr(view.line(view.sel()[0]))
        if not len(line):
            return
        line = line.strip()
        self.view.run_command("move_to", {"to": "bol",})
        for i in range(0, len(line)//2):
            self.view.run_command("move", {"by": "characters", "forward": True})

