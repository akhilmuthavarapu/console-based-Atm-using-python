# console-based-Atm-using-python
Codegnan Bank ATM Simulation

Overview

This program simulates a basic banking system for Codegnan Bank, allowing customers to create accounts and perform various ATM transactions such as withdrawals, deposits, PIN generation/reset, and checking their mini statement.

Features

Account Creation: Users can create accounts by providing their name, date of birth, and an initial deposit.

Withdrawal: Customers can withdraw money from their accounts after PIN verification.

Deposit: Customers can deposit money into their accounts.

PIN Generation & Reset: Customers can create or reset their PIN if forgotten.

Mini Statement: Customers can check their account details and balance.

How It Works

Account Creation

The user enters the number of customers.

Each customer is assigned an account number starting from 1001.

Customers provide their name, date of birth, balance, and a PIN (optional initially but required for transactions).

ATM Operations

The user selects an operation:

Withdraw: Requires account number and PIN.

Deposit: Requires account number and deposit amount.

PIN Generation/Reset: Allows setting or changing the PIN.

Mini Statement: Displays account details after PIN verification.

Exit: Ends the program.

How to Run

Run the Python script.

Enter the number of customers.

Follow the prompts to create accounts and perform transactions.

Error Handling

If an invalid account number is entered, an error message is displayed.

If an incorrect PIN is entered, the transaction is denied.

If an account has no PIN, the user is redirected to PIN generation.

Minimum balance is required to open an account.

Example Execution

Welcome to the Codegnan Bank
****************************************
No of Customers: 2
Account Number: 1001
Enter Customer 1 name: John
Enter Customer 1 dob[dd-mm-yy]: 15-05-90
Enter the customer 1 balance: 5000
Enter Customer 1 pin: 1234
-----Customer 1 Details Saved Successfully -----
****************************************
Account Number: 1002
Enter Customer 2 name: Alice
Enter Customer 2 dob[dd-mm-yy]: 20-07-92
Enter the customer 2 balance: 3000
Enter Customer 2 pin: 5678
-----Customer 2 Details Saved Successfully -----
****************************************
Welcome to the ATM:
1. WITHDRAW
2. DEPOSIT
3. PIN GENERATION / RESET PIN
4. MINI STATEMENT
5. EXIT
****************************************
Enter Your Choice: 1
Enter the Account No [like 1001]: 1001
Enter the pin: 1234
Enter your amount: 2000
 ---- Withdraw Successful !!!! ----
Current Balance:  3000
..Exiting from the Withdraw Window ...

Technologies Used

Programming Language: Python

Future Enhancements

Implement a database for storing account details persistently.

Add transaction history for each customer.

Introduce interest calculation and loan options.

Author

Developed by [Your Name]

