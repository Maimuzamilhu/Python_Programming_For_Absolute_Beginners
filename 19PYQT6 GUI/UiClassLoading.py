import PyQt6.QtWidgets as MyQtWidgets
import PyQt6.uic as MyUic
#---------My Class----------
class MyUiWindow(MyQtWidgets.QMainWindow):
      def __init__(self):
            super(MyUiWindow, self).__init__()
            MyUic.loadUi("Data/Musavi.ui",self )
            #self.setWindowTitle("Hello Qt World!")

#------------------
MyApp=MyQtWidgets.QApplication([])
#------------------
#MyWind=MyQtWidgets.QMainWindow()
#MyUic.loadUi("Data/Musavi.ui",MyWind)
MyWind=MyUiWindow()
#------------------
MyWind.setWindowTitle("Hello Qt World!")
#------------------
MyWind.show()
MyApp.exec()
print("Is Done!")