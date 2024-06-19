import sys
import psycopg2
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QDialog, QMainWindow, QApplication, QStackedWidget, QGridLayout, QFrame, QLabel, QWidget, QMessageBox
from PyQt5.QtCore import QDate, Qt
from ui_addscheduledialog import AddScheduleDialog
from ui_addstaff import AddStaffDialog
from ui_deletescheduledialog import DeleteSchedDialog
from ui_deletestaffdialog import DeleteStaffDialog
from ui_editscheduledialog import EditSchedDialog
from ui_login import Ui_Form
from ui_staff import StaffTab
from ui_schedule1 import ScheduleTab
from ui_addschedule import AddStaffSchedule
from ui_updatestaff import UpdateStaffDialog
from wesdw import widgets  # Ensure this imports the correct widget class

# Database connection setup
conn = psycopg2.connect(host='localhost', dbname='insurgent_db', user='postgres', password='admin', port='5432')
cur = conn.cursor()



class StaffScreen(QMainWindow):
    def __init__(self, stacked_widget):
        super(StaffScreen, self).__init__()
        self.ui = StaffTab()
        self.ui.setupUi(self)
        self.stacked_widget = stacked_widget
        self.ui.schedbtn.clicked.connect(self.open_schedule)
        self.ui.updatestaffbtn.clicked.connect(self.open_update_staff_dialog)
        self.ui.deletestaffbtn.clicked.connect(self.open_delete_staff_dialog)
        self.ui.addstaffbtn.clicked.connect(self.open_add_staff_dialog)
        
        # Initialize the delete staff dialog
        self.delete_staff_dialog = None
        self.update_staff_dialog = None
        self.add_staff_dialog = None
        
    def open_schedule(self):
        sched = ScheduleScreen(self.stacked_widget)
        self.stacked_widget.addWidget(sched)
        self.stacked_widget.setCurrentWidget(sched)
        
    def open_add_staff_dialog(self):
        if self.add_staff_dialog is None:
            # Create an instance of the add staff dialog
            self.add_staff_dialog = QDialog()
            self.add_ui = AddStaffDialog()
            self.add_ui.setupUi(self.add_staff_dialog)
            self.add_ui.staff_add.connect(self.ui.load_data)


        # Show the dialog
        self.add_staff_dialog.exec()
        
    def open_delete_staff_dialog(self):
        selected_row = self.ui.tableWidget.currentRow()
        if selected_row != -1:
            staff_id = self.ui.tableWidget.item(selected_row, 0).text()  # Assuming ID is in the first column
            first_name = self.ui.tableWidget.item(selected_row, 1).text()
            last_name = self.ui.tableWidget.item(selected_row, 2).text()
            
            # Create the delete staff dialog if it doesn't already exist
            if self.delete_staff_dialog is None:
                self.delete_staff_dialog = QDialog()
                self.delete_ui = DeleteStaffDialog(self.delete_staff_dialog)
                self.delete_ui.setupUi(self.delete_staff_dialog)
                self.delete_ui.staff_deleted.connect(self.ui.load_data)  # Connect the signal to the slot

            # Update dialog text and show it
            self.delete_ui.label.setText(f"Are you sure you want to delete {first_name} {last_name}?")
            self.delete_ui.emp_id.setText(staff_id)
            self.delete_staff_dialog.exec_()
    
    def open_update_staff_dialog(self):
        # Get the selected staff's information from the table
        selected_row = self.ui.tableWidget.currentRow()
        if selected_row != -1:  # Ensure a row is selected
            staff_id = self.ui.tableWidget.item(selected_row, 0).text()  # Assuming ID is in the first column
            first_name = self.ui.tableWidget.item(selected_row, 1).text()
            last_name = self.ui.tableWidget.item(selected_row, 2).text()
            address = self.ui.tableWidget.item(selected_row, 3).text()
            hire_date = self.ui.tableWidget.item(selected_row, 4).text()
            phone = self.ui.tableWidget.item(selected_row, 5).text()
            email = self.ui.tableWidget.item(selected_row, 6).text()
            emp_pin = self.ui.tableWidget.item(selected_row, 7).text()

            # Create an instance of the update staff dialog
            if self.delete_staff_dialog is None:
                self.update_staff_dialog = QDialog()
                self.update_ui = UpdateStaffDialog(staff_id, self.update_staff_dialog)
                self.update_ui.setupUi(self.update_staff_dialog)
                self.update_ui.staff_updated.connect(self.ui.load_data)

            # Set the staff's information in the update staff dialog
            self.update_ui.fnameinput.setText(first_name)
            self.update_ui.lnameinput.setText(last_name)
            self.update_ui.addressinput.setText(address)
            self.update_ui.phoneinput.setText(phone)
            self.update_ui.emailinput.setText(email)
            self.update_ui.pinlabel.setText(emp_pin)
            self.update_ui.hdinput.setDate(QDate.fromString(hire_date, "yyyy-MM-dd"))

            # Connect any signals or slots as needed

            # Show the dialog
            self.update_staff_dialog.exec_()
            
