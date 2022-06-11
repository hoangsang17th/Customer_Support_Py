import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="shop"
)

mycursor = conn.cursor()


def GetCustomers():
    mycursor.execute("SELECT * FROM customer")
    return mycursor


def CreateCustomer(cccd, name, phone, address):
    query = f"INSERT INTO customer (cccd, name, phone, address) VALUES ({cccd}, {name}, {phone}, {address})"

    mycursor.execute(query)
    mycursor.execute("SELECT * FROM customer")
    return mycursor
