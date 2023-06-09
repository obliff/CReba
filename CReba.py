import sys
import numpy as np
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
from formWidget import Ui_Form
from loginWidget import loginui
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QDialog,  QPushButton, QHBoxLayout, QVBoxLayout, QStyle, QSlider, QFileDialog, QScrollArea, QMessageBox
from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtCore import Qt, QUrl
import pandas as pd
import os


# Define the Table A matrix
table_A = np.array([[[1, 2, 3, 4], [2, 3, 4, 5], [2, 4, 5, 6], [3, 5, 6, 7], [4, 6, 7, 8]],
                    [[1, 2, 3, 4], [3, 4, 5, 6], [4, 5, 6, 7], [5, 6, 7, 8], [6, 7, 8, 9]],
                    [[3, 3, 5, 6], [4, 5, 6, 7], [5, 6, 7, 8], [6, 7, 8, 9], [7, 8, 9, 9]]])  
#Define the Table B Matrix
table_B = np.array([[[1, 2, 2], [1, 2, 3], [3, 4, 5], [4, 5, 5], [6, 7, 8], [7, 8, 8]],
                    [[1, 2, 3], [2, 3, 4], [4, 5, 5], [5, 6, 7], [7, 8, 8], [8, 9, 9]]])  
#Define the Table C Matrix
table_C = np.array([[1, 1, 1, 2, 3, 3, 4, 5, 6, 7, 7, 7], [1, 2, 2, 3, 4, 4, 5, 6, 6, 7, 7, 8], [2, 3, 3, 3, 4, 5, 6, 7, 7, 8, 8, 8], [3, 4 , 4, 4, 5, 6, 7, 8, 8, 9, 9, 9],
                            [4, 4, 4, 5, 6, 7, 8, 8, 9, 9, 9, 9], [6, 6, 6, 7, 8, 8, 9, 9, 10, 10, 10, 10], [7, 7, 7, 8, 9, 9, 9, 10, 10, 11, 11, 11], [8, 8, 8, 9, 10, 10, 10, 10, 10, 11, 11, 11],
                            [9, 9, 9, 10, 10, 10, 11, 11, 11, 12, 12, 12], [10, 10, 10, 11, 11, 11, 11, 12, 12, 12, 12, 12], [11, 11, 11, 11, 12, 12, 12, 12, 12, 12, 12, 12], [12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12]])

class formWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.setWindowTitle("C-REBA Calculator")
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_1)
        self.ui.prevBtn.setEnabled(False)
        self.ui.historybtn.clicked.connect(self.show_history)
        self.ui.calculatebtn.clicked.connect(self.handle_calculate_button) 
        self.ui.clearbtn.clicked.connect(self.clear_content) 
        self.ui.nextBtn.clicked.connect(self.next_page)
        self.ui.prevBtn.clicked.connect(self.previous_page)
       
        self.checkboxes = [self.ui.neck_adjbtn_1, self.ui.trunkadj_1, self.ui.forceadj_1, 
                      self.ui.upperarmadj_1, self.ui.upperarmadj_2, self.ui.upperarmadj_3, 
                      self.ui.wristadj_1, self.ui.activitybtn_1, self.ui.activitybtn_2, 
                      self.ui.activitybtn_3]
        
        self.radioboxes = [self.ui.neckbtn_1, self.ui.neckbtn_2, self.ui.neckbtn_3, self.ui.trunkbtn_1,
                      self.ui.trunkbtn_2, self.ui.trunkbtn_3, self.ui.trunkbtn_4, self.ui.trunkbtn_5,
                      self.ui.legsbtn_1, self.ui.legsbtn_2, self.ui.legsadj_1, self.ui.legsadj_2,
                      self.ui.legsadj_3, self.ui.forcebtn_1, self.ui.forcebtn_2, self.ui.forcebtn_3,
                      self.ui.upperarmbtn_1, self.ui.upperarmbtn_2, self.ui.upperarmbtn_3, self.ui.upperarmbtn_4,
                      self.ui.upperarmbtn_5, self.ui.lowerarmbtn_1, self.ui.lowerarmbtn_2, self.ui.wristbtn_1, 
                      self.ui.wristbtn_2, self.ui.couplingbtn_1, self.ui.couplingbtn_2, self.ui.couplingbtn_3,  self.ui.couplingbtn_4]
        #initilaze values for excel executions
        self.neck1=0
        self.trunk1=0
        self.leg1 = 0
        self.force1 = 0

        self.upperarm1 = 0
        self.lowerarm1 = 0
        self.wrist1 = 0
        self.coupling1 = 0


    def previous_page(self):
        current_index = self.ui.stackedWidget.currentIndex()
        if current_index > 0:
            self.ui.stackedWidget.setCurrentIndex(current_index - 1)
        self.update_button_states()
            
    def next_page(self):
        current_index = self.ui.stackedWidget.currentIndex()
        if current_index < self.ui.stackedWidget.count() - 1:
            self.ui.stackedWidget.setCurrentIndex(current_index + 1)
        self.update_button_states()
    
    def update_button_states(self):
        current_index = self.ui.stackedWidget.currentIndex()
        self.ui.prevBtn.setEnabled(current_index > 0)
        self.ui.nextBtn.setEnabled(current_index < self.ui.stackedWidget.count() - 1)
       
    def clear_content(self):
        
        for checkbox in self.checkboxes:
            checkbox.setChecked(False)

        for radiobox in self.radioboxes:
            radiobox.setAutoExclusive(False)
            radiobox.setChecked(False)
            radiobox.setAutoExclusive(True)

    def handle_calculate_button(self):
        neck_checked = self.ui.neckbtn_1.isChecked() or self.ui.neckbtn_2.isChecked() or self.ui.neckbtn_3.isChecked()
        trunk_checked = any(self.ui.__dict__[f"trunkbtn_{i}"].isChecked() for i in range(1, 6))
        legs_checked = self.ui.legsbtn_1.isChecked() or self.ui.legsbtn_2.isChecked()
        legs_adj_checked = any(self.ui.__dict__[f"legsadj_{i}"].isChecked() for i in range(1, 4))
        force_checked = any(self.ui.__dict__[f"forcebtn_{i}"].isChecked() for i in range(1, 4))
        upper_arm_checked = any(self.ui.__dict__[f"upperarmbtn_{i}"].isChecked() for i in range(1, 6))
        lower_arm_checked = self.ui.lowerarmbtn_1.isChecked() or self.ui.lowerarmbtn_2.isChecked()
        wrist_checked = self.ui.wristbtn_1.isChecked() or self.ui.wristbtn_2.isChecked()
        coupling_checked = any(self.ui.__dict__[f"couplingbtn_{i}"].isChecked() for i in range(1, 5))

        if all((neck_checked, trunk_checked, legs_checked, legs_adj_checked, force_checked, upper_arm_checked, lower_arm_checked, wrist_checked, coupling_checked)):
            self.ui.calculatebtn.setEnabled(True)
            reba_score = self.calculate_reba_score()  # calculate the REBA score
            self.display_reba_score(reba_score)  # display the REBA score
        else:
            QMessageBox.warning(self, "Calculation Failed", "Fill in all the necessary blanks on the form.")

    def calculate_reba_score(self):
        score_A = self.calculate_score_A()
        score_B = self.calculate_score_B()
        
        activity_score = 0
        if self.ui.activitybtn_1.isChecked():
            activity_score += 1
        if self.ui.activitybtn_2.isChecked():
            activity_score += 1
        if self.ui.activitybtn_3.isChecked():
            activity_score += 1

        score_C = table_C[score_A - 1 , score_B - 1]
        reba_score = score_C + activity_score    
        return reba_score
    
    def display_reba_score(self, reba_score):
        savebtn = QPushButton("Save")
        savebtn.clicked.connect(self.save_to_excel)

        if reba_score == 1:
            msgbox_1= QMessageBox(self)
            msgbox_1.setWindowTitle("Your Result")
            msgbox_1.setText(f" <i>REBA Score: {reba_score}</i>, Negligible Risk.")
            msgbox_1.setStyleSheet("""
            QMessageBox {
                background-color: #2ed92b;
                font-size: 16px;
            }
            QMessageBox QLabel {
                background-color: #2ed92b;
                color: #ffffff;
            }
            QMessageBox QPushButton {
                background-color: #ded9ee;
                padding: 5px 10px;
            }
            QMessageBox QPushButton:hover {
                background-color: #cbc1ee;
            }
        """)
            msgbox_1.addButton(QMessageBox.Ok)
            msgbox_1.addButton(savebtn, QMessageBox.AcceptRole)
            msgbox_1.exec_()
            
        if reba_score in [2,3]:
            msgbox_2 = QMessageBox(self)
            msgbox_2.setWindowTitle("Your Result")
            msgbox_2.setText(f"<i>REBA Score: {reba_score}</i>, Low Risk. Change may be needed.")
            msgbox_2.setStyleSheet("""
            QMessageBox {
                background-color: #d3d92b;
                font-size: 16px;
            }
            QMessageBox QLabel {
                background-color: #d3d92b;
                color: #ffffff;
            }
            QMessageBox QPushButton {
                background-color: #ded9ee;
                padding: 5px 10px;
            }
            QMessageBox QPushButton:hover {
                background-color: #cbc1ee;
            }

        """)
            msgbox_2.addButton(QMessageBox.Ok)
            msgbox_2.addButton(savebtn, QMessageBox.AcceptRole)
            msgbox_2.exec_()

        if reba_score in [4,5,6,7]:
            msgbox_3 = QMessageBox(self)
            msgbox_3.setWindowTitle("Your Result")
            msgbox_3.setText(f"<i>REBA Score: {reba_score}</i>, Medium Risk. Further Investigate. Change Soon.")
            msgbox_3.setStyleSheet("""
            QMessageBox {
                background-color: #d98e2b;
                font-size: 16px;
            }
            QMessageBox QLabel {
                background-color: #d98e2b;
                color: #ffffff;
            }
            QMessageBox QPushButton {
                background-color: #ded9ee;
                padding: 5px 10px;
            }
            QMessageBox QPushButton:hover {
                background-color: #cbc1ee;
            }

        """)
            msgbox_3.addButton(QMessageBox.Ok)
            msgbox_3.addButton(savebtn, QMessageBox.AcceptRole)
            msgbox_3.exec_()

        if reba_score in [8,9,10]:
            msgbox_4 = QMessageBox(self)
            msgbox_4.setWindowTitle("Your Result")
            msgbox_4.setText(f"<i>REBA Score: {reba_score}</i>, High Risk. Investigate and Implement Change.")
            msgbox_4.setStyleSheet("""
            QMessageBox {
                background-color: #d9572b;
                font-size: 16px;
            }
            QMessageBox QLabel {
                background-color: #d9572b;
                color: #ffffff;
            }
            QMessageBox QPushButton {
                background-color: #ded9ee;
                padding: 5px 10px;
            }
            QMessageBox QPushButton:hover {
                background-color: #cbc1ee;
            }

        """)
            msgbox_4.addButton(QMessageBox.Ok)
            msgbox_4.addButton(savebtn, QMessageBox.AcceptRole)
            msgbox_4.exec_()

        if reba_score in [11,12,13,14,15]:
            msgbox_5 = QMessageBox(self)
            msgbox_5.setWindowTitle("Your Result")
            msgbox_5.setText(f"<i>REBA Score: {reba_score}</i>, Very High Risk. Implement Change.")
            msgbox_5.setStyleSheet("""
            QMessageBox {
                background-color: #d92b2b;
                font-size: 16px;
            }
            QMessageBox QLabel {
                background-color: #d92b2b;
                color: #ffffff;
            }
            QMessageBox QPushButton {
                background-color: #ded9ee;
                padding: 5px 10px;
            }
            QMessageBox QPushButton:hover {
                background-color: #cbc1ee;
            }
            
        """)
            msgbox_5.addButton(QMessageBox.Ok)
            msgbox_5.addButton(savebtn, QMessageBox.AcceptRole)
            msgbox_5.exec_()
           
        
    def calculate_score_A(self):
        neck_score = 0
        if self.ui.neckbtn_1.isChecked():
            neck_score += 1
        if self.ui.neckbtn_2.isChecked():
            neck_score += 2
        if self.ui.neckbtn_3.isChecked():
            neck_score += 2

        if self.ui.neck_adjbtn_1.isChecked():
            neck_score += 1

        trunk_score = 0
        if self.ui.trunkbtn_1.isChecked():
            trunk_score += 1
        if self.ui.trunkbtn_2.isChecked():
            trunk_score += 2
        if self.ui.trunkbtn_3.isChecked():
            trunk_score += 2
        if self.ui.trunkbtn_4.isChecked():
            trunk_score += 3
        if self.ui.trunkbtn_5.isChecked():
            trunk_score += 4
        if self.ui.trunkadj_1.isChecked():
            trunk_score += 1

        leg_score = 0
        if self.ui.legsbtn_1.isChecked():
            leg_score += 1
        if self.ui.legsbtn_2.isChecked():
            leg_score += 2
        if self.ui.legsadj_1.isChecked():
            leg_score += 0
        if self.ui.legsadj_2.isChecked():
            leg_score += 1
        if self.ui.legsadj_3.isChecked():
            leg_score += 2
        
        forceload_score = 0
        if self.ui.forcebtn_1.isChecked():
            forceload_score += 0
        if self.ui.forcebtn_2.isChecked():
            forceload_score += 1
        if self.ui.forcebtn_3.isChecked():
            forceload_score += 2
        if self.ui.forceadj_1.isChecked():
            forceload_score += 1

        posture_score_A = table_A[neck_score - 1][trunk_score - 1][leg_score - 1]
        score_A = posture_score_A + forceload_score
        self.neck1=neck_score
        self.trunk1=trunk_score
        self.leg1 = leg_score
        self.force1 = forceload_score

        return score_A


    def calculate_score_B(self):
        upperarm_score = 0
        if self.ui.upperarmbtn_1.isChecked():
            upperarm_score += 1
        if self.ui.upperarmbtn_2.isChecked():
            upperarm_score += 2
        if self.ui.upperarmbtn_3.isChecked():
            upperarm_score += 2
        if self.ui.upperarmbtn_4.isChecked():
            upperarm_score += 3
        if self.ui.upperarmbtn_5.isChecked():
            upperarm_score += 4
        if self.ui.upperarmadj_1.isChecked():
            upperarm_score += 1
        if self.ui.upperarmadj_2.isChecked():
            upperarm_score += 1
        if self.ui.upperarmadj_3.isChecked():
            if upperarm_score == 1:
                upperarm_score += 0
            else:
                upperarm_score -= 1
        
        lowerarm_score = 0
        if self.ui.lowerarmbtn_1.isChecked():
            lowerarm_score += 1
        if self.ui.lowerarmbtn_2.isChecked():
            lowerarm_score += 2

        wrist_score = 0
        if self.ui.wristbtn_1.isChecked():
            wrist_score += 1
        if self.ui.wristbtn_2.isChecked():
            wrist_score += 2
        if self.ui.wristadj_1.isChecked():
            wrist_score += 1
        
        coupling_score = 0
        if self.ui.couplingbtn_1.isChecked():
            coupling_score += 0
        if self.ui.couplingbtn_2.isChecked():
            coupling_score += 1
        if self.ui.couplingbtn_3.isChecked():
            coupling_score += 2
        if self.ui.couplingbtn_4.isChecked():
            coupling_score += 3

        posture_score_B = table_B[lowerarm_score - 1][upperarm_score - 1][wrist_score - 1]
        score_B = posture_score_B + coupling_score

        self.upperarm1 = upperarm_score
        self.lowerarm1 = lowerarm_score
        self.wrist1 = wrist_score
        self.coupling1 = coupling_score

        return score_B
    
    def save_to_excel(self): 
        rebascore = self.calculate_reba_score()
        scoreA = self.calculate_score_A()
        necka = self.neck1
        trunka = self.trunk1
        lega = self.leg1
        forcea = self.force1

        scoreB =self.calculate_score_B()
        upperarmb = self.upperarm1
        lowerarmb = self.lowerarm1
        wristb = self.wrist1
        couplingb = self.coupling1

        data = {'user': 'admin', 'reba score': [rebascore], 'score A': [scoreA], 'score B': [scoreB], 
                'neck score' : [necka], 'trunk score': [trunka], 'leg score': [lega], 'force/load score': [forcea],
                'upper arm score' : [upperarmb], 'lower arm score': [lowerarmb], 'wrist score': [wristb], 'coupling score': [couplingb]}
        
        df = pd.DataFrame(data)

        filepath = 'database1.xlsx'
        try:
            existing_data = pd.read_excel(filepath)
            df = pd.concat([existing_data, df], ignore_index=True)
        except FileNotFoundError:
            pass

        df.to_excel(filepath, index=False, header=True)

    
    def show_history(self):
        history_dialog = HistoryDialog()
        history_dialog.resize(820, 320)
        history_dialog.exec_()

