import krita

from .widgets import PythonReferenceDialog


class PythonReferenceExtension(krita.Extension):

    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent

    def setup(self):
        pass

    def createActions(self, window):
        action = window.createAction(
            'python_reference', 'Python Reference', 'tools/scripts')
        action.triggered.connect(self.python_reference)

    def python_reference(self):
        dlg = PythonReferenceDialog(
            parent=self.parent.activeWindow().qwindow())
        dlg.show()
        dlg.activateWindow()


krita_instance = krita.Krita.instance()
krita_instance.addExtension(PythonReferenceExtension(krita_instance))
