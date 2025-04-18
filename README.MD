# Simple blockchain system implementation
# How my projrct works
Here, we are using python to create this project also we are calculating our hash with SHA-256 algorithm.

# Transaction Flow
User will create transaction by specifying following
a. senders address
b. Recipients address
c. Amount
Then the transaction will be saved in "pending transaction" folder

# Block work flow
1) Code will retrive all pending transaction from "pending transaction" folder
2) A new block will be created which includes block height, previous block height and transactions
3) This new block's hash will be calculated and saved in blocks folder.

# Prerequisites
There is no any prerequisite needed, we are using all standard python libraries

User can create two folders named 'pending transactions' and 'blocks' and run this system.
