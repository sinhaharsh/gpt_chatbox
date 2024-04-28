
import sys
from PySide6 import QtWidgets
from PySide6.QtUiTools import QUiLoader
from widget import Widget

def main():
    app = QtWidgets.QApplication(sys.argv)
    window = Widget()
    window.show()
    app.exec()


# # from PySide6.QtWidgets import QApplication, QWidget
# # import sys

# # from mainwindow import MainWindow

# # def main():
# #     app = QApplication(sys.argv)
# #     # By default, window is hidden, so we need to show
# #     window = MainWindow(app)
# #     window.show()

# #     # start the event loop
# #     app.exec()

if __name__ == "__main__":
    main()

# # import sys
# # from PyQt6.QtGui import QGuiApplication
# # from PyQt6.QtQml import QQmlApplicationEngine
# # from PyQt6.QtQuick import QQuickWindow

# # def main():
# #     QQuickWindow.setSceneGraphBackend('software')
# #     app = QGuiApplication(sys.argv)
# #     engine = QQmlApplicationEngine()
# #     engine.quit.connect(app.quit)
    
# #     try:
# #         engine.load('./ui/main.qml')
# #         if not engine.rootObjects():
# #             raise Exception("Failed to load QML file")
# #         sys.exit(app.exec())
# #     except Exception as e:
# #         print(f"An error occurred: {e}")
# #         sys.exit(1)

# # if __name__ == "__main__":
# #     main()
