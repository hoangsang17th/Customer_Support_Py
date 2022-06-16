# coding=utf-8
import sys
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from module import Database, TableModel


class MyWindow(QtWidgets.QDialog):
    f_itemId = 0

    def __init__(self):
        # Load UI
        super(MyWindow, self).__init__()
        uic.loadUi('UIs/ConfigItem.ui', self)
        # Load button event
        self.Database = Database
        self.pushButton_Insert.clicked.connect(self.insert)
        self.pushButton_Update.clicked.connect(self.update)
        self.pushButton_Delete.clicked.connect(self.delete)
        self.pushButton_Clear.clicked.connect(self.clear)
        self.lineEdit_Money.setValidator(
            QtGui.QIntValidator(0, 999999999, self))
        self.loadcomboBox_Employee()

        # Load table list item
        self.tableView_itemList.setShowGrid(False)
        self.loadtableView_ItemList()
        self.tableView_itemList.resizeColumnsToContents()
        self.tableView_itemList.horizontalHeader().setStretchLastSection(True)
        self.tableView_itemList.clicked.connect(self.rowClick)
        self.tableView_itemList.setSelectionBehavior(1)
        self.tableView_itemList.sortByColumn(0, QtCore.Qt.AscendingOrder)
        self.tableView_itemList.setSortingEnabled(True)

        # Build form
        self.exec_()

    def loadcomboBox_Employee(self):
        self.comboBox_Employee.clear()
        rows = self.Database.GetEmployees()
        self.comboBox_Employee.addItem('', -1)

        for row in rows:
            try:
                self.comboBox_Employee.addItem(
                    row[1], row[0])
            except Exception as e:
                QtWidgets.QMessageBox.critical(None, 'Error', str(e))

    def loadtableView_ItemList(self):
        header = ['Item ID',
                  'Item Name', 'Amount', 'Employee', 'Date']
        model = TableModel.TableModel(self, header, self.item_GetList())
        self.tableView_itemList.setModel(model)

    def rowClick(self):
        try:
            for index in self.tableView_itemList.selectedIndexes():
                data = index.data()
                if index.column() == 0:
                    self.f_itemId = data
                elif index.column() == 1:
                    self.lineEdit_ItemName.setText(data)
                elif index.column() == 2:
                    self.lineEdit_Money.setText(data)
                elif index.column() == 3:
                    index = self.comboBox_Employee.findText(
                        data, QtCore.Qt.MatchFixedString)
                    if index >= 0:
                        self.comboBox_Employee.setCurrentIndex(index)
        except Exception as e:
            QtWidgets.QMessageBox.critical(None, 'Error', str(e))

    def item_GetList(self):
        rows = self.Database.GetItems()
        return rows

    def captureCAM(self):
        pass

    def insert(self):
        itemName = str(self.lineEdit_ItemName.text())
        money = str(self.lineEdit_Money.text())
        employeeId = self.comboBox_Employee.itemData(
            self.comboBox_Employee.currentIndex())
        if (itemName == '' or employeeId == 0):
            QtWidgets.QMessageBox.critical(
                None, 'Error', 'Not enough inputed (*) value')
            return

        result = self.Database.CreateItem(itemName, money, employeeId)
        if result:
            QtWidgets.QMessageBox.information(
                None, 'Susscess', 'Action susscess')
            self.loadtableView_ItemList()
            self.clear()
        else:
            QtWidgets.QMessageBox.critical(None, 'Error', "Không thể tạo")
            return

    def update(self):
        itemId = self.f_itemId
        itemName = str(self.lineEdit_ItemName.text())
        money = str(self.lineEdit_Money.text())
        employeeId = self.comboBox_Employee.itemData(
            self.comboBox_Employee.currentIndex())
        if itemId == 0 or itemName == '' or employeeId == 0:
            QtWidgets.QMessageBox.critical(
                None, 'Error', 'Not enough inputed (*) value')
            return

        result = self.Database.UpdateItem(itemId, itemName, money, employeeId)
        if result:
            QtWidgets.QMessageBox.information(
                None, 'Susscess', 'Action susscess')
            self.loadtableView_ItemList()
        else:
            QtWidgets.QMessageBox.critical(None, 'Error', "Không thể cập nhập")
            return

    def delete(self):
        itemId = self.f_itemId
        if itemId == 0:
            QtWidgets.QMessageBox.critical(
                None, 'Error', 'No record need delete')
            return

        confirm = QtWidgets.QMessageBox.question(self, 'Message',
                                                 'Are you sure you want to delete ?', QtWidgets.QMessageBox.Yes,
                                                 QtWidgets.QMessageBox.No)
        if confirm == QtWidgets.QMessageBox.Yes:
            if len(itemId) > 0:
                result = self.Database.DeleteItem(itemId)
                if result:
                    QtWidgets.QMessageBox.information(
                        None, 'Susscess', 'Action susscess')
                    self.loadtableView_ItemList()
                    self.clear()
                else:
                    QtWidgets.QMessageBox.critical(
                        None, 'Error', "Không thể xoá")
                    return
        else:
            return

    def clear(self):
        self.f_itemId = 0
        self.lineEdit_ItemName.setText('')
        self.lineEdit_Money.setText('')
        self.loadcomboBox_Employee()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    sys.exit(app.exec_())
