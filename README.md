 ## 1.JAVA USE CASE - Banking System Simulation
> A console-based Java application simulating core banking operations using Object-Oriented Programming concepts.



##  Project Overview

This project simulates a real-world banking system where users can create accounts, log in, and perform transactions such as deposits, withdrawals, and transfers. Each account type has its own unique rules and restrictions.


## Project Structure


BankingSystem/
│
├── Accounts.java               # Base class with core banking methods
├── SavingsAccount.java         # Minimum balance rule (Rs.1000)
├── CurrentAccount.java         # Overdraft limit (Rs.1000)
├── StudentAccount.java         # Daily withdrawal limit (Rs.1000)
├── TransactionHistory.java     # Records every transaction with date & time
├── Bank.java                   # Manages all accounts (create, login, find)
└── Main.java                   # Menu-driven entry point


## Features

-  Create account (Savings / Current / Student)
-  Login with username and password authentication
-  Deposit money
-  Withdraw money (with account-type rules)
-  Transfer money to another account
-  Check current balance
-  View full transaction history
-  Logout and switch accounts

---

## Account Types & Rules

| Account Type | Rule |
|---|---|
| Savings Account | Balance cannot go below Rs.1000 minimum |
| Current Account | Can overdraft up to Rs.1000 below zero |
| Student Account | Maximum Rs.1000 withdrawal per day |


##  Sample Output

1. Create new Account
2. Login
3. Exit

Enter option: 1
Enter your name: Rahul
Enter your initial balance: 5000
Enter username: rahul123
Enter password: pass123
Enter account type (Savings/Current/Student): Savings
Account created! Your account number is: MDID001

-------------------------------------

1. Deposit
2. Withdraw
3. Transfer
4. Check Balance
5. Transaction History
6. Logout

Enter option: 1
Enter amount: 2000
Deposited: Rs.2000.0

Enter option: 5
[2024-01-15T10:30] Deposit - Rs.2000.0

## Java Concepts Used

| Concept | Where Used |

| **Inheritance** | SavingsAccount, CurrentAccount, StudentAccount extend Accounts |
| **Encapsulation** | Private fields with getters in Accounts.java |
| **Method Overriding** | withdraw() overridden in each child class |
| **ArrayList** | Storing accounts in Bank, transactions in Accounts |
| **Custom Classes** | TransactionHistory stores type, amount, date |
| **Scanner** | All user input handled in Main.java |
| **LocalDateTime** | Timestamps on every transaction |
| **While Loop** | Menu keeps running until user exits |

 ## 2. SQL USECASE

 ## Hospital Management & Patient Analytics System

A relational database project built using **MySQL** that simulates
real-world hospital operations — managing patients, doctors,
appointments, and treatments — while extracting meaningful analytical
insights using advanced SQL techniques.

## Project Overview

Hospitals generate large volumes of data daily. This project designs
a structured relational database to store and analyze that data,
helping hospital administrators make data-driven decisions such as:

- Which doctors are handling the highest patient load?
- What diseases are most commonly diagnosed?
- How much revenue is generated each month?
- Which patients are at high risk based on age?



## Tools & Technologies

| Tool             | Purpose                        |
|------------------|--------------------------------|
| MySQL Workbench  | Database design & query execution |
| SQL (DDL)        | Table creation & schema design |
| SQL (DML)        | Data insertion                 |
| SQL Queries      | Data analysis & reporting      |
| Views            | Reusable virtual tables        |
| Stored Procedures| Reusable parameterized queries |

---

##  Database Schema

### Entity Relationship Overview
```
Patients ──────< Treatments
   │
   └──────────< Appointments >────── Doctors
```

### Tables

| Table        | Columns                                              |
|--------------|------------------------------------------------------|
| Patients     | patient_id, name, age, gender                        |
| Doctors      | doctor_id, name, specialization                      |
| Appointments | appointment_id, patient_id, doctor_id, date          |
| Treatments   | treatment_id, patient_id, diagnosis, cost            |

