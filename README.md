# Bank Account Management with Logging

This Python code demonstrates how to use the logging module to create a simple bank account management system. The project comprises a BankAccount class, which allows users to authenticate, deposit, withdraw, and view their account balance. Additionally, it logs all transactions and status updates to a log file.

## Features

1. **Logging Transactions:** The primary focus of this project is to illustrate the use of Python's built-in `logging` module. The system logs all account transactions and status updates to a log file called 'formatted.log' in a structured format, including timestamps.

2. **Account Authentication:** Users are prompted to enter their PIN to authenticate themselves before performing transactions.

3. **Deposit:** Users can deposit funds into their account, and the transaction details, including the deposited amount and status, are logged.

4. **Withdrawal:** Users can withdraw funds from their account, and the transaction details, including the withdrawn amount and status, are logged.

5. **Display Balance:** Users can view their account's available balance.

## How to Use

1. Clone the repository or download the code files.

2. Ensure you have Python installed on your system.

3. Run the `bank_account.py` script using a Python interpreter.

4. Follow the on-screen prompts:
   - Authenticate by entering the PIN (default PIN: 1234).
   - Choose to deposit or withdraw funds.
   - Enter the transaction amount.

5. The program will log all transactions and status updates to 'formatted.log'.

## Logging Module Usage

The logging module in Python is used extensively in this project to maintain a structured record of all activities. It demonstrates the following key logging concepts:

- **Logging Levels:** Different levels of log entries (INFO, WARNING, ERROR) are used to categorize the log messages, allowing for easy filtering and identification of issues.

- **Log Formatting:** The `Formatter` class is used to format log messages, including timestamps and custom messages.

- **Logging to Multiple Handlers:** The project showcases how to log to both the console (stdout) and a file (`formatted.log`) using multiple handlers.

## Dependencies

This project only uses the built-in Python modules, so there are no external dependencies to install.

## Customization

Feel free to modify this code to suit your needs. You can change the PIN, add additional features, or further customize the logging format as required.

```python
# Example: Custom log format
formatter = logging.Formatter('%(asctime)s - [%(levelname)s] - %(message)s')
```

## Contribution

If you want to contribute to this project or have any suggestions for improvements, please feel free to submit a pull request or open an issue.

I hope you find this project useful for understanding how the logging module can be employed to create a structured log of activities in a Python application.