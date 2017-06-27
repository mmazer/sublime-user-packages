import sublime_plugin
import datetime

DATE_TIMESTAMP_FORMAT = "%Y-%m-%d %H:%M:%S"
DATE_TIME_FORMAT = "%Y-%m-%d %H:%M"
DATE_FORMAT = "%Y-%m-%d"
TIMESTAMP_FORMAT = "%H:%M:%S"


class AddDateTimeStampCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        self.view.run_command("insert_snippet",
                              {"contents": "%s" %
                               str_now(DATE_TIMESTAMP_FORMAT)})


class AddDateTimeCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        self.view.run_command("insert_snippet",
                              {"contents": "%s" %
                               str_now(DATE_TIME_FORMAT)})


class AddDateStampCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        self.view.run_command("insert_snippet",
                              {"contents": "%s" %
                               str_now(DATE_FORMAT)})


class AddTimeStampCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        self.view.run_command("insert_snippet",
                              {"contents": "%s" %
                               str_now(TIMESTAMP_FORMAT)})


def str_now(format):
    return datetime.datetime.now().strftime(format)
