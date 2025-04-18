# Simple blockchain system implementation
# How my project works
I am using Python to create this project and calculating our hash with the SHA-256 algorithm.

# Transaction Flow
The user will create a transaction by specifying the following
: a. sender's address
, b. Recipient's address
c. Amount
Then the transaction will be saved in the "pending transaction" folder

# Block workflow
1) The code will retrieve all pending transactions from the "pending transaction" folder
2) A new block will be created, which includes block height, previous block height, and transactions
3) This new block's hash will be calculated and saved in the blocks folder.

# Prerequisites
There is no prerequisite needed, we are using all standard Python libraries

The user can create two folders named 'pending transactions' and 'blocks' and run this system.
