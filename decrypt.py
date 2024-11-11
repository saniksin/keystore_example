from web3 import Web3
import json

# Connect to web3
w3 = Web3()

# Password for decrypting the keystore file
password = "12345"

# Load the consolidated keystore file
with open("keystore_files.json", "r") as file:
    keystore_data = json.load(file)

# Iterate over each encrypted keystore object and decrypt it
for encrypted_keystore in keystore_data:
    # Decrypt the keystore with the password to obtain the private key
    private_key = w3.eth.account.decrypt(encrypted_keystore, password)
    
    # Use from_key to create an account from the private key
    account = w3.eth.account.from_key(private_key)

    # Print the address and private key
    print(f"Address: {account.address}")
    print(f"Private Key: {private_key.hex()}")
