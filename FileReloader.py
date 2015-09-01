import sublime, sublime_plugin

class ReloadAllFilesCommand(sublime_plugin.WindowCommand):
  def run(self):
    self.focus_all_views()

  def focus_all_views(self):
    window = self.window
    saved_view = window.active_view()
    total_groups = window.num_groups()

    for i in range(0, total_groups):
      window.focus_group(i)
      views = window.views_in_group(i)

      # Reload all views in current group
      for inner_view in views:
        window.focus_view(inner_view)
        window.run_command("revert")

    # Set the focus back to the saved view
    window.focus_view(saved_view)
