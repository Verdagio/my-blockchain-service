from utils import hash_utils
from utils.validator import Validator
from block import Block
from transaction import Transaction
from functools import reduce

MINER_REWARD = 10

class Blockchain:
   
    def __init__(self, host_id):
        GENESIS_BLOCK = Block(0,'',[],100,0)
        self.chain = [GENESIS_BLOCK]
        self.open_transactions = []
        self.host = host_id

    def create_transaction(self, sender, receiver, amount): 
        tx = Transaction(sender, receiver, amount)
        if Validator.validate_transaction(tx, self.get_balance):
            self.__open_transactions.append(tx)
            return True
        return False

    def mine_block(self, miner):
        hashed_block = hash_utils.hash_block(self.__chain[-1])
        copy_open_tx = self.__open_transactions[:]
        mined_tx = Transaction('MINED', miner, MINER_REWARD)
        copy_open_tx.append(mined_tx)
        block = Block(len(self.__chain), hashed_block, copy_open_tx, self.proof_of_work())
        self.__chain.append(block)
        self.__open_transactions = []
        return True

    def proof_of_work(self):
        last_block = self.__chain[-1]
        last_hash = hash_utils.hash_block(last_block)
        proof = 0
        while not Validator.validate_proof(self.__open_transactions, last_hash, proof):
            proof +=1
        return proof

    def get_balance(self): 
        tx_sender = [[tx.amount for tx in block.transactions if tx.sender == self.host] for block in self.__chain]
        open_tx_sender = [tx.amount for tx in  self.__open_transactions if tx.sender == self.host]
        tx_sender.append(open_tx_sender)
        tx_receiver = [[tx.amount for tx in block.transactions  if tx.receiver == self.host] for block in self.__chain]
        amt_sent = reduce(lambda tx_sum, tx_amt: tx_sum + sum(tx_amt)
                            if len(tx_amt) > 0 else tx_sum + 0, tx_sender, 0)
        amt_rec = reduce(lambda tx_sum, tx_amt: tx_sum + sum(tx_amt)
                            if len(tx_amt) > 0 else tx_sum + 0, tx_receiver, 0)
        return amt_rec - amt_sent
    
    def get_last_block(self):
        return None if len(self.__chain) < 1 else self.__chain[-1]

    @property
    def chain(self):
        return self.__chain[:]

    @chain.setter
    def chain(self, val):
        self.__chain = val
    
    @property
    def open_transactions(self):
        return self.__open_transactions[:]

    @open_transactions.setter
    def open_transactions(self, val):
        self.__open_transactions = val