---

##  Basic Analytical Queries

| # | Query                       | Concepts Used                    |
|---|-----------------------------|----------------------------------|
| 1 | Most Consulted Doctors      | JOIN, COUNT, GROUP BY, ORDER BY  |
| 2 | Total Revenue Per Month     | JOIN, SUM, MONTHNAME, GROUP BY   |
| 3 | Most Common Diseases        | COUNT, GROUP BY, ORDER BY        |
| 4 | Patient Visit Frequency     | JOIN, COUNT, GROUP BY            |
| 5 | Doctor Performance Report   | JOIN x3, SUM, COUNT DISTINCT     |

---

##  Advanced Analytical Queries

| #  | Query                              | Concepts Used                  |
|----|------------------------------------|--------------------------------|                  |
| 6  | Doctors with 3+ Appointments       | HAVING                         |
| 7  | Patient Risk Classification        | CASE WHEN, BETWEEN             |
         |

---

##  Views Created

| View Name              | Purpose                                     |
|------------------------|---------------------------------------------|
| vw_patient_summary     | Patient details combined with diagnosis and cost |
| vw_doctor_workload     | Doctor-wise appointment count               |


---

##  Stored Procedures

| Procedure              | Input Parameter | Purpose                              |
|------------------------|-----------------|--------------------------------------
| MONTHLY_REVENUE_REPORT | month_num (INT) | Revenue report for any given month   |

---

##  How to Run

1. Open **MySQL Workbench**
2. Open the file `hospital_management.sql`
3. Run the full script using `Ctrl + Shift + Enter`
4. Each query result appears in the output panel below
5. To call a stored procedure, run:
```sql
CALL GetDoctorAppointments(1);
CALL GetPatientTotalSpend(2);
CALL MONTHLY_REVENUE_REPORT(11);
```

---

##  File Structure
```
hospital-management-sql/
│
└── hospital_management.sql    # Complete SQL script
    ├── Section 1: Database Setup
    ├── Section 2: Table Creation (DDL)
    ├── Section 3: Sample Data (DML)
    ├── Section 4: Basic Queries
    ├── Section 5: Advanced Queries
    ├── Section 6: Views
    └── Section 7: Stored Procedures
```

---

##  Key SQL Concepts Demonstrated

| Concept           | Where Used                                      |
|-------------------|-------------------------------------------------|
| Primary Key       | All 4 tables                                    |
| Foreign Key       | Appointments, Treatments                        |
| INNER JOIN        | All queries linking multiple tables             |
| GROUP BY          | Queries 1–5, 7, 10                              |
| HAVING            | Query 7 — filter after grouping                 |
| Subquery          | Queries 6, 9                                    |
| CASE WHEN         | Query 8 — patient risk classification           |
| Aggregate Functions | SUM, COUNT, AVG, MAX, MIN                     |
| MONTHNAME()       | Query 2, Procedure 3                            |
| CREATE VIEW       | 3 reusable virtual tables                       |
| Stored Procedure  | 3 parameterized reusable procedures             |
| DELIMITER         | Required for stored procedure blocks in MySQL   |

---

##  Sample Output Snapshots

### Most Consulted Doctors
| doctor_name        | specialization  | total_appointments |
|--------------------|-----------------|--------------------|
| Dr. Senthil Kumar  | Cardiology      | 6                  |
| Dr. Arun Prasad    | General Medicine| 4                  |
| Dr. Ramesh Pillai  | Orthopedics     | 4                  |

### Patient Risk Classification
| patient_name   | age | gender | risk_category |
|----------------|-----|--------|---------------|
| Ravi Kumar     | 60  | Male   | High Risk     |
| Anitha Menon   | 55  | Female | High Risk     |
| Priya Nair     | 45  | Female | Medium Risk   |
| Arjun Sharma   | 28  | Male   | Low Risk      |

