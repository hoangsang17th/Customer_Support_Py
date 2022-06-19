import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="shop"
)
cursorAll = conn.cursor(buffered=True)

cursorOnlyOne_1 = conn.cursor()

cursorOnlyOne_2 = conn.cursor()


def GetCustomer(id):
    cursorOnlyOne_1.execute(
        "SELECT * FROM customer WHERE id= %s LIMIT 1" % (id))
    return cursorOnlyOne_1


def GetCustomers():
    cursorAll.execute("SELECT * FROM customer")
    return cursorAll


def GetCustomersWhere(cccd):
    cursorOnlyOne_1.execute("SELECT * FROM customer WHERE cccd = %s" % (cccd))
    myresult = cursorOnlyOne_1.fetchall()
    return myresult


def CreateCustomer(cccd, name, phone, address):
    try:
        query = "INSERT INTO customer (cccd, name, phone, address) VALUES (%s, %s, %s, %s)"
        data = (cccd, name, phone, address)
        cursorOnlyOne_1.execute(query, data)
        conn.commit()
        return True
    except:
        return False


def GetInvoicesWhere(id):
    cursorAll.execute("SELECT * FROM invoice WHERE customerId = %s" % (id))
    myresult = cursorAll.fetchall()
    return myresult


def GetInvoices():
    cursorAll.execute("SELECT * FROM invoice")
    # mycursor.fetchall()
    dataItem = []
    for data in cursorAll:
        employeesTemp = GetEmployee(data[1])
        for employeeTemp in employeesTemp:
            customersTemp = GetCustomer(data[2])
            for customerTemp in customersTemp:
                dataItem.append([str(data[0]), str(employeeTemp[1]),
                                str(customerTemp[2]), str(data[3]), str(data[4])])
            # return

    return dataItem


# ############ DONE - Employee


def GetEmployee(id):
    cursorOnlyOne_1.execute(
        "SELECT * FROM employee WHERE id= %s LIMIT 1" % (id))
    return cursorOnlyOne_1


def GetEmployees():
    cursorOnlyOne_1.execute("SELECT * FROM employee")
    return cursorOnlyOne_1


def CreateEmployee(name, email):
    try:
        query = "INSERT INTO employee (name, email) VALUES (%s, %s)"
        data = (name, email)
        cursorOnlyOne_1.execute(query, data)
        conn.commit()
        return True
    except:
        return False


def DeleteEmployee(id):
    try:
        cursorOnlyOne_1.execute("DELETE FROM employee WHERE id = %s" % (id))
        conn.commit()
        return True
    except:
        return False


def UpdateEmployee(id, name, email):
    try:
        query = "UPDATE employee SET name = %s, email = %s WHERE id = %s"
        data = (name, email, id)
        cursorOnlyOne_1.execute(query, data)
        conn.commit()
        return True
    except:
        return False


# ############ Items


def GetItems():
    cursorAll.execute("SELECT * FROM item")
    # mycursor.fetchall()
    dataItem = []
    for data in cursorAll:
        employeesTemp = GetEmployee(data[3])
        for employeeTemp in employeesTemp:
            dataItem.append([str(data[0]), str(data[1]),
                            str(data[2]), str(employeeTemp[1]), str(data[4])])
            # return

    return dataItem


def GetItemsName():
    cursorAll.execute("SELECT * FROM item")
    return cursorAll


def CreateItem(name, amount, employeeId):
    try:
        query = "INSERT INTO item (name, amount, employeeId) VALUES (%s, %s, %s)"
        data = (name, amount, employeeId)
        cursorAll.execute(query, data)
        conn.commit()
        return True
    except:
        return False


def DeleteItem(id):
    try:
        cursorAll.execute("DELETE FROM item WHERE id = %s" % (id))
        conn.commit()
        return True
    except:
        return False


def UpdateItem(id, name, amount, employeeId):
    try:
        query = "UPDATE item SET name = %s, amount = %s, employeeId = %s WHERE id = %s"
        data = (name, amount, employeeId, id)
        cursorAll.execute(query, data)
        print("Update thành công")
        conn.commit()
        return True
    except:
        return False
