import PyQt6.QtWidgets as MyWidgets

#---------------
MyApp=MyWidgets.QApplication([])
#--------------------
MyWind=MyWidgets.QMainWindow()
MyWind.setWindowTitle("Hello PyQt6!")
MyWind.setGeometry(0,0,500,300)#=> (x, y, width, height )
#--------------------
lbl=MyWidgets.QLabel(MyWind)
lbl.setText("First Name:")
lbl.setGeometry(10,10,80,30)#=> (x, y, width, height )
#lbl.setVisible(True)
#--------------------
Butt=MyWidgets.QPushButton(MyWind)
Butt.setText("First Name:")
Butt.setGeometry(10,60,80,30)#=> (x, y, width, height )
#Butt.setVisible(True)
#--------------------
MyWind.show()
MyApp.exec()
print("Done!")