import sys, subprocess, time, os
from PyQt5.QtWidgets import (QWidget, QMessageBox, QLabel, QLineEdit, QAction, QFileDialog, QTextEdit, QGridLayout, QRadioButton, QPushButton, QApplication, QInputDialog, QSystemTrayIcon, QTabWidget, QListWidget, QListWidgetItem, QSplitter, QVBoxLayout, QHBoxLayout, QMainWindow, QAction, QDialog, QMenuBar)
from PyQt5 import QtGui, QtWidgets, QtCore, Qt
from PyQt5.QtGui import QIcon, QWindow
class MainClass(QWidget):
	def __init__(self):
		super().__init__()
		self.initUI()
	def downloadVid(self):
		link = self.mainBox.text()
		msgDialog = QMessageBox()
		msgDialog.setText("Please note that the program will freeze while the video is downloading. Please wait until the program says Done.")
		msgDialog.exec_()
		if self.mp4Button.isChecked() == True:
			subprocess.call(["youtube-dl", "-o", self.directoryBox.text() + "\\" + self.fileNameBox.text(), link])
			self.consoleLabel.setText("Done")
		else:
			subprocess.call(["youtube-dl", "-o", self.directoryBox.text() + "\\" + self.fileNameBox.text() + ".%%(ext)s" , "--extract-audio", "--audio-format", "mp3", link])
			self.consoleLabel.setText("Done")
	def showDialog(self):
		fname = QFileDialog.getExistingDirectory()
		if fname[0]:
			self.directoryBox.setText(fname)
	def initUI(self):
		self.firstRow = QHBoxLayout()
		self.secondRow = QHBoxLayout()
		self.thirdRow = QHBoxLayout()
		self.fourthRow = QHBoxLayout()
		self.fifthRow = QHBoxLayout()
		self.mainLayout = QVBoxLayout()
		self.directoryLabel = QLabel("Select directory")
		self.directoryBox = QLineEdit()
		self.directoryBox.setText("C:" + os.environ["HOMEPATH"])
		self.openButton = QPushButton("Browse")
		self.openButton.clicked.connect(self.showDialog)
		self.fileNameLabel = QLabel("File Name: ")
		self.fileNameBox = QLineEdit()
		self.fileNameBox.setText("downloadedYoutubeFile")
		self.downloadLabel = QLabel("YouTube Link: ")
		self.mainBox = QLineEdit()
		self.mainButton = QPushButton("Download")
		self.mainButton.clicked.connect(self.downloadVid)
		self.mp4Button = QRadioButton("Video")
		self.mp3Button = QRadioButton("Audio")
		self.mp4Button.setChecked(True)
		self.consoleLabel = QLabel("Standby")
		self.firstRow.addWidget(self.directoryLabel)
		self.firstRow.addWidget(self.directoryBox)
		self.firstRow.addWidget(self.openButton)
		self.secondRow.addWidget(self.fileNameLabel)
		self.secondRow.addWidget(self.fileNameBox)
		self.thirdRow.addWidget(self.downloadLabel)
		self.thirdRow.addWidget(self.mainBox)
		self.fourthRow.addWidget(self.mp4Button)
		self.fourthRow.addWidget(self.mp3Button)
		self.fifthRow.addWidget(self.consoleLabel)
		self.fifthRow.addStretch(1)
		self.fifthRow.addWidget(self.mainButton)
		self.mainLayout.addLayout(self.firstRow)
		self.mainLayout.addLayout(self.secondRow)
		self.mainLayout.addLayout(self.thirdRow)
		self.mainLayout.addLayout(self.fourthRow)
		self.mainLayout.addLayout(self.fifthRow)
		self.setLayout(self.mainLayout)
		self.setWindowTitle("YouTube Download")
		self.setGeometry(300, 300, 300, 300)
		self.show()
app = QApplication(sys.argv)
ex = MainClass()
app.exec_() # Executes GUI