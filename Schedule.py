import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget, QFileDialog
import pandas as pd
import annealSchedule

from annealSchedule import Employee

class ScheduleApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('Employee Schedule')
        self.setGeometry(200, 200, 1000, 800)  # Adjust size and position

        # Main layout
        layout = QVBoxLayout()

        # Button for uploading Excel files
        self.uploadButton = QPushButton('Upload Excel File', self)
        self.uploadButton.clicked.connect(self.uploadFile)
        layout.addWidget(self.uploadButton)  # Add button before the table

        # Table widget
        self.table = QTableWidget(self)
        self.initializeTable()
        layout.addWidget(self.table)  # Add table after the button

        # Set the layout
        centralWidget = QWidget()
        centralWidget.setLayout(layout)
        self.setCentralWidget(centralWidget)






    def initializeTable(self):
        # Example names and days
        names = ['Example']
        days = ['Mon', 'Tues', 'Wed', 'Thurs', 'Fri', 'Sat', 'Sun']

        self.table.setColumnCount(len(days) + 3)  # Days + Extra Columns
        self.table.setRowCount(len(names))

        # Set headers
        self.table.setHorizontalHeaderLabels(['Name'] + days + ['Scheduled Hours'] + ['Required Hours'])
        self.table.setVerticalHeaderLabels([''] * len(names))

        # Populate names
        for i, name in enumerate(names):
            self.table.setItem(i, 0, QTableWidgetItem(name))


    def uploadFile(self):
        days = ['Mon', 'Tues', 'Wed', 'Thurs', 'Fri', 'Sat', 'Sun']
        # Function to handle file upload (not fully implemented)
        options = QFileDialog.Options()
        fileName, _ = QFileDialog.getOpenFileName(self, "QFileDialog.getOpenFileName()", "", "Excel Files (*.xlsx);;All Files (*)", options=options)
        if fileName:
            print("File selected:", fileName)
            # Add logic to handle the Excel file and update the table
            optimalSchedule, optimalCost, costs, employees = self.parseFile(fileName)

            if len(employees.keys()) >0:
                self.table.setRowCount(len(employees))
                self.table.setVerticalHeaderLabels([''] * len(employees.keys()))

                rows = {}
                for i, employeeName in enumerate(employees.keys()):
                    self.table.setItem(i,0,QTableWidgetItem(employeeName))
                    rows[employeeName] = i
                
                for day, shifts in optimalSchedule.items():
                    for shift in shifts:
                        time, name, type = shift
                        self.table.setItem(rows[name],days.index(day)+1, QTableWidgetItem("{} (Type: {})".format(time,type)))
                       
                for name, index in rows.items():
                    self.table.setItem(index, 8, QTableWidgetItem(str(employees[name].getHoursScheduled())))
                    self.table.setItem(index, 9, QTableWidgetItem(str(employees[name].getRequiredHours())))
                    
                self.table.resizeColumnsToContents()

            print(optimalCost)

  

    def parseFile(self, fileName):
        # Parses a specific excel file template and returns an optimal schedule, cost, a list of costs by each iteration, and a list of employee objects

        dfAvailability = pd.read_excel(fileName).iloc[:,1:11] # splice the data frame to include just the columns for availability
        dfShifts = pd.read_excel(fileName).iloc[:,13:17] # get columns for shifts
        dfManualShifts = pd.read_excel(fileName).iloc[:,18:24] # get columns for manual shifts

        days = ["Mon","Tues","Wed","Thurs","Fri","Sat","Sun"]
        employees = {}
        for index, row in dfAvailability.iterrows():
            if pd.isna(row['Employee Name']):
                break

            employeeName = row['Employee Name']
            hours = float(row['Required Hours'])
            trainedShifts = row['Trained Shifts'].split(", ")

            availability = {}
            for day in  days:
                if not pd.isna(row[day]):
                    availability[day] = []
                    availability[day].append(row[day])
            
            employees[employeeName]= {"hours" : hours, "trained" : trainedShifts, "availability" : availability}

        shifts = {day: [] for day in days}
        for index, row in dfShifts.iterrows():
            if pd.isna(row['Day']):
                    break
            day = row["Day"]
            startTime = row["Start Time"].strftime("%H:%M")
            endTime = row["End Time"].strftime("%H:%M")
            if pd.isna(row['Shift Type']):
                shiftType = None
            else:
                shiftType = row["Shift Type"]
            
            shifts[day].append((startTime, endTime, shiftType))
        
        manualShifts = {day: {} for day in days}
        for index,row in dfManualShifts.iterrows():
                if pd.isna(row['Employee Name.1']):
                    break
                day = row['Day.1']
                employeeName = row['Employee Name.1']
                startTime = row['Start Time.1'].strftime("%H:%M")
                endTime = row['End Time.1'].strftime("%H:%M")
                if pd.isna(row['Shift Type.1']):
                    shiftType = None
                else:
                    shiftType = row['Shift Type.1']
                manualShifts[day][employeeName] = (startTime,endTime,shiftType)
        
        optimal_schedule, optimal_cost, costs, new_employees = annealSchedule.mainProcess(employees, shifts, manualShifts)

        return optimal_schedule, optimal_cost, costs, new_employees


def main():
    app = QApplication(sys.argv)
    ex = ScheduleApp()
    ex.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
