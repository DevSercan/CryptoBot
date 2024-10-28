[![ccxt](https://img.shields.io/pypi/v/ccxt)](https://pypi.org/project/ccxt/)
[![colorama](https://img.shields.io/pypi/v/colorama)](https://pypi.org/project/colorama/)

# CryptoBot

This project was developed to facilitate cryptocurrency transactions using the **ccxt** library.

---

## Languages
- [Turkish](README_TR.md)
- [English](README.md)

---

### Requirements
- Python 3.x
- `ccxt` library (Installation instructions are given below)

### How to Get an API Key?
To get an API key on the MEXC exchange, follow the steps below:
  1. Log in to your profile at [mexc.com](https://www.mexc.com/).
  2. Open the **API Management** page.
  3. Using the **Create New API Key** option, specify the required permissions and create your API key.

### Configuring the API Key
1. Open the `keys.json` file located in the project root directory.
2. Add the API key you received to the `keys.json` file as follows:
   ```json
   {
       "accessKey": "YOUR_API_KEY",
       "secretKey": "YOUR_API_SECRET"
   }
> Note: To ensure the security of your API key, store the `keys.json` file in a secure environment and do not share this file.

---

### Setup
1. **For Systems with Python Installed**
   If Python is installed on your computer, you first need to install the dependencies listed in the `requirements.txt` file. To install them, open a terminal in the root directory and enter the command `pip install -r requirements.txt`. Once the setup is complete, you can start the software by running the `main.py` file.
   
2. **For Systems without Python Installed**
   If Python is not installed, you can start the program directly by running the `main.exe` application.

---

### Usage
The software operates via a console interface for user interaction. You can access functions using the following command numbers:
- 0: Clears the console.

- 1: Initiates a cryptocurrency purchase transaction.
  - Trading Pair: Enter the trading pair you wish to trade, e.g., BTC/USDC.
  - Amount: Enter the amount you wish to purchase. Use a decimal point for fractional amounts, e.g., 0.14.

- 2: Initiates a cryptocurrency sale transaction.
  - Trading Pair: Enter the trading pair you wish to sell, e.g., BTC/USDC.
  - Amount: Enter the amount you wish to sell. Use a decimal point for fractional amounts, e.g., 0.14.

- 3: Displays your current balance information.