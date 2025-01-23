# Basic ATM Application

This is a simple ATM application built using Python and Tkinter. It allows users to perform basic banking operations such as checking balance, depositing funds, withdrawing funds, transferring funds, viewing transaction history, and changing PIN.

## Features

- **Check Balance**: View the current balance.
- **Deposit Funds**: Deposit a specified amount into the account.
- **Withdraw Funds**: Withdraw a specified amount from the account.
- **Transfer Funds**: Transfer a specified amount to another account.
- **Transaction History**: View the history of all transactions.
- **Change PIN**: Change the account PIN.

## Requirements

- Python 3.x
- Tkinter library (usually included with Python)

## Installation

1. Clone the repository or download the source code.
2. Ensure you have Python 3.x installed on your system.
3. Run the `basic-atm.py` file using Python.

```sh
python basic-atm.py
```

## Usage

1. Launch the application.
2. Enter the PIN (default is `1234`).
3. Use the buttons to navigate through different operations:
   - **Deposit**: Enter the amount and click "Deposit".
   - **Withdraw**: Enter the amount and click "Withdraw".
   - **Transfer**: Enter the amount and account number, then click "Transfer".
   - **Transaction History**: View the history of transactions.
   - **Bank Inquiry**: View the current balance.
   - **Change PIN**: Enter the old PIN and new PIN to change the account PIN.
   - **Logout**: Return to the welcome screen.

## Customization

- **Initial Balance**: Modify the `self.balance` variable in the `ATM` class constructor.
- **Default PIN**: Change the `self.pin` variable in the `ATM` class constructor.

## License

This project is licensed under the godopgaming License.
