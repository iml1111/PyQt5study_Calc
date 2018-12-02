import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtCore import pyqtSlot

class Form(QWidget):
	def __init__(self):
		super().__init__()
		self.ui = uic.loadUi("IMLCalc.ui", self) #ui 파일 불러오기

		btn_list = [self.ui.btn1,self.ui.btn2,self.ui.btn3,self.ui.btn4,self.ui.btn5,
		self.ui.btn6,self.ui.btn7,self.ui.btn8,self.ui.btn9,self.ui.btn0,self.ui.btnplus,
		self.ui.btnminus,self.ui.btnmul,self.ui.btndiv,self.ui.btndiv_2,self.ui.btnopen,
		self.ui.btnclose]

		for i in btn_list:
			i.clicked.connect(\
				lambda state, button = i: self.write_edit(state, button))
	
		self.ui.show()

	@pyqtSlot()
	def write_edit(self, state, button):
		if self.ui.ledit.text() == "that's wrong expression!":
			self.ui.ledit.setText("")
		if button.text() == 'x':
			exp = '*'
		else:
			exp = button.text()
		self.ui.ledit.setText(self.ui.ledit.text() + exp)		

	@pyqtSlot()
	def one_delete(self):
		 arr = self.ui.ledit.text()
		 self.ledit.setText(arr[0:-1])

	@pyqtSlot()
	def answer(self):
		exp = self.ledit.text()
		try:
			self.ledit.setText(str(eval(exp)))
		except:
			self.ledit.setText("that's wrong expression!")


if __name__ == '__main__':
	app =QApplication(sys.argv)
	w = Form()
	sys.exit(app.exec())