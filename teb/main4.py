import sys
from PyQt6.QtGui import QResizeEvent
from PyQt6.QtWidgets import QApplication,QFrame, QWidget, QGridLayout, QLabel, QLineEdit, QPushButton, QVBoxLayout, QDialog, QHBoxLayout, QMessageBox,QScrollArea
from PyQt6.QtCore import Qt, QThread, pyqtSignal
import time

emp = [
    {"name": "Juan", "timer": 1, "status": None},
    {"name": "Jack", "timer": 0, "status": None},
    {"name": "Joe", "timer": 0, "status": None},
    {"name": "James", "timer": 0, "status": None},
    {"name": "Emily", "timer": 0, "status": None},
    {"name": "John", "timer": 0, "status": None},
    {"name": "Emma", "timer": 10, "status": None},
    {"name": "Jacob", "timer": 0, "status": None},
    {"name": "Sophia", "timer": 0, "status": None},
    {"name": "Michael", "timer": 0, "status": None},
    {"name": "Cortes", "timer": 0, "status": None}
]

# Add id to each dictionary
for i, employee in enumerate(emp, start=1):
    employee["id"] = i

empF = []

class TimerThread(QThread):
    timer_updated = pyqtSignal(int)

    def __init__(self, emp_timer=0, parent=None):
        super().__init__(parent)
        self.running = False
        self.paused = False
        self.timer = emp_timer  # Initialize the timer with emp_timer value

    def run(self):
        print("Timer thread started!")
        while True:
            if self.running and not self.paused:
                self.timer += 1
                print("Timer value:", self.timer)
                self.timer_updated.emit(self.timer)
            time.sleep(1)

    def start_timer(self):
        self.running = True

    def pause_timer(self):
        self.paused = True

    def resume_timer(self):
        self.paused = False


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.timers = {}  # Dictionary to store timers for each employee
        for employee in emp:
            if employee["timer"] != 0:
                timer_thread = TimerThread(emp_timer=employee["timer"])  # Pass the initial timer value
                print(f"Creating timer thread for employee {employee['name']} with timer value {employee['timer']}")
                timer_thread.timer_updated.connect(lambda seconds, id=employee["id"]: self.update_timer_label(seconds, id))
                self.timers[employee["id"]] = timer_thread
                timer_thread.start()  # Start the timer thread immediately
                timer_thread.start_timer()
    def initUI(self):
        self.setWindowTitle('Main Window')
        self.setGeometry(720, 30, 0, 0)
        self.setMinimumSize(720,720)
        self.setStyleSheet("background-color:black;")
        
        # Create grid layout
        grid_layout = QGridLayout()
        grid_layout.setSpacing(0)  # Set spacing between widgets to 0
        grid_layout.setContentsMargins(0, 0, 0, 0)  # Set margins to 0

        self.frame1 = QFrame(self)
        self.frame3 = QFrame(self)
        self.back_button = QPushButton("Back",self.frame3)
        self.back_button.setStyleSheet("background-color:red; border: 2px solid red; border-radius: 10px;")
        self.back_button.hide()
        self.frame4 = QFrame(self)
        self.frame4.setStyleSheet("background-color:pink;")
       
        self.start_button = QPushButton("Start", self.frame4)
        self.pause_button = QPushButton("Pause", self.frame4)
        self.resume_button = QPushButton("Resume", self.frame4)
        self.frame4.hide()
        self.empScrollArea = QScrollArea(self)
        self.frame2 = QFrame()
        self.empLayout = QVBoxLayout(self.frame2)
        self.empScrollArea.setWidgetResizable(True)
        self.empScrollArea.setWidget(self.frame2)

        label1 = QLabel("INSURGENT",self.frame3)
        frame3_layout = QVBoxLayout(self.frame3)
        frame3_layout.addWidget(label1, alignment=Qt.AlignmentFlag.AlignCenter)
        self.frame3.setLayout(frame3_layout)
        self.frame3.setStyleSheet("background-color:black;")
        self.frame2.setStyleSheet("background-color:red;")
        self.frame1.setStyleSheet("background-color:blue;")

        grid_layout.addWidget(self.frame3, 0, 0, 1, 2)  # Span frame3 across two columns
        grid_layout.addWidget(self.frame1, 1, 0)
        grid_layout.addWidget(self.empScrollArea, 1, 1)
        grid_layout.addWidget(self.frame4,1,1)
        
        self.setLayout(grid_layout)
        self.setFrame2()

    def back_clicked(self):
        self.frame4.hide()
        self.empScrollArea.show()
        self.back_button.hide()
    
    def resizeEvent(self,event):
        global empF

        frame1W = int(self.width()*.20)
        self.frame1.setFixedWidth(frame1W)
        self.frame3.setFixedWidth(int(self.width()*1))
        self.frame3.setFixedHeight(int(self.height()*.20))
        self.back_button.setGeometry(int(self.frame3.width()*.80),int(self.frame3.height()*.10),int(self.frame3.width()*.15),int(self.frame3.height()*.30))
        self.empScrollArea.setGeometry(0,0,int(self.width()),int(self.height()))
        total_height = (len(empF)+2) * int(self.empScrollArea.height() * 0.10)

        self.frame2.setMinimumHeight(total_height)
        y = 0.
        for a in range(len(empF)):
            empF[a].setGeometry(int(self.empScrollArea.width()*.10),int(self.empScrollArea.height()* y),int(self.empScrollArea.width()*.60),int(self.empScrollArea.height()*.10))
            y += .11
            
    def setFrame2(self):
        global emp, empF
        for a in emp:
            empFrame = QFrame(self.frame2)
            label = QLabel(a["name"], empFrame)
            hover_style = """
                QFrame:hover {
                    background-color: purple;
                    border-color: purple;
                }
            """
            empFrame.setStyleSheet("background-color: violet; border: 2px solid violet; border-radius: 10px;") 
            empF.append(empFrame)
            empFrame.mousePressEvent = lambda event, name=a["id"]: self.on_empFrame_clicked(name)

        self.timer_labels = {}  # Dictionary to store timer labels for each employee
        # Create timer labels for each employee
        for employee in emp:
            timer_label = QLabel("00:00:00", self.frame4)
            self.timer_labels[employee["id"]] = timer_label
            timer_label.hide()

        # Create start, pause, and resume buttons
        # self.start_button = QPushButton("Start", self.frame4)
        # self.pause_button = QPushButton("Pause", self.frame4)
        # self.resume_button = QPushButton("Resume", self.frame4)
        self.start_button.move(20, 100)
        self.pause_button.move(100, 100)
        self.resume_button.move(180, 100)
        # Connect buttons to functions
        self.start_button.clicked.connect(self.start_button_clicked)
        self.pause_button.clicked.connect(self.pause_button_clicked)
        self.resume_button.clicked.connect(self.resume_button_clicked)

    def back_clicked(self):
        self.frame4.hide()
        self.empScrollArea.show()
        self.back_button.hide()
        self.hide_timer_labels()

    def start_button_clicked(self):
        # Retrieve the employee id of the clicked frame
        id = self.current_emp_id

        # Check if the timer thread exists for the current employee
        if id in self.timers:
            timer_thread = self.timers[id]
            if not timer_thread.running:
                # Check if there's a non-zero timer value for the current employee
                for employee in emp:
                    if employee["id"] == id and employee["timer"] != 0:
                        timer_thread.timer = employee["timer"]
                        break
                timer_thread.start_timer()

    def pause_button_clicked(self):
        # Retrieve the employee id of the clicked frame
        id = self.current_emp_id

        # Check if the timer thread exists for the current employee
        if id in self.timers:
            timer_thread = self.timers[id]
            if timer_thread.running:
                timer_thread.pause_timer()

    def resume_button_clicked(self):
        # Retrieve the employee id of the clicked frame
        id = self.current_emp_id

        # Check if the timer thread exists for the current employee
        if id in self.timers:
            timer_thread = self.timers[id]
            if timer_thread.paused:
                timer_thread.resume_timer()

    def hide_timer_labels(self):
        for label in self.timer_labels.values():
            label.hide()

    def show_timer_label(self, id):
        if id in self.timer_labels:
            self.timer_labels[id].show()

    def on_empFrame_clicked(self, id):
        global emp
        self.current_emp_id = id
        self.empScrollArea.hide()
        self.frame4.show()
        self.back_button.show()
        self.back_button.clicked.connect(self.back_clicked)

        # Find the employee corresponding to the clicked id
        emp_info = next(emp_info for emp_info in emp if emp_info["id"] == id)

        # Show employee name in the frame4
        emp_name_label = QLabel(f"Employee Name: {emp_info['name']}", self.frame4)
        emp_name_label.move(20, 20)

        # Hide all existing timer labels
        self.hide_timer_labels()

        # Show the timer label for the clicked employee
        self.show_timer_label(id)

        # Create timer thread if it doesn't exist
        if id not in self.timers:
            timer_thread = TimerThread()
            timer_thread.timer_updated.connect(lambda seconds, id=id: self.update_timer_label(seconds, id))
            self.timers[id] = timer_thread

            # Create start, pause, and resume buttons
            self.start_button.move(20, 100)
            self.pause_button.move(100, 100)
            self.resume_button.move(180, 100)

            # Connect buttons to functions
            self.start_button.clicked.connect(lambda: self.start_button_clicked())
            self.pause_button.clicked.connect(lambda: self.pause_button_clicked())
            self.resume_button.clicked.connect(lambda: self.resume_button_clicked())

            timer_thread.start()

    def update_timer_label(self, seconds, id):
        print("Updating timer label...")
        hours = seconds // 3600
        minutes = (seconds % 3600) // 60
        seconds = seconds % 60
        timer_string = f"{hours:02d}:{minutes:02d}:{seconds:02d}"
        self.timer_labels[id].setText(timer_string)

        # Update the corresponding dictionary in emp list
        for employee in emp:
            if employee["id"] == id:
                employee["timer"] = seconds
                break
        print(emp)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
