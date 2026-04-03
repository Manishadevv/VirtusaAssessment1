 ## Banking System Simulation
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



##  Author

- Name: Manisha Devi S
- GitHub: @manishadevv