### Most Common Diseases
| diagnosis    | total_cases |
|--------------|-------------|
| Hypertension | 4           |
| Arthritis    | 3           |
| Diabetes     | 3           |


# 3. PYTHON USECASE : CaseStudent Result Management System

A desktop application built using Python and Tkinter that manages
student academic records, calculates grades automatically, and
generates performance reports.

## Project Overview

Educational institutions need efficient systems to manage student
results and generate performance insights. This project provides a
simple GUI-based application that allows staff to add, view, search,
and delete student records while automatically computing grades,
percentages, and results based on marks entered.

## Tools and Technologies

| Tool             | Purpose                          |
|------------------|----------------------------------|
| Python 3.x       | Core programming language        |
| Tkinter          | GUI framework (built-in)         |
| CSV Module       | Data storage and file handling   |
| OS Module        | File existence check             |
| Datetime Module  | Date display on dashboard        |


## Features

| Feature            | Description                                        |
|--------------------|----------------------------------------------------|
| Dashboard          | Shows total, passed, failed count and average score |
| Add Student        | Form to enter student details with validation       |
| View Students      | Displays all student records in a table             |
| Search Student     | Search by name or roll number                       |
| Delete Student     | Remove a student record by roll number              |
| Report Card        | Individual student report with grade and result     |
| Class Summary      | Overall class performance and grade distribution    |


## Subjects Covered

| Subject | Code |
|---------|------|
| Computer Networks        | CN   |
| Object Oriented Programming | OOPS |
| Data Structures and Algorithms | DSA  |
| Database Management System | DBMS |
| Operating Systems        | OS   |

Each subject is marked out of 100. Total marks are out of 500.


## Grading System

| Percentage    | Grade         | Result |
|---------------|---------------|--------|
| 90 and above  | O (Outstanding) | Pass |
| 80 to 89      | A+            | Pass   |
| 70 to 79      | A             | Pass   |
| 60 to 69      | B             | Pass   |
| 50 to 59      | C             | Pass   |
| Below 50      | F             | Fail   |

A student also fails if any single subject mark is below 35,
regardless of the total percentage.


## Python Concepts Demonstrated

| Concept              | Where It Is Used                              |
|----------------------|-----------------------------------------------|
| Class and Objects    | Student class with attributes and methods     |
| Constructor (__init__) | Initializes student data automatically      |
| Instance Methods     | calculate_grade(), calculate_result()         |
| Functions            | save_student(), load_students(), delete_student() |
| File Handling        | Reading and writing CSV files                 |
| Exception Handling   | try-except blocks in file operations          |
| Lists                | Storing loaded student records                |
| Dictionary           | CSV rows read as key-value pairs              |
| List Comprehension   | Filtering and searching student records       |
| Conditional Statements | Grade and result logic                      |
| Loops                | Processing student records                    |
| String Methods       | strip(), lower() for input cleaning           |
| Modules              | csv, os, tkinter, datetime                    |
| GUI Programming      | Tkinter frames, labels, buttons, entry, treeview |
| Input Validation     | Checking empty fields, duplicate roll numbers, mark ranges |


## File Structure
student_result_system/
|
|-- student_result.py       # Main application file
|-- student_results.csv     # Auto-generated data storage file
|-- README.md               # Project documentation


## Input Validation Rules

- All fields are required before saving
- Roll number must be unique — duplicates are rejected
- Marks must be numeric values only
- Marks must be between 0 and 100

## Sample Data

| Roll No | Name    | CN | OOPS | DSA | DBMS | OS | Grade | Result |
|---------|---------|----|------|-----|------|----|-------|--------|
| 211478  | Manisha | 54 | 65   | 56  | 45   | 60 | C     | PASS   |
| 211479  | Elava   | 67 | 45   | 87  | 40   | 97 | B     | PASS   |
| 211481  | Siva    | 89 | 67   | 87  | 87   | 98 | A+    | PASS   |


##  Author

- Name: Manisha Devi S
- Virtusa Training (Group-1)
- GitHub: @manishadevv
