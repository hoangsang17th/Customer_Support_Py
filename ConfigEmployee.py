# coding=utf-8
import sys
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from module import Database, TableModel


class MyWindow(QtWidgets.QDialog):
    f_employeeId = 0

    def __init__(self):
        # Load UI
        super(MyWindow, self).__init__()
        uic.loadUi('UIs/ConfigEmployee.ui', self)
        # Load button event
        self.Database = Database
        self.pushButton_Insert.clicked.connect(self.insert)
        self.pushButton_Update.clicked.connect(self.update)
        self.pushButton_Delete.clicked.connect(self.delete)
        self.pushButton_Clear.clicked.connect(self.clear)

        # Load table list employee
        self.tableView_employeeList.setShowGrid(False)
        self.loadtableView_EmployeeList()
        self.tableView_employeeList.resizeColumnsToContents()
        self.tableView_employeeList.horizontalHeader().setStretchLastSection(True)
        self.tableView_employeeList.clicked.connect(self.rowClick)
        self.tableView_employeeList.setSelectionBehavior(1)
        self.tableView_employeeList.sortByColumn(0, QtCore.Qt.AscendingOrder)
        self.tableView_employeeList.setSortingEnabled(True)

        # Build form
        self.exec_()

    def loadtableView_EmployeeList(self):
        header = ['Employee ID', 'Employee Name', 'Email', 'Date']
        model = TableModel.TableModel(self, header, self.employee_GetList())
        self.tableView_employeeList.setModel(model)

    def rowClick(self):
        try:
            for index in self.tableView_employeeList.selectedIndexes():
                data = index.data()
                if index.column() == 0:
                    self.f_employeeId = data
                elif index.column() == 1:
                    self.lineEdit_EmployeeName.setText(data)
                elif index.column() == 2:
                    self.lineEdit_Email.setText(data)
        except Exception as e:
            QtWidgets.QMessageBox.critical(None, 'Error', str(e))

    def employee_GetList(self):
        rows = self.Database.GetEmployees()
        data = []
        for row in rows:
            try:
                data.append([str(i) for i in row])
            except Exception as e:
                QtWidgets.QMessageBox.critical(None, 'Error', str(e))
        return data

    def captureCAM(self):
        pass

    def insert(self):
        employeeName = str(self.lineEdit_EmployeeName.text())
        email = str(self.lineEdit_Email.text())
        if (employeeName == '' or email == ''):
            QtWidgets.QMessageBox.critical(
                None, 'Error', 'Not enough inputed (*) value')
            return

        result = self.Database.CreateEmployee(employeeName, email)
        if result:
            QtWidgets.QMessageBox.information(
                None, 'Susscess', 'Action susscess')
            self.loadtableView_EmployeeList()
            self.clear()
        else:
            QtWidgets.QMessageBox.critical(
                None, 'Error', "Kh??ng t???o ???????c nh??n vi??n n??y :))")
            return

    def update(self):
        employeeId = self.f_employeeId
        employeeName = str(self.lineEdit_EmployeeName.text())
        email = str(self.lineEdit_Email.text())
        if employeeId == 0 or employeeName == '' or email == '':
            QtWidgets.QMessageBox.critical(
                None, 'Error', 'Not enough inputed (*) value')
            return

        result = self.Database.UpdateEmployee(employeeId, employeeName, email)
        if result:
            QtWidgets.QMessageBox.information(
                None, 'Susscess', 'Action susscess')
            self.loadtableView_EmployeeList()
        else:
            QtWidgets.QMessageBox.critical(None, 'Error', "C???p nh???t th???t b???i")
            return

    def delete(self):
        employeeId = self.f_employeeId
        if employeeId == 0:
            QtWidgets.QMessageBox.critical(
                None, 'Error', 'No record need delete')
            return

        confirm = QtWidgets.QMessageBox.question(self, 'Message',
                                                 'Are you sure you want to delete ?', QtWidgets.QMessageBox.Yes,
                                                 QtWidgets.QMessageBox.No)
        if confirm == QtWidgets.QMessageBox.Yes:
            if len(employeeId) > 0:
                result = self.Database.DeleteEmployee(employeeId)

                if result:
                    QtWidgets.QMessageBox.information(
                        None, 'Susscess', 'Action susscess')
                    self.loadtableView_EmployeeList()
                    self.clear()
                else:
                    QtWidgets.QMessageBox.critical(
                        None, 'Error', "D??? li???u kh??ng t???n t???i")
                    return
        else:
            return

    def clear(self):
        self.f_employeeId = 0
        self.lineEdit_EmployeeName.setText('')
        self.lineEdit_Email.setText('')


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    app.setQuitOnLastWindowClosed(False)
    window = MyWindow()
    sys.exit(app.exec_())
