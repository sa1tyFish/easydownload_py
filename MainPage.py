#Author:Azrael
import sys
from PyQt5.QtWidgets import QApplication, QDialog, QStackedWidget,QListWidget,\
    QTextEdit,QVBoxLayout,QListWidgetItem


class MainPage(QDialog):
    def __init__(self, parent=None):
        super(MainPage, self).__init__(parent)
        self.initUI()

    def initUI(self):

        self.setWindowTitle("sa1tFish")
        self.setGeometry(200, 200, 800, 400)



        self.selectList = QListWidget()
        self.Item = QListWidgetItem()
        self.selectList.setFlow(QListWidget.LeftToRight)
        self.selectList.addItems(["function1","function2","function3"])
        self.selectList.setMaximumHeight(40)
        self.selectList.setMinimumHeight(20)




        self.resultEdit1 = QTextEdit("function1--result1--111",self)
        self.resultEdit2 = QTextEdit("function2--result2--222",self)
        self.resultEdit3 = QTextEdit("function3--result3--333",self)

        self.stack = QStackedWidget()
        self.stack.addWidget(self.resultEdit1)
        self.stack.addWidget(self.resultEdit2)
        self.stack.addWidget(self.resultEdit3)

        layout = QVBoxLayout(self)
        layout.addWidget(self.selectList)
        layout.addWidget(self.stack)
        layout.setStretch(0,1)
        layout.setStretch(1,20)



        self.selectList.currentRowChanged.connect(self.stack.setCurrentIndex)
        self.setMinimumHeight(200)
        self.show()
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainPage()
    sys.exit(app.exec_())
