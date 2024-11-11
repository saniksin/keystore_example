from web3 import Web3
import json

# Connect to web3
w3 = Web3()

# Array with private keys
private_keys = [
    "0x59c6995e998f97a5a004497e5e3eec6bcdfc8c4ad770b7b4b901c7e7f55689d0",
    "0x59c6995e998f97a5a004497e5e3eec6bcdfc8c4ad770b7b4b901c7e7f55689d1",
    "0x59c6995e998f97a5a004497e5e3eec6bcdfc8c4ad770b7b4b901c7e7f55689d2",
    "0x59c6995e998f97a5a004497e5e3eec6bcdfc8c4ad770b7b4b901c7e7f55689d3",
    "0x59c6995e998f97a5a004497e5e3eec6bcdfc8c4ad770b7b4b901c7e7f55689d4",
    "0x59c6995e998f97a5a004497e5e3eec6bcdfc8c4ad770b7b4b901c7e7f55689d5",
    "0x59c6995e998f97a5a004497e5e3eec6bcdfc8c4ad770b7b4b901c7e7f55689d6",
    "0x59c6995e998f97a5a004497e5e3eec6bcdfc8c4ad770b7b4b901c7e7f55689d7",
    "0x59c6995e998f97a5a004497e5e3eec6bcdfc8c4ad770b7b4b901c7e7f55689d8",
    "0x59c6995e998f97a5a004497e5e3eec6bcdfc8c4ad770b7b4b901c7e7f55689d9",
]

# Password for encrypting the keystore file
password = "12345"

# Array for storing encrypted keystore objects
keystore_data = []

# Iterate over private keys and create encrypted objects
for private_key in private_keys:
    account = w3.eth.account.from_key(private_key)
    encrypted_keystore = account.encrypt(password)
    
    # Add the encrypted keystore to the array
    keystore_data.append(encrypted_keystore)

# Save all keystore objects in a single JSON file
with open("keystore_files.json", "w") as file:
    json.dump(keystore_data, file)

print("All keystores successfully created and saved in keystore_files.json")
