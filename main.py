import sys
import psycopg2
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QDialog, QMainWindow, QApplication, QStackedWidget, QGridLayout, QFrame, QLabel, QWidget, QMessageBox
from ui_login import Ui_Form
from ui_staff import StaffTab
from ui_schedule1 import ScheduleTab
from wesdw import widgets  # Ensure this imports the correct widget class

# Database connection setup
conn = psycopg2.connect(host='localhost', dbname='insurgent_db', user='postgres', password='admin', port='5432')
cur = conn.cursor()

class AddSchedScreen(QWidget):  # Changed to QWidget
    def __init__(self, stacked_widget):
        super(AddSchedScreen, self).__init__()
        self.stacked_widget = stacked_widget
        self.setMinimumSize(1280, 720)
        self.setWindowTitle('Add Schedule Screen')

        # Use the MainWindow content from grip.py
        self.initUI()

    def initUI(self):
        grid_layout = QGridLayout(self)  # Creating a grid layout

        self.frame2 = QFrame(self)
        self.frame = QFrame(self)

        self.frame2.setStyleSheet("background-color:#f2f2f2;")

        self.block = QLabel(self.frame)
        self.frame.setStyleSheet("background-color: orange;")
        self.block.setStyleSheet("background-color: green;")

        self.f = widgets(self.frame)
        self.f.setStyleSheet("background-color:lightgrey;")

        grid_layout.addWidget(self.frame, 1, 0)
        grid_layout.addWidget(self.frame2, 0, 0)
        self.setLayout(grid_layout)

    def resizeEvent(self, event):
        frame_width = int(self.height() * 0.8)
        self.frame.setFixedHeight(frame_width)
        self.f.setGeometry(0, 0, int(self.frame.width()), int(self.frame.height()))
        super().resizeEvent(event)  # Ensure the base class resizeEvent is also called

class StaffScreen(QMainWindow):  # Changed to QMainWindow
    def __init__(self, stacked_widget):
        super(StaffScreen, self).__init__()
        self.ui = StaffTab()
        self.ui.setupUi(self)  # Set up the UI
        self.stacked_widget = stacked_widget
        self.ui.schedbtn.clicked.connect(self.open_schedule)  # Connect to the open_schedule method
        
    def open_schedule(self):
        sched = ScheduleScreen(self.stacked_widget)
        self.stacked_widget.addWidget(sched)
        self.stacked_widget.setCurrentWidget(sched)

class ScheduleScreen(QMainWindow):
    def __init__(self, stacked_widget):
        super(ScheduleScreen, self).__init__()
        self.ui = ScheduleTab()
        self.ui.setupUi(self)  # Set up the UI
        self.stacked_widget = stacked_widget
        # Ensure the button is correctly referenced
        if hasattr(self.ui, 'staffbtn'):
            self.ui.staffbtn.clicked.connect(self.open_staff)
        else:
            print("Error: 'staffbtn' not found in UI setup")
        # self.addschedbtn.clicked.connect(self.open_addsched)

    def open_staff(self):
        staff = StaffScreen(self.stacked_widget)
        self.stacked_widget.addWidget(staff)
        self.stacked_widget.setCurrentWidget(staff)

    def open_schedule(self):
        sched = ScheduleScreen(self.stacked_widget)
        self.stacked_widget.addWidget(sched)
        self.stacked_widget.setCurrentWidget(sched)

    def open_addsched(self):
        addsched = AddSchedScreen(self.stacked_widget)
        self.stacked_widget.addWidget(addsched)
        self.stacked_widget.setCurrentWidget(addsched)

class LoginScreen(QDialog):
    def __init__(self, stacked_widget):
        super(LoginScreen, self).__init__()
        self.ui = Ui_Form()  # Instantiate the UI class
        self.ui.setupUi(self)  # Set up the UI
        self.stacked_widget = stacked_widget
        self.ui.btnLogin.clicked.connect(self.loginfunction)

    def loginfunction(self):
        user = self.ui.inputEmail.text()
        password = self.ui.inputPass.text()

        cur.execute("""SELECT password FROM users WHERE username = %s""", (user,))
        result_pass = cur.fetchone()

        if len(user) == 0 and len(password) == 0:
            self.ui.error.setText('Input all field')
        else:
            if result_pass and result_pass[0] == password:
                self.open_staff()
            else:
                self.ui.error.setText('Invalid Email or Password')

    def open_schedule(self):
        sched = ScheduleScreen(self.stacked_widget)  # Pass the stacked widget instance
        self.stacked_widget.addWidget(sched)
        self.stacked_widget.setCurrentWidget(sched)
        
    def open_staff(self):
        staff = StaffScreen(self.stacked_widget)
        self.stacked_widget.addWidget(staff)
        self.stacked_widget.setCurrentWidget(staff)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = QStackedWidget()
    login = LoginScreen(widget)
    widget.addWidget(login)
    widget.show()
    sys.exit(app.exec_())
