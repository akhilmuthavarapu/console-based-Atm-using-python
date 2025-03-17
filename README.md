# Codegnan Bank ATM System 🚀🏦💳

## Description 📜💡🔍
This project is a simple command-line ATM system for Codegnan Bank, developed in Python. It allows users to create bank accounts and perform basic banking operations, such as withdrawals, deposits, PIN generation/reset, and viewing mini statements. This system provides a basic simulation of an ATM, making it a useful project for learning fundamental banking operations and Python programming. 🎯📊💻

## Features 🔥⚡🎉
- **Account Creation**: Users can create a bank account with a unique account number.
- **Secure Transactions**: Withdrawals and deposits require the correct account number and PIN.
- **PIN Management**: Users can generate or reset their PIN.
- **Mini Statement**: Users can view their account details, including balance and date of birth.
- **Command-Line Interface**: A simple and interactive CLI-based banking system.

## Prerequisites 🛠️🔧📌
Before running the program, ensure you have the following:
- Python 3.x installed on your system

## How to Run 🚀🖥️⚙️
1. Clone this repository to your local machine:
   ```bash
   git clone https://github.com/yourusername/codegnan-bank-atm.git
   cd codegnan-bank-atm
   ```
2. Run the script:
   ```bash
   python codegnan_atm.py
   ```

## Usage Guide 📋📝✅
1. **Account Creation**: 🏦📂🎫
   - Enter the number of customers.
   - For each customer, provide the name, date of birth (in `dd-mm-yy` format), initial balance, and PIN.
   - Each account is assigned a unique account number starting from `1001`.

2. **ATM Operations**: 💳🏧🔄
   - **Withdraw**:
     - Enter the account number and PIN.
     - Specify the amount to withdraw.
     - If funds are sufficient, the withdrawal is processed.
     - Updated balance is displayed.
   - **Deposit**:
     - Enter the account number.
     - Specify the amount to deposit.
     - Updated balance is displayed.
   - **PIN Generation/Reset**:
     - Users without a PIN are prompted to create one.
     - Users with an existing PIN can reset it by entering the old PIN.
   - **Mini Statement**:
     - Users can view their account details, including account number, name, date of birth, and balance.
   - **Exit**:
     - Users can exit the ATM system at any time.

## Example Output 📌📊🔢
```
Welcome to the Codegnan Bank  
****************************************
No of Customers: 2
Account Number: 1001
Enter Customer 1 name: John Doe
Enter Customer 1 dob[dd-mm-yy]: 12-05-90
Enter the customer 1 balance: 5000
Enter Customer 1 pin: 1234
-----Customer 1 Details Saved Successfully -----
****************************************
Account Number: 1002
Enter Customer 2 name: Alice Smith
Enter Customer 2 dob[dd-mm-yy]: 22-08-85
Enter the customer 2 balance: 3000
Enter Customer 2 pin: 5678
-----Customer 2 Details Saved Successfully -----
****************************************
Welcome to the Atm:
1. WITHDRAW
2. DEPOSIT
3. PIN GENERATION / RESET PIN
4. MINI STATEMENT
5. EXIT
****************************************
Enter Your Choice:
```

## Error Handling ⚠️🚨🔄
- If an invalid account number is entered, an error message is displayed.
- If a user enters the wrong PIN, access to the account is denied.
- If insufficient funds are available, the withdrawal is canceled.
- If an incorrect menu option is selected, an error message is shown.

## Contributing 🤝📌💡
Contributions are welcome! Feel free to fork this repository, make modifications, and submit a pull request with your improvements.

## License 📜⚖️✅
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details. 🎓🔏📝

