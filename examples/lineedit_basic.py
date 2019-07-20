from entrywidget import AutoColorLineEdit
from PyQt5.Qt import QApplication
from PyQt5 import QtWidgets
import sys
import logging


app = QApplication(sys.argv)


def detect_error(w):
    return w.text() == 'error'

def announce_error(w):
    print(w.name + ': There IS an Error')

def announce_no_error(w):
    print(w.name + ': There is NO Error')

def print_entered_text(w):
    print(w.name + ": Entered Text is '"+ w.text() + "'")

def do_whats_typed(w):
    if w.text() == 'auto':
        print(w.name + ": Changing to Automatic colors")
        w.setAutoColors()
    if w.text() == 'manual':
        print(w.name + ": Changing to Manual colors")
        w.setColors(('black', 'white'))
    if w.text() == 'readonly':
        w.setReadOnly(True)
        print(w.name + ': Entry is ReadOnly')
    if w.text() == 'disable':
        w.setEnabled(False)
        print(w.name + ': Entry is Disabled')
    if w.text() == 'close':
        print(w.name + ': Closing Window')
        w.window().close()

logging.basicConfig(stream=sys.stdout, level=logging.INFO)
widgetDefault = AutoColorLineEdit()
widgetDefault.setText("Basic Widget")
widgetDefault.show()
app.exec_()

widgetDefault = AutoColorLineEdit()
widgetDefault.errorCheck = lambda: detect_error(widgetDefault)
widgetDefault.setText("Type 'error'")
widgetDefault.show()
app.exec_()

widgetDefault = AutoColorLineEdit(liveErrorChecking=False)
widgetDefault.errorCheck = lambda: detect_error(widgetDefault)
widgetDefault.setText("Type 'error', press ENTER")
widgetDefault.show()
app.exec_()


widget0 = AutoColorLineEdit(
    objectName='widget0',  # object name inside Qt, also can be used for logging
    text='startPrompt',  # box's text on startup
    liveErrorChecking=True,  # whether to run isError() every text change, or only when editing is finished
    readOnly=False  # whether the text box is readOnly or not
)
widget0.errorCheck = lambda: detect_error(widget0)
widget0.hasError.connect(lambda e: announce_error(widget0))
widget0.textChanged.connect(lambda t: print_entered_text(widget0))
widget0.editingFinished.connect(lambda: do_whats_typed(widget0))
widget0.setToolTip(
    """
Typing anything causes:
    error checking (liveErrorChecking=True)
    log the new text (textChanged)

Typing 'error' causes:
    box to have error (errorCheck)
    log the error (hasError)

Typing 'close', 'readonly', or 'disable' and pressing RETURN/ENTER:
    closes the window ; makes box readonly ; disables box entirely
    (editingFinished)
"""
)


widget1 = AutoColorLineEdit(objectName='widget1')
widget1.errorCheck = lambda: detect_error(widget1)
widget1.hasError.connect(lambda: announce_error(widget1))
widget1.editingFinished.connect(lambda: print_entered_text(widget1))
widget1.setToolTip(
    """
Typing anything causes:
    error checking (liveErrorChecking=True)

Typing 'error' causes:
    box to have error (errorCheck)
    log the error (hasError)
    
Hit ENTER / finish editing causes:
    print the entered text (editingFinished)
"""
)

widget2 = AutoColorLineEdit(
    objectName='widget 2',
    text='error',
    liveErrorChecking=False
)
widget2.errorCheck = lambda: detect_error(widget2)
widget2.hasError.connect(lambda: announce_error(widget2))
widget2.errorCleared.connect(lambda: announce_no_error(widget2))
widget2.editingFinished.connect(lambda: do_whats_typed(widget2))
widget2.setToolTip(
    """
Typing DOES NOT cause error checking (liveErrorChecking=False)

Typing then pressing RETURN/ENTER causes:
    errorCheck (liveErrorChecking=False)
    log the error (hasError)
    log lack of error (errorCleared)

Typing 'close', 'readonly', or 'disable' and pressing RETURN/ENTER:
    closes the window ; makes box readonly ; disables box entirely
    (editingFinished)
"""
)

print("\n-----------------------")
widget3 = AutoColorLineEdit(
    text="custom colors",
    liveErrorChecking=False
)
widget3.textChanged.connect(lambda: do_whats_typed(widget3))
widget3.setColors(('black', 'white'))
widget3.setObjectName('widget 3')
widget3.setToolTip(
    """
Typing DOES NOT cause error checking (liveErrorChecking=False)

Typing 'close', 'readonly', or 'disable':
    closes the window ; makes box readonly ; disables box entirely
    (textChanged)
"""
)

print("\n-----------------------")
window = QtWidgets.QWidget()
window.setObjectName('main window')
layout = QtWidgets.QVBoxLayout(window)
layout.addWidget(widgetDefault)
layout.addWidget(widget0)
layout.addWidget(widget1)
layout.addWidget(widget2)
layout.addWidget(widget3)

info = QtWidgets.QTextEdit(
    """
The boxes that accept 
close/disable/readonly, 
also accept:
'auto' and 'manual' to change colors.
    """, window)
layout.addWidget(info)

window.setLayout(layout)
window.show()
app.exec_()
