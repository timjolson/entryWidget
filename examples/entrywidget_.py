import pytest

from entrywidget import EntryWidget
import sys

# Qt stuff
from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication
app = QApplication(sys.argv)

# logging stuff
import logging
logging.basicConfig(stream=sys.stdout, level=logging.INFO)

# <editor-fold desc="Support Funcs">
def change_color_on_option(entry_widget):
    print('change_color to', entry_widget.getSelected())
    entry_widget.setColors((entry_widget.getSelected(), 'black'))
# </editor-fold>


print("\n----------------------- Default")
widget = EntryWidget()
widget.setWindowTitle('Default')
widget.show()
app.exec_()

print("\n----------------------- Standard Usage")
widget = EntryWidget(options=['opt1', 'opt2', 'opt3'], text='Prompt Text')
widget.setWindowTitle('Standard usage')
widget.show()
app.exec_()

print("\n----------------------- Printing text")
widget = EntryWidget(text='type here')
widget.textChanged[str].connect(print)
widget.setWindowTitle('Print text')
widget.show()
app.exec_()

print("\n----------------------- Select a Color")
widget = EntryWidget(options=['white', 'red', 'blue', 'orange'], text='pick a color')
widget.optionChanged.connect(lambda: change_color_on_option(widget))
widget.setWindowTitle('Select a Color')
widget.show()
app.exec_()
