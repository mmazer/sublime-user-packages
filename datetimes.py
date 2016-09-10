import sublime_plugin
import datetime

DATE_TIMESTAMP_FORMAT = "%Y-%m-%d %H:%M:%S"
DATE_FORMAT = "%Y-%m-%d"
TIMESTAMP_FORMAT = "%H:%M:%S"


class AddDateTimeStampCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        now = datetime.datetime.now()
        self.view.run_command("insert_snippet",
                              {"contents": "%s" %
                               now.strftime(DATE_TIMESTAMP_FORMAT)})


class AddDateStampCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        now = datetime.datetime.now()
        self.view.run_command("insert_snippet",
                              {"contents": "%s" %
                               now.strftime(DATE_FORMAT)})


class AddTimeStampCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        now = datetime.datetime.now()
        self.view.run_command("insert_snippet",
                              {"contents": "%s" %
                               now.strftime(TIMESTAMP_FORMAT)})
