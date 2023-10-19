import logging
import random
import sys

# Initialize the logger
logger = logging.getLogger(__name__)
stream_handler = logging.StreamHandler(sys.stdout)
file_handler = logging.FileHandler('formatted.log')

# Define a formatter for log messages
formatter = logging.Formatter('%(asctime)s - %(message)s')
stream_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)

# Add handlers to the logger
logger.addHandler(stream_handler)
logger.addHandler(file_handler)
logger.setLevel(logging.INFO)

class BankAccount:
    def __init__(self):
        self.balance = 100
        print("Hello! Welcome to the ATM Depot!")

    def authenticate(self):
        while True:
            # Get and validate the account PIN
            pin = int(input("\nEnter account pin: "))
            while pin != 1234:
                logger.error("Invalid pin.")
                pin = int(input("Try again: "))
            return None

    def deposit(self):
        try:
            # Get the deposit amount
            amount = float(input("Enter amount to be deposited: "))
            if amount < 0:
                logger.warning("You entered a negative number to deposit.")
            # Update the balance and log the transaction
            self.balance += amount
            logger.info(f"Amount Deposited: {amount}")
            self.log_transaction("Successful")

        except ValueError:
            self.log_transaction("Failed")

    def withdraw(self):
        try:
            # Get the withdrawal amount
            amount = float(input("Enter amount to be withdrawn: "))
            if self.balance >= amount:
                # Update the balance and log the transaction
                self.balance -= amount
                logger.info(f"You withdrew: {amount}")
                self.log_transaction("Successful")
            else:
                logger.error("Insufficient balance to complete withdraw.")
                self.log_transaction("Failed")

        except ValueError:
            self.log_transaction("Failed")

    def display(self):
        print("\nAvailable Balance =", self.balance)

    def log_transaction(self, status):
        # Log a transaction with a random transaction number
        transaction_number = random.randint(10000, 1000000)
        logger.info("\nTransaction Info:")
        logger.info(f"Status: {status}")
        logger.info(f"Transaction #{transaction_number}")

# Create a BankAccount object
acct = BankAccount()

# Authenticate the user
acct.authenticate()

# Perform deposit and withdrawal transactions
acct.deposit()
acct.withdraw()

# Display the updated balance
acct.display()
