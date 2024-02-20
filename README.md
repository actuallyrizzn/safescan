# Gnosis Safe Address Fetcher

This Python script interacts with the Etherscan API to fetch information about Gnosis Safe addresses created by a specified factory contract.

## Requirements

- Python 3
- Requests library
- dotenv library

## Setup

1. Install the required dependencies:

    ```bash
    pip install requests python-dotenv
    ```

2. Create a `.env` file in the root directory of the project and add your Etherscan API key:

    ```plaintext
    etherscan_key=YOUR_API_KEY_HERE
    ```

## Usage

Run the script with:

```bash
python main.py
```

The script will output the number of Gnosis Safe addresses created by the specified factory contract.

## TODO still

 - I want to add pagination to go back in history on the factory, since etherscan stops at 1000 results by default. Wasn't important for this version, but I'll include it in future ones.
 - Gonna add command line args to make it more utility, and do the same for the function so it can be included in other libraries.
