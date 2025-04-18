import json
import hashlib
import time
import os

#creates class to represent the blockchain
class Block:
    def __init__(self, height, previous_block_hash, transactions):
        self.height = height
        self.timestamp = int(time.time())
        self.previous_block_hash = previous_block_hash
        self.body = transactions
        self.hash = self.calculate_hash()

#Calculates hash using SHA256 based on the header (new file name)
    def calculate_hash(self):
        header = {
            "height": self.height,
            "timestamp": self.timestamp,
            "previous_block_hash": self.previous_block_hash,
            "body_hash": self.calculate_body_hash()
        }
        header_json = json.dumps(header, separators=(',', ':'))
        hash_object = hashlib.sha256(header_json.encode())
        return hash_object.hexdigest()

#Calculates hash using SHA256 based on body
    def calculate_body_hash(self):
        body_json = json.dumps(self.body, separators=(',', ':'))
        hash_object = hashlib.sha256(body_json.encode())
        return hash_object.hexdigest()

#saves the block as a json in the blocks folder
    def save_to_file(self, block_folder):
        file_name = self.hash + ".json"
        file_path = os.path.join(block_folder, file_name)
        with open(file_path, "w") as f:
            json.dump(self.to_json(), f)
        return file_name

#returns the file as a .json file
    def to_json(self):
        return {
            "height": self.height,
            "timestamp": self.timestamp,
            "previous_block_hash": self.previous_block_hash,
            "body": self.body,
            "hash": self.hash  # Add the hash to the JSON data
        }

#processes the files in the pending_transactions folder and moves to blocks folder
def process_transactions(pending_folder, block_folder):
    transactions = []
    for file in os.listdir(pending_folder):
        if file.endswith(".json"):
            with open(os.path.join(pending_folder, file), "r") as f:
                transaction_data = json.load(f)
            transactions.append(transaction_data)
            os.remove(os.path.join(pending_folder, file))
    block_height = get_block_height(block_folder)
    previous_block_hash = get_latest_block_hash(block_folder) if block_height > 0 else "0"
    
    block = Block(block_height, previous_block_hash, transactions)
    file_name = block.save_to_file(block_folder)
    print(f"Block {block_height} saved to {file_name} in block folder")
    return block.hash

#returns block height by finding current number of files in block folder 
def get_block_height(block_folder):
    return len(os.listdir(block_folder))

#hashes the body
def calculate_body_hash(body):
    body_json = json.dumps(body, separators=(',', ':'))
    hash_object = hashlib.sha256(body_json.encode())
    return hash_object.hexdigest()

#gets the latest hash and returns 
def get_latest_block_hash(block_folder):
    files = os.listdir(block_folder)
    if not files:
        return "0"
    latest_block_file = max(files, key=lambda file: int(file.split('.')[0], 16))
    with open(os.path.join(block_folder, latest_block_file), "r") as f:
        block_data = json.load(f)
    if "hash" in block_data:
        return block_data["hash"]
    else:
        # Calculate the hash using the block's data
        height = block_data["height"]
        if isinstance(height, str):  # Check if height is a string
            height = int(height, 16)  # Convert hexadecimal string to integer
        header = {
            "height": height,
            "timestamp": block_data["timestamp"],
            "previous_block_hash": block_data["previous_block_hash"],
            "body_hash": calculate_body_hash(block_data["body"])
        }
        header_json = json.dumps(header, separators=(',', ':'))
        hash_object = hashlib.sha256(header_json.encode())
        return hash_object.hexdigest()

def main():
    pending_folder = "pending_transactions"
    block_folder = "blocks"
    if not os.path.exists(block_folder):
        os.makedirs(block_folder)
    
    process_transactions(pending_folder, block_folder)

if __name__ == "__main__":
    main()