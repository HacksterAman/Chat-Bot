import sys
import time
import pyautogui
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.Qt import QStyle
from PyQt5.QtWidgets import QApplication, QLabel, QDesktopWidget, QSizePolicy, QWidget, QVBoxLayout, QHBoxLayout, QTextEdit, QPushButton, QMenu, QSystemTrayIcon, QAction, QFormLayout, QSpinBox

class Application(QWidget):
    def __init__(self):
        super().__init__()
        self.cursor = FloatingElements(1)
        self.crosshair = FloatingElements(2)
        self.menu()

    def menu(self):
        outerLayout = QVBoxLayout()
        self.text_field = QTextEdit(self)
        self.text_field.setPlaceholderText('Enter Your Text Here...')
        self.text_field.setAcceptRichText(True)
        outerLayout.addWidget(self.text_field)

        innerLayout1 = QHBoxLayout()
        label = QLabel("Delay:")
        label.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed) 
        innerLayout1.addWidget(label)
        self.spin_box1 = QSpinBox(self)
        self.spin_box1.setRange(0, 100)
        self.spin_box1.setMaximumWidth(45) 
        innerLayout1.addWidget(self.spin_box1)
        outerLayout.addLayout(innerLayout1)

        innerLayout2 = QHBoxLayout()
        label = QLabel("Multiple:")
        label.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed) 
        innerLayout2.addWidget(label)
        self.spin_box2 = QSpinBox(self)
        self.spin_box2.setRange(1, 10000)
        self.spin_box2.setMaximumWidth(60) 
        innerLayout2.addWidget(self.spin_box2)

        outerLayout.addLayout(innerLayout2)
        self.start_stop_button = QPushButton('Start', self)
        self.start_stop_button.clicked.connect(self.writer)
        self.start_stop_button.setStyleSheet("QPushButton { border-radius: 15px; background-color: green; min-width: 60px; min-height: 30px; }")
        outerLayout.addWidget(self.start_stop_button)
        self.setLayout(outerLayout)
        
        screen_rect = QApplication.desktop().screenGeometry()
        window_width = 300
        window_height = 150
        self.setGeometry(screen_rect.width() - window_width, 0, window_width, window_height)
        self.setWindowFlag(Qt.WindowStaysOnTopHint)
        self.setWindowFlag(Qt.WindowMaximizeButtonHint, False)
        self.setWindowTitle('Chat Bot')
        self.show()

    def writer(self):
        text=self.text_field.toPlainText()
        lines = text.split('\n')
        messages = [line.strip() for line in lines if line.strip()]
        cursorPos=self.cursor.position()
        crosshairPos=self.crosshair.position()
        delay=self.spin_box1.value()
        multiple=self.spin_box2.value()
        self.cursor.hide()
        self.crosshair.hide()

        for i in range(multiple):
            for message in messages:
                pyautogui.click(cursorPos)
                pyautogui.write(message)
                time.sleep(delay)
                pyautogui.click(crosshairPos)
        
        self.cursor.show()
        self.crosshair.show()

    def closeEvent(self, event):
        self.cursor.close()
        self.crosshair.close()
        self.close()

class FloatingElements(QWidget): 
    def __init__(self,element):
        super().__init__()
        desktop = QDesktopWidget()
        screen_rect = desktop.screenGeometry(desktop.primaryScreen())
        self.label = QLabel(self)

        if element == 1:
            initial_x = screen_rect.width() // 2 - self.label.width() // 2 - 100
            icon_path = "cursor.png"

        elif element == 2:
            initial_x = screen_rect.width() // 2 - self.label.width() // 2 + 100
            icon_path = "crosshair.png"

        initial_y = screen_rect.height() // 2 - self.label.height() // 2
        pixmap = QPixmap(icon_path)
        self.label.setPixmap(pixmap)
        self.label.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        self.label.setAlignment(Qt.AlignTop | Qt.AlignLeft)
        self.setGeometry(initial_x, initial_y, pixmap.width(), pixmap.height())
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setWindowFlag(Qt.WindowStaysOnTopHint)
        self.setWindowTitle('Chat Bot')
        self.draggable = False
        self.offset = None
        self.show()

    def position(self):
        center_x = self.pos().x() + self.label.width() // 2
        center_y = self.pos().y() + self.label.height() // 2
        return (center_x, center_y)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.draggable = True
            self.offset = event.pos()

    def mouseMoveEvent(self, event):
        if self.draggable:
            self.move(event.globalPos() - self.offset)

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.draggable = False

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon('bot.png'))
    chatbot = Application()
    sys.exit(app.exec_())
