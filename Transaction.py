import json
import hashlib
import time
import os
from Block import get_block_height

# Sets a class for the transactions
class Transaction:
    def __init__(self, from_addr, to_addr, amount, height):
        self.height = height
        self.timestamp = int(time.time())
        self.from_addr = from_addr
        self.to_addr = to_addr
        self.amount = amount

    # Returns json file 
    
    def to_json(self):
        return {
            "height": self.height,
            "timestamp": self.timestamp,
            "from": self.from_addr,
            "to": self.to_addr,
            "amount": self.amount
        }

    # Saves the file as .json in the pending_transactions folder
    def save_to_file(self, pending_folder):
        json_data = json.dumps(self.to_json(), separators=(',', ':'))
        hash_object = hashlib.sha256(json_data.encode())
        file_name = hash_object.hexdigest() + ".json"
        file_path = os.path.join(pending_folder, file_name)
        with open(file_path, "w") as f:
            f.write(json_data)
        return file_name

# Gets input from user and saves to folder
def get_transaction_from_user(pending_folder, current_block_height):
    from_addr = input("Enter from address: ")
    to_addr = input("Enter to address: ")
    amount = int(input("Enter amount: "))
    transaction = Transaction(from_addr, to_addr, amount, current_block_height)
    file_name = transaction.save_to_file(pending_folder)
    print(f"Transaction saved to {file_name} in pending_transactions folder")

if __name__ == "__main__":
    pending_folder = "pending_transactions"
    block_folder = "blocks"
    

    
    current_block_height = get_block_height(block_folder)
    get_transaction_from_user(pending_folder, current_block_height)
