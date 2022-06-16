import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="shop"
)

mycursor1 = conn.cursor()
mycursor2 = conn.cursor(buffered=True)


def GetCustomers():
    mycursor1.execute("SELECT * FROM customer")
    return mycursor1


def GetCustomersWhere(cccd):
    mycursor1.execute("SELECT * FROM customer WHERE cccd = %s" % (cccd))
    myresult = mycursor1.fetchall()
    return myresult


def CreateCustomer(cccd, name, phone, address):
    try:
        query = "INSERT INTO customer (cccd, name, phone, address) VALUES (%s, %s, %s, %s)"
        data = (cccd, name, phone, address)
        mycursor1.execute(query, data)
        conn.commit()
        return True
    except:
        return False

# ############ DONE - Employee


def GetEmployee(id):
    mycursor1.execute("SELECT * FROM employee WHERE id= %s LIMIT 1" % (id))
    return mycursor1


def GetEmployees():
    mycursor1.execute("SELECT * FROM employee")
    return mycursor1


def CreateEmployee(name, email):
    try:
        query = "INSERT INTO employee (name, email) VALUES (%s, %s)"
        data = (name, email)
        mycursor1.execute(query, data)
        conn.commit()
        return True
    except:
        return False


def DeleteEmployee(id):
    try:
        mycursor1.execute("DELETE FROM employee WHERE id = %s" % (id))
        conn.commit()
        return True
    except:
        return False


def UpdateEmployee(id, name, email):
    try:
        query = "UPDATE employee SET name = %s, email = %s WHERE id = %s"
        data = (name, email, id)
        mycursor1.execute(query, data)
        conn.commit()
        return True
    except:
        return False


# ############ Items


def GetItems():
    mycursor2.execute("SELECT * FROM item")
    # mycursor.fetchall()
    dataItem = []
    for data in mycursor2:
        employeesTemp = GetEmployee(data[3])
        for employeeTemp in employeesTemp:
            dataItem.append([str(data[0]), str(data[1]),
                            str(data[2]), str(employeeTemp[1]), str(data[4])])
            # return

    return dataItem


def CreateItem(name, amount, employeeId):
    try:
        query = "INSERT INTO item (name, amount, employeeId) VALUES (%s, %s, %s)"
        data = (name, amount, employeeId)
        mycursor2.execute(query, data)
        conn.commit()
        return True
    except:
        return False


def DeleteItem(id):
    try:
        mycursor2.execute("DELETE FROM item WHERE id = %s" % (id))
        conn.commit()
        return True
    except:
        return False


def UpdateItem(id, name, amount, employeeId):
    try:
        query = "UPDATE item SET name = %s, amount = %s, employeeId = %s WHERE id = %s"
        data = (name, amount, employeeId, id)
        mycursor2.execute(query, data)
        print("Update thành công")
        conn.commit()
        return True
    except:
        return False
