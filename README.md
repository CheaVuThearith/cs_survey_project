# CS Survey Project

Welcome to the CS Survey Project! This project is designed to manage restaurant reservations, customers, tables, and employees. Follow the instructions below to set up and run the project on your local machine.

## Prerequisites

Before you begin, ensure you have the following software installed on your machine:

- Python 3.x
- MySQL Server
- MySQL Workbench

## Setup Instructions

### 1. Configure Database Credentials

First, update the database credentials in the `sql_credentials.py` file.

1. Open the `sql_credentials.py` file.
2. Locate the `get_creds` function and update it with your MySQL database password:

```python
def get_creds():
    return "enter_ur_db_pw"
```

Replace `"enter_ur_db_pw"` with your actual MySQL database password.

### 2. Create the Database and Tables

Next, use MySQL Workbench to set up the database and tables required for the project.

1. Open MySQL Workbench and connect to your MySQL Server.
2. Copy and paste the following SQL commands into a new SQL script:

```sql
create database cs_survey;
use cs_survey;
create TABLE Customers (
CustomerID INT PRIMARY KEY AUTO_INCREMENT,
Name VARCHAR(50),
PhoneNumber VARCHAR(15),
Status VARCHAR(20) DEFAULT "Checked Out",
TimesVisited int DEFAULT 0,
TimesCancelled int DEFAULT 0,
AmountSpent float(10,3) DEFAULT 0,
LastVisited TIMESTAMP  DEFAULT NOW()
);

create table Tables (
TableID int primary key AUTO_INCREMENT,
Capacity varchar(10),
Status varchar(20)
);

create table Employees(
EmployeeID int PRIMARY key AUTO_INCREMENT,
FirstName varchar(25),
LastName varchar(25),
Gender varchar(10),
Position varchar(20),
Username varchar(50),
Password varchar(50)
);

create table Reservations(
ReservationID int primary key AUTO_INCREMENT,
StartTime TIME,
EndTime TIME,
BookingDate DATE,
TableID int NOT NULL,
CustomerID int NOT NULL,
FOREIGN KEY (TableID) REFERENCES Tables(TableID),
FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID)
);
INSERT INTO Tables (Capacity, Status) VALUES
('1 - 2', 'Vacant'),
('1 - 2', 'Vacant'),
('1 - 2', 'Vacant'),
('1 - 2', 'Vacant'),
('1 - 2', 'Vacant'),
('3 - 4', 'Vacant'),
('3 - 4', 'Vacant'),
('3 - 4', 'Vacant'),
('3 - 4', 'Vacant'),
('3 - 4', 'Vacant'),
('5 - 10', 'Vacant'),
('5 - 10', 'Vacant'),
('5 - 10', 'Vacant'),
('5 - 10', 'Vacant'),
('5 - 10', 'Vacant'),
('3 - 4', 'Vacant'),
('3 - 4', 'Vacant'),
('3 - 4', 'Vacant'),
('3 - 4', 'Vacant'),
('3 - 4', 'Vacant');
INSERT INTO Customers (Name, PhoneNumber) VALUES 
('John Doe', '123-456-7890'), 
('Jane Smith', '234-567-8901'), 
('Alice Johnson', '345-678-9012'), 
('Bob Brown', '456-789-0123'), 
('Carol Davis', '567-890-1234');
```

3. Run the script to create the `cs_survey` database and its tables.

### 3. Run the Application

Now that the database is set up, you can run the main application.

1. Open a terminal or command prompt.
2. Navigate to the project directory.
3. Run the following command to start the application:

```bash
python main.py
```

## Usage

Once the application is running, you can start using it to manage customers, tables, employees, and reservations.

## Contributing

If you'd like to contribute to this project, please fork the repository and create a pull request with your changes.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.

---

If you encounter any issues or have any questions, feel free to open an issue in the repository.

Happy coding!
