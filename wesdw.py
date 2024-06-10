from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QFrame, QWidget, QLabel, QScrollArea, QVBoxLayout, QDialog
from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5 import QtGui
import sys

first = [1, 2, 0, 1, 1, 2, 0, 1, 1,2,1,1,0]
last = [7, 5, 4, 9, 12, 5, 0, 9, 12,9,2,12,12]
name = ['Juan Juan', "Jack Jack", "Joe Joe", "Jeff Jeff", "James James", "Jeff Jeff", "James James", "Jeff Jeff",
        "James James","BATO","asda","Motherfucker","Kenneth Cortes"]
yes1 = []
yes2 = []


redframes = []  # List to store ClickableFrame instances
redframesx = []
v = .05
count = 0
timelabels = []
guidelines = []
namez = []
labelz = []
guide = []
content_height = 0

class ClickableFrame(QFrame):
    doubleClicked = pyqtSignal()  # Define doubleClicked signal using pyqtSignal

    def mouseDoubleClickEvent(self, event):
        self.doubleClicked.emit()
class widgets(QFrame):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.schedScrollArea = QScrollArea(self)
        self.schedScrollArea.setGeometry(0, int(self.height() * .05), int(self.width() * .99), int(self.height() * .95))

        self.schedFrame = QFrame()
        self.schedLayout = QVBoxLayout(self.schedFrame)
        self.schedScrollArea.setWidgetResizable(True)
        self.schedScrollArea.setWidget(self.schedFrame)

        self.time = QFrame(self)
        self.time.setGeometry(int(self.width() * .9), 0, int(self.width() * .99), int(self.height() * .05))
        self.time.setStyleSheet("background-color: red")

        x = 15
        gx =0
        for a in range(10, 23):
            if a <= 12:
                tme = str(a) + " am"
            else:
                tme = str(a - 12) + " pm"
            timelabel = QLabel(tme, self.time)
            timelabel.setGeometry(x, 12, 62, 25)
            timelabels.append(timelabel)
            guideline = QFrame(self.time)
            guideline.setGeometry(gx+61,0,3,50)
            guideline.setStyleSheet("background-color:black;")
            guidelines.append(guideline)
            x += 61
            gx += 61
        self.name()

        
        
    def sched(self):
        global first, last, v, count, name,redframes,redframesx,guide,yes1,yes2,content_height
        count2 = 0
        content_height = 0
        redframes = [] 

        
        gx = 0.06
        for a in range(13):
            guideline2 = QFrame(self.schedFrame)
            guideline2.setGeometry(int((self.schedScrollArea.width()*gx)+(self.schedScrollArea.width()*.20)), 0, int(self.schedScrollArea.width()*.005), int(self.schedScrollArea.height()*.99))
            guideline2.setStyleSheet("background-color: black")
            guide.append(guideline2)
            gx += 0.06

        
        for a in first:
            if a != 0 or last[count] != 0:
                
                redframe = ClickableFrame(self.schedFrame)
                
                redframe.setStyleSheet("background-color: maroon;")
                redframe.setObjectName("redframe")  # Set object name for identification

                label = QLabel("Schedule", redframe)
                label.setGeometry(10, 10, 150, 30)

                # Connect the doubleClicked signal of redframe to open_dialog method with name[count] as argument
                yes1.append(a)
                yes2.append(last[count])
                redframes.append(redframe)  # Add redframe to the list
                namez = name[count]
                redframes[count2].doubleClicked.connect(lambda name=namez: self.open_dialog(name))
                count2 += 1
            else:
                redframex = QFrame(self.schedFrame)
               
                redframex.setStyleSheet("background-color: grey;")

                label = QLabel("Schedule", redframe)
                label.setGeometry(10, 10, 150, 30)

                redframesx.append(redframex)

            v += 100
            count += 1
            content_height += 100
        self.schedFrame.setMinimumHeight(content_height)

    def name(self):
        global name,namez,labelz
        v = 0
        namez = []
        labelz = []

        for i in reversed(range(self.schedFrame.layout().count())):
            item = self.schedFrame.layout().itemAt(i)
            item.widget().setParent(None)
            del item
      
        for a in name:
            names = QFrame(self.schedFrame)
            label = QLabel(a, names)
            names.setGeometry(0, int(self.height()*v), int(self.width()*.20), int(self.width()*.10))
            # names.setStyleSheet("background-color: maroon;")
            names.setStyleSheet("""
            background-color: maroon;
            border: 5px solid #000000;  /* Black border of 2 pixels */
            border-radius: 10px;  /* Optional: rounded corners */
        """)
            label.setStyleSheet("border: none;")
            label.setGeometry( int(names.width()*.20), 20, 180, 25)
            
            names.setLineWidth(2)
            font = QtGui.QFont()
            font.setPointSize(20)  # Change 12 to your desired font size
            label.setFont(font)
            namez.append(names)
            labelz.append(label)
            v += 9.9
        self.sched()

    def resizeEvent(self, event):
        global timelabels,guidelines,name,namez,labelz,guide,v,first,last,redframesx,yes1,yes2,content_height
        count =0
        g = 0.06
        x = .02
        self.time.setGeometry(0, 0,int(self.width()*1) , int(self.height()*.05))
        self.schedScrollArea.setGeometry(0, int(self.height()*.04), int(self.width()*1), int(self.height()*.95))
        for a in range(13):
            guidelines[a].setGeometry(((int(self.time.width()*g)+int(self.time.width()*.2))+2),0 , int(self.time.width()*.007), int(self.time.height()))
            timelabels[a].setGeometry(((int(self.time.width()*x)+int(self.time.width()*.2))),0 , int(self.time.width()*.99), int(self.time.height()))
            
            g+= 0.06
            x += .06
        v = .01
        
        for a in range(len(name)):
            namez[a].setGeometry(0, int(self.schedScrollArea.height()*v), int(self.schedScrollArea.width()*.20), int(self.schedScrollArea.height()*.20))
            labelz[a].setGeometry( int(namez[a].width()*.20), 20, 180, 25)
            # namez[a].hide()
        
            v += .202

        v = 0.05
        count = 0
        count2 = 0
        
        for a in first:
            if a != 0 or last[count] != 0:
                redframes[count].setGeometry((int(self.schedScrollArea.width()*.201) + ( int((self.schedScrollArea.width())*.06)*yes1[count])), 
                                         (int(self.schedScrollArea.height()*v)),
                                         int(((self.schedScrollArea.width())*.0605)*yes2[count]), 
                                         int(self.schedScrollArea.height()*.10))
                
                count += 1

            else:
                redframesx[count2].setGeometry(int(self.schedScrollArea.width()*.201), 
                                               (int(self.schedScrollArea.height()*v)),
                                                int((self.schedScrollArea.width())), 
                                                int(self.schedScrollArea.height()*.10))
                
                count2 += 1 
               

            #     redframes[count].setGeometry(int(self.schedScrollArea.width()*.201), (int(self.schedScrollArea.height()*v)), 61 * int(self.schedScrollArea.width()*.6), int(self.schedScrollArea.width()*.10))
            

                #label.setGeometry(10, 10, 150, 30)

            v += 0.20
            content_height += v
        self.schedFrame.setMinimumHeight(int(self.schedScrollArea.height()*(.205*len(name))))

        gx = 0.06
        for a in range(13):
            guide[a].setGeometry(int((self.schedScrollArea.width()*gx)+(self.schedScrollArea.width()*.201)), 0, int(self.schedScrollArea.width()*.005), int(self.schedFrame.height()*1))
            gx += 0.06

        
        # for a in redframesx:
        #     redframesx[count].setGeometry(int(self.schedScrollArea.width()*.201), 
        #                                   (int(self.schedScrollArea.height()*v)),
        #                                     13 * int(self.schedScrollArea.width()*.06), 
        #                                   int(self.schedScrollArea.width()*.10))
        #     v += 0.10
           
        #     count += 1

        # self.label.setText(str(self.height())+
        #                    str(self.width()))
        # self.label.setGeometry(int(self.width() * 0.21), int(self.height() * 0.21),
        #                         int(self.width() * 0.58), int(self.height() * 0.58))
        # print(int(self.width()), int(self.height()),
        #                         int(self.width() ), int(self.height() ))
        # # self.repaint()

    def open_dialog(self, name):
        dialog = QDialog(self)
        dialog.setWindowTitle("Dialog")
        label = QLabel(f"Name: {name}", dialog)
        label.move(20, 20)
        dialog.exec()

