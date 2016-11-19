import sublime_plugin
import os


class FileStatus(sublime_plugin.EventListener):
    def on_modified_async(self, view):
        self.update_status(view)

    def on_post_save_async(self, view):
        self.update_status(view)

    def on_activated_async(self, view):
        self.update_status(view)

    def on_post_text_command(self, view, command, arg):
        if command == "_vi_u" or command == "undo":
            self.update_status(view)

    def update_status(self, view):
        filename = self.getfilename(view)
        readonly = view.is_read_only()
        modified = view.is_dirty()
        status = []

        status.append(filename)
        if (modified):
            status.append('+')

        if (readonly):
            status.append(' RO')

        lines = (view.rowcol(view.size())[0] + 1)
        if lines > 1:
            status.append(' %dL' % (view.rowcol(view.size())[0] + 1))

        view.set_status("01.file_info_status", "".join(status))

    def getfilename(self, view):
        filename = view.file_name()
        if not filename:
            return "[No Name]"

        cwd = self.getcwd(view)
        cwd = cwd + os.path.sep
        if filename.startswith(cwd):
            filename = filename.replace(cwd, "")

        return filename

    def getcwd(self, view):
        f = view.file_name()
        cwd = None
        window = view.window()
        if window:
            pd = window.project_data()
            if pd:
                cwd = pd.get("folders")[0].get("path")
        if not cwd:
            if f:
                cwd = os.path.dirname(f)

        return cwd
