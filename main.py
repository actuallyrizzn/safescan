import os
import requests
from dotenv import load_dotenv

# Load the API key from the .env file
load_dotenv()
ETHERSCAN_API_KEY = os.getenv('etherscan_key')

# Etherscan API base URL
BASE_URL = 'https://api.etherscan.io/api'

def get_created_safes(factory_address, start_block=0, end_block=99999999):
    """
    Get Gnosis Safe addresses created by the factory contract.

    Args:
        factory_address (str): The address of the factory contract.
        start_block (int, optional): The starting block number for the query. Defaults to 0.
        end_block (int, optional): The ending block number for the query. Defaults to 99999999.

    Returns:
        list: A list of Gnosis Safe addresses created by the factory contract.
    """
    params = {
        'module': 'logs',
        'action': 'getLogs',
        'fromBlock': start_block,
        'toBlock': end_block,
        'address': factory_address,
        'topic0': '0x4f51faf6c4561ff95f067657e43439f0f856d97c04d9ec9070a6199ad418e235',  # Hash of the ProxyCreation event
        'apikey': ETHERSCAN_API_KEY
    }
    response = requests.get(BASE_URL, params=params)
    safe_addresses = []
    if response.status_code == 200:
        logs = response.json()['result']
        for log in logs:
            # Extract the Safe address from the data field
            safe_address = '0x' + log['data'][:66][-40:]
            safe_addresses.append(safe_address)
    return safe_addresses

# Example usage
factory_address = '0xa6b71e26c5e0845f74c812102ca7114b6a896ab2'
safe_addresses = get_created_safes(factory_address)
print(f'Found {len(safe_addresses)} Gnosis Safe addresses created by the factory.')
