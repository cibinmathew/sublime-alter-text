import sublime
import sublime_plugin


class ReplaceTextWithCommand(sublime_plugin.TextCommand):
    def run(self, edit, replacement=""):
        regions = self.view.sel()
        for region in regions:
            region_text = self.view.substr(region)
            replacement_text = replacement * len(region_text)
            self.view.replace(edit, region, replacement_text)
