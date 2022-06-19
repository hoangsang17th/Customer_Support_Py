# coding=utf-8
import sys
from PyQt5 import QtCore, QtWidgets, uic
from module import TableModel, Camera, Database
from datetime import datetime


class MyWindow(QtWidgets.QMainWindow):
    dataInvoiceCustomer = []
    customerFoundList = []

    def __init__(self):
        super(MyWindow, self).__init__()
        uic.loadUi('UIs/App.ui', self)
        # self.setWindowState(QtCore.Qt.WindowMaximized) #Set maxwindow
        self.show()
        # Load event items
        self.Database = Database

        # Link menu
        self.actionConfig_Customer.triggered.connect(self.showConfigCustomer)
        self.actionConfig_Item.triggered.connect(self.showConfigItem)
        self.actionConfig_Invoice.triggered.connect(self.showConfigInvoice)
        self.actionConfig_Employee.triggered.connect(self.showConfigEmployee)

        # Load Camera
        self.initializationCam()

    # Connect camera
    def initializationCam(self):
        self.video = Camera.Video(0)
        self._timer = QtCore.QTimer(self)
        self._timer.timeout.connect(self.loadCamera)
        self.loadCamera()

    # Load camera
    def loadCamera(self):
        self._timer.start(27)

        try:
            defect_out = []
            names = self.getCustomers()

            # Nhân diện khách hàng sử dụng hàm recogitionFace trong Class Camera.py
            self.video.recogitionFace(names, defect_out)

            self.label_videoFrame.setPixmap(self.video.convertFrame())
            self.label_videoFrame.setScaledContents(True)
            self.loadTableView_Data(defect_out)
        except TypeError:
            print("No frame")

    # getList customer
    def getCustomers(self):
        rows = self.Database.GetCustomers()
        data = []
        for row in rows:

            try:
                data.append({'cccd': row[1], 'name': row[2]})

            except Exception as e:
                QtWidgets.QMessageBox.critical(None, 'Error', str(e))
        return data

    # Load dữ liệu thông tin khách hàng lên hệ thống
    def loadTableView_Data(self, data_list):
        header = ['Invoice ID', 'Employee Name',
                  'Customer Name', 'Amount', 'Date']
        data = []

        for customer in data_list:
            if customer not in self.customerFoundList:
                rows = self.Database.GetInvoicesWhere(customer['id'])

                for row in rows:
                    data.append([str(i) for i in row])
                    self.dataInvoiceCustomer.insert(0, [str(i) for i in row])

                # Code gui email tạm thời chưa thực hiện được !
                self.customerFoundList.append(customer)
        # print(self.dataInvoiceCustomer)
        # Xuat file txt
        if self.dataInvoiceCustomer != []:
            theFile = open(
                'dist/Main/file/' + datetime.now().strftime("%Y%m%d%H%M%S") + '.txt', 'w')
            for item in self.dataInvoiceCustomer:
                theFile.write('\n'.join(str(x) for x in item) + '\n')
            theFile.close()

        model = TableModel.TableModel(self, header, self.dataInvoiceCustomer)
        self.tableView_Data.setModel(model)
        self.tableView_Data.resizeRowsToContents()

    # show các Button ra hệ thống

    def showConfigCustomer(self):
        self._timer.stop()
        # self.video.quit()
        del self._timer
        del self.video
        import ConfigCustomer
        ConfigCustomer.MyWindow()
        self.initializationCam()

    def showConfigEmployee(self):
        # self._timer.stop()
        self._timer.stop()
        # self.video.quit()
        del self._timer
        del self.video
        import ConfigEmployee
        ConfigEmployee.MyWindow()
        self.initializationCam()
        # self._timer.start(27)

    def showConfigItem(self):
        # self._timer.stop()
        self._timer.stop()
        # self.video.quit()
        del self._timer
        del self.video
        import ConfigItem as ConfigItem
        ConfigItem.MyWindow()
        self.initializationCam()
        # self._timer.start(27)

    def showConfigInvoice(self):
        # self._timer.stop()
        self._timer.stop()
        # self.video.quit()
        del self._timer
        del self.video
        import ConfigInvoice
        ConfigInvoice.MyWindow()
        self.initializationCam()
        # self._timer.start(27)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    sys.exit(app.exec_())