class AddScheduleScreen(QMainWindow):
    def __init__(self, stacked_widget, date):
        
        super(AddScheduleScreen, self).__init__()
        self.date = date
        self.stacked_widget = stacked_widget
        previous_index = self.stacked_widget.currentIndex()
        self.ui = AddStaffSchedule(self.stacked_widget, self.date, previous_index)
        self.ui.setupUi(self)  # Set up the UI
        self.stacked_widget = stacked_widget
        self.ui.updateschedbtn.clicked.connect(self.open_edit_sched)
        self.ui.addstaffbtn.clicked.connect(self.open_add_schedule)
        self.ui.deletestaffbtn.clicked.connect(self.open_delete_sched)
        
        self.update_schedule_dialog = None
        self.add_schedule_dialog = None
        self.delete_schedule_dialog = None
        
        
    def open_add_schedule(self):
        
        selected_row = self.ui.tableWidget.currentRow()
        if selected_row != -1:  # Ensure a row is selected
            staff_id = self.ui.tableWidget.item(selected_row, 0).text()  # Assuming ID is in the first column
            first_name = self.ui.tableWidget.item(selected_row, 1).text()
            last_name = self.ui.tableWidget.item(selected_row, 2).text()
            
            if self.add_schedule_dialog is None:
                # Create an instance of the add staff dialog
                self.add_schedule_dialog = QDialog()
                self.add_ui = AddScheduleDialog(self.add_schedule_dialog)
                self.add_ui.setupUi(self.add_schedule_dialog)
                self.add_ui.sched_add.connect(self.ui.load_data)
                
                
            self.add_ui.emp_id.setText(staff_id)
            self.add_ui.dateinput.setText(self.date)
            self.add_ui.nameinput.setText(f"{first_name} {last_name}")

            # Show the dialog
            self.add_schedule_dialog.show()
        
        
    def open_edit_sched(self):
        selected_row = self.ui.tableWidget.currentRow()
        if selected_row != -1:  # Ensure a row is selected
            staff_id = self.ui.tableWidget.item(selected_row, 0).text()  # Assuming ID is in the first column
            first_name = self.ui.tableWidget.item(selected_row, 1).text()
            last_name = self.ui.tableWidget.item(selected_row, 2).text()
            start_time = self.ui.tableWidget.item(selected_row, 3).text()
            end_time = self.ui.tableWidget.item(selected_row, 4).text()
            status = self.ui.tableWidget.item(selected_row, 5).text()

            if self.update_schedule_dialog is None:
                self.update_sched_dialog = QDialog()
                self.update_ui = EditSchedDialog(staff_id, self.update_sched_dialog, self.date)
                self.update_ui.setupUi(self.update_sched_dialog)
                self.update_ui.sched_update.connect(self.ui.load_data)

            self.update_ui.emp_id.setText(str(staff_id))
            self.update_ui.dateinput.setText(self.date)
            self.update_ui.nameinput.setText(f"{first_name} {last_name}")
            self.update_ui.frominput.setCurrentText(start_time)
            self.update_ui.toinput.setCurrentText(end_time)
            self.update_ui.comboBox.setCurrentText(status)

            self.update_sched_dialog.exec()
            
    def open_delete_sched(self):
        selected_row = self.ui.tableWidget.currentRow()
        if selected_row != -1:  # Ensure a row is selected
            sched_id = self.ui.tableWidget.item(selected_row, 6).text()
            if self.delete_schedule_dialog is None:
                self.delete_sched_dialog = QDialog()
                self.delete_ui = DeleteSchedDialog(self.delete_sched_dialog)
                self.delete_ui.setupUi(self.delete_sched_dialog)
                self.delete_ui.delete_update.connect(self.ui.load_data)
            self.delete_ui.sched_id.setText(sched_id)
            
            self.delete_sched_dialog.exec()
            

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
            
        self.ui.calendarWidget.selectionChanged.connect(self.ui.printSelectedDate)
        self.ui.addschedbtn.clicked.connect(self.open_addsched)


    def open_staff(self):
        staff = StaffScreen(self.stacked_widget)
        self.stacked_widget.addWidget(staff)
        self.stacked_widget.setCurrentWidget(staff)

    def open_schedule(self):
        sched = ScheduleScreen(self.stacked_widget)
        self.stacked_widget.addWidget(sched)
        self.stacked_widget.setCurrentWidget(sched)

    def open_addsched(self):
        date = self.ui.selected_date
        addsched = AddScheduleScreen(self.stacked_widget, date)
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