class HistoryDialog(QDialog):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("History")

        self.table = QTableWidget()
        self.table.setColumnCount(12)  # Assuming there are 12 columns in the Excel file
        self.table.setHorizontalHeaderLabels(['User', 'REBA Score', 'Score A', 'Score B', 'Neck', 'Trunk',
                                               'Legs', 'Force/Load', 'Upper Arm', 'Lower Arm',
                                               'Wrist', 'Coupling'])

        filepath = 'database1.xlsx'
        try:
            data = pd.read_excel(filepath)
            num_rows, num_cols = data.shape

            self.table.setRowCount(num_rows)

            for row in range(num_rows):
                for col in range(num_cols):
                    item = QTableWidgetItem(str(data.iloc[row, col]))
                    item.setFlags(item.flags() ^ Qt.ItemIsEditable)  # Make item read-only
                    self.table.setItem(row, col, item)

        except FileNotFoundError:
            pass
        
        self.setStyleSheet("background-color: rgb(213,205,238);")

        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        scroll_area.setWidget(self.table)

        self.table.setStyleSheet('''
            QTableWidget {
                background-color: rgb(222, 217, 238);
                alternate-background-color: #2d2d2d;
                color: rgb(10, 9, 13);
            }
            QHeaderView::section {
                background-color: rgb(204, 193, 238) ;
                color: rgb(10, 9, 13);
            }
            QTableWidget::item:selected {
                background-color: rgb(204, 193, 238);
            }
            QTableWidget::item:selected:!active {
                color: #ffffff;
            }
        ''')
        layout = QVBoxLayout(self)
        layout.addWidget(scroll_area)

        delete_button = QPushButton("Delete All Content")
        delete_button.setStyleSheet("QPushButton {\n"
"    background-color: #ded9ee; \n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #cbc1ee;\n"
"}")
        delete_button.clicked.connect(self.delete_content)
        layout.addWidget(delete_button)


        # Resize columns and rows to fit the available space
        header = self.table.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.Stretch)
        header = self.table.verticalHeader()
        header.setSectionResizeMode(QHeaderView.Stretch)

    def delete_content(self):
        filepath = 'database1.xlsx'
        try:
            os.remove(filepath)
            self.table.clearContents()
            self.table.setRowCount(0)
            QMessageBox.information(self, "Deletion", "Content deleted successfully.")
        except FileNotFoundError:
            pass

