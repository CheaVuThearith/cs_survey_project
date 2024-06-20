from sqlite3 import Cursor
from typing import Union
from typing import Literal
import pymysql
from pymysql.cursors import DictCursor
from sql_credentials import get_creds

from dataclasses import dataclass
from datetime import date, time


@dataclass
class Customer_Type:
    CustomerID: int
    Name: str
    PhoneNumber: str
    Status: str
    TimesVisited: int
    TimesCancelled: int
    AmountSpent: int


@dataclass
class Table_Type:
    TableID: int
    Capacity: str
    Status: str


@dataclass
class Employee_Type:
    EmployeeID: int
    FirstName: str
    LastName: str
    Gender: str
    Position: str
    Username: str
    Password: str


@dataclass
class Reservation_Type:
    ReservationID: int
    StartTime: time
    EndTime: time
    BookingDate: date
    TableID: int
    CustomerID: int


def make_connection() -> pymysql.Connection:
    conn = pymysql.connect(
        host="localhost", user="root", password=get_creds(), db="cs_survey"
    )
    return conn


tables = Literal["Customers", "Employees", "Reservations", "Tables"]


def get_data(
    table: tables, page, where, limit=3
) -> Union[Reservation_Type, Employee_Type, Table_Type, Customer_Type]:
    conn = make_connection()
    cur: Cursor = conn.cursor(DictCursor)
    command = f"select * from {table} where {where} limit {limit} offset {3*(page-1)}"
    cur.execute(command)
    conn.close()
    return cur.fetchall()


def find_reservation_data(TableID):
    conn = make_connection()
    cur: Cursor = conn.cursor(DictCursor)
    command = f"select Name, EndTime, Reservations.CustomerID FROM Reservations INNER JOIN Tables ON Reservations.TableID = Tables.TableID INNER JOIN Customers ON Reservations.CustomerID = Customers.CustomerID Where Reservations.TableID = {TableID}"
    cur.execute(command)
    conn.close()
    out = cur.fetchone()
    return out


StatusTables = Literal["Customer", "Table"]
StatusTypes = Literal["Checked In", "Checked Out", "Reserved", "Occupied", "Vacant"]


def update_status(what: StatusTables, Status: StatusTypes, ID):
    conn = make_connection()
    cur: Cursor = conn.cursor(DictCursor)
    command = f"update {what}s set Status = '{Status}' where {what}ID = {ID}"
    cur.execute(command)
    conn.commit()
    conn.close()


getAndSetTypes = Literal["TimesVisited", "AmountSpent", "TimesCancelled"]


def get_and_set(what: getAndSetTypes, CustomerID, incrementValue=1):
    conn = make_connection()
    cur: Cursor = conn.cursor()
    getPrev = f"select {what} from Customers where CustomerID = {CustomerID}"
    cur.execute(getPrev)
    prev = cur.fetchone()

    setPrev = f"update Customers set {what} = {prev[0] + incrementValue} where CustomerID = {CustomerID}"
    cur.execute(setPrev)

    conn.commit()
    conn.close()


def get_and_update_customer_info(amountSpent, CustomerID):
    conn = make_connection()
    cur: Cursor = conn.cursor()

    get_and_set("AmountSpent", CustomerID, amountSpent)

    lastVisitCommand = (
        f"update Customers set LastVisited = now() where CustomerID = {CustomerID}"
    )
    cur.execute(lastVisitCommand)
    conn.commit()
    conn.close()

    get_and_set("TimesVisited", CustomerID, 1)

    delete_reservation(CustomerID)


def delete_reservation(CustomerID):
    conn = make_connection()
    cur: Cursor = conn.cursor(DictCursor)
    deleteCommand = f"delete from Reservations where CustomerID = {CustomerID}"
    cur.execute(deleteCommand)
    conn.commit()
    conn.close()


def check_in(TableID):
    obj = find_reservation_data(TableID)
    CustomerID = obj["CustomerID"]
    update_status("Customer", "Checked In", CustomerID)
    update_status("Table", "Occupied", TableID)


def check_out(TableID, amountSpent):
    obj = find_reservation_data(TableID)
    CustomerID = obj["CustomerID"]
    update_status("Customer", "Checked Out", CustomerID)
    update_status("Table", "Vacant", TableID)
    get_and_update_customer_info(amountSpent, CustomerID)


def cancle_reservation(TableID):
    obj = find_reservation_data(TableID)
    CustomerID = obj["CustomerID"]
    update_status("Table", "Vacant", CustomerID)
    get_and_set("TimesCancelled", CustomerID, 1)
    delete_reservation(CustomerID)
