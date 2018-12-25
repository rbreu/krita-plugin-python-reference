import krita

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QDialog,
    QLineEdit,
    QListWidget,
    QSplitter,
    QTextBrowser,
    QVBoxLayout,
    QWidget,
)


class PythonReferenceDialog(QDialog):

    def __init__(self, parent):
        """Initialise the GUI."""

        super(PythonReferenceDialog, self).__init__(parent=parent)
        self.setModal(False)
        self.setWindowTitle('Python API Reference')

        # The general layout
        outer_layout = QVBoxLayout()
        splitter = QSplitter(Qt.Horizontal)
        left_widget = QWidget()
        left_layout = QVBoxLayout()
        left_widget.setLayout(left_layout)
        splitter.addWidget(left_widget)
        outer_layout.addWidget(splitter)
        self.setLayout(outer_layout)
        self.resize(800, 800)

        # The search box
        self.search_widget = QLineEdit(self)
        self.search_widget.setPlaceholderText('search...')
        self.search_widget.setClearButtonEnabled(True)
        self.search_widget.textChanged.connect(
            lambda s: self.update_browser(s))
        left_layout.addWidget(self.search_widget)

        # The table of contents
        self.toc_widget = QListWidget()
        self.toc_widget.itemClicked.connect(lambda i: self.scroll_to(i))
        left_layout.addWidget(self.toc_widget)
        for (attr, name) in self.iter_krita_objects():
            self.toc_widget.addItem(name)

        # The text browser for the actual reference
        self.browser = QTextBrowser()
        self.update_browser()
        splitter.addWidget(self.browser)

        splitter.setStretchFactor(1, 10)

    def scroll_to(self, item):
        self.browser.scrollToAnchor(item.text())

    def update_browser(self, search_text=None):
        self.browser.setHtml(self.build_reference(search_text))

    def is_wanted_attr(self, attr, search_text=None):
        """Only collect attributes that aren't Python-internal
        (__xxx__) and that, if given, meet the search term."""

        if attr.startswith('__'):
            return False
        if not search_text:
            return True
        return search_text.lower() in attr.lower()

    def iter_krita_objects(self):
        """Get all classes from PyKrita.krita."""

        for name, attr in sorted(krita.__dict__.items()):
            try:
                module = attr.__module__
                if module == 'PyKrita.krita':
                    yield (attr, attr.__name__)
            except (TypeError, AttributeError):
                continue

    def build_reference(self, search_text=None):
        """Collect the actual reference and return as HTML."""

        doc = []
        for (obj, name) in self.iter_krita_objects():
            attrs = []
            for attr in dir(obj):
                if self.is_wanted_attr(attr, search_text):
                    attrs.append('<li>%s</li>' % attr)

            if attrs:
                doc.append('<h2><a id="%s">%s</a></h2>' % (name, name))
                doc.append('<ul>')
                doc.extend(attrs)
                doc.append('</ul>')

        return '\n'.join(doc)