class MediaWindow(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowIcon(QIcon("player.ico"))
        self.setWindowTitle("Video Player")
        self.setGeometry(350,100,700,500)
        self.create_player()

    def create_player(self):
        self.mediaPlayer = QMediaPlayer(None, QMediaPlayer.VideoSurface)
        videowidget = QVideoWidget()
        self.mediaPlayer.setVideoOutput(videowidget)

        self.openBtn = QPushButton("Open File")
        self.openBtn.clicked.connect(self.open_file)
        self.openBtn.setStyleSheet("QPushButton {\n"
    "    background-color: #ded9ee; \n"
    "}\n"
    "\n"
    "QPushButton:hover {\n"
    "    background-color: #cbc1ee;\n"
    "}")

        self.playBtn = QPushButton()
        self.playBtn.setIcon(self.style().standardIcon(QStyle.SP_MediaPlay))
        self.playBtn.setEnabled(False)
        self.playBtn.clicked.connect(self.play_video)
        self.playBtn.setStyleSheet("QPushButton {\n"
    "    background-color: #ded9ee; \n"
    "}\n"
    "\n"
    "QPushButton:hover {\n"
    "    background-color: #cbc1ee;\n"
    "}")

        self.slider = QSlider(Qt.Horizontal)
        self.slider.setRange(0,0)
        self.slider.sliderMoved.connect(self.set_position)
        
        hbox = QHBoxLayout()
        hbox.setContentsMargins(0,0,0,0)

        hbox.addWidget(self.openBtn)
        hbox.addWidget(self.playBtn)
        hbox.addWidget(self.slider)

        vbox = QVBoxLayout()
        vbox.addWidget(videowidget)
        vbox.addLayout(hbox)

        self.setLayout(vbox)

        self.mediaPlayer.setVideoOutput(videowidget)
        self.mediaPlayer.stateChanged.connect(self.mediastate_changed)
        self.mediaPlayer.positionChanged.connect(self.position_changed)
        self.mediaPlayer.durationChanged.connect(self.duration_changed)
        
    def open_file(self):
        filename, _ = QFileDialog.getOpenFileName(self,"Open Video")

        if filename != '':
            self.mediaPlayer.setMedia(QMediaContent(QUrl.fromLocalFile(filename)))
            self.playBtn.setEnabled(True)
            
    def play_video(self):
        if self.mediaPlayer.state() == QMediaPlayer.PlayingState:
            self.mediaPlayer.pause()
        else:
            self.mediaPlayer.play()
    
    def mediastate_changed(self):
        if self.mediaPlayer.state() == QMediaPlayer.PlayingState:
            self.playBtn.setIcon(self.style().standardIcon(QStyle.SP_MediaPause))

        else:
            self.playBtn.setIcon(self.style().standardIcon(QStyle.SP_MediaPlay))

    def position_changed(self,position):
        self.slider.setValue(position)
    
    def duration_changed(self,duration):
        self.slider.setRange(0, duration)
    
    def set_position(self, position):
        self.mediaPlayer.setPosition(position)


class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.lgn = loginui()
        self.lgn.setupUi(self)
        
        self.lgn.password_input.setEchoMode(QLineEdit.Password)
        self.lgn.loginbtn.clicked.connect(self.check_login)


    def check_login(self):
        username = self.lgn.username_input.text()
        password = self.lgn.password_input.text()
        

        if username == "admin" and password == "admin":
            self.hide()
            self.main_window = MainWindow()
            self.main_window.show()
        else:
            QMessageBox.warning(self, "Login Failed", "Incorrect username or password.")

        
        return username


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("C-REBA Calculator")
        self.setStyleSheet("background-color: rgb(249, 246, 255);")

        self.resize(1000, 400)
        
        self.form_window = formWindow()
        self.media_widget = MediaWindow()

        main_widget = QWidget()
        self.setCentralWidget(main_widget)

        hbox = QHBoxLayout(main_widget)

        splitter = QSplitter()
        splitter.addWidget(self.form_window)
        splitter.addWidget(self.media_widget)

        hbox.addWidget(splitter)

        splitter.setStretchFactor(0, 2)
        splitter.setStretchFactor(1, 1)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    lgn_ex = LoginWindow()
    lgn_ex.show()
    sys.exit(app.exec_())