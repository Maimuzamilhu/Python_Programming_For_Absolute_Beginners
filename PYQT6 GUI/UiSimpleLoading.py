import PyQt6.QtWidgets as MyQtWidgets
import PyQt6.uic as MyUic
#------------------
MyApp=MyQtWidgets.QApplication([])
#------------------
MyWind=MyQtWidgets.QMainWindow()
MyUic.loadUi("Data/Musavi.ui",MyWind)
#------------------
MyWind.setWindowTitle("Hello Qt World!")
#------------------
MyWind.show()
MyApp.exec()
print("Is Done!")