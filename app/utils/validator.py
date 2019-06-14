'''Provides validation logic to ensure security for multiple elements in our blockchain'''

import utils.hash_utils as hash_utils

class Validator:

    @staticmethod
    def validate_proof(transactions, last_hash, proof):
        '''
        Encodes:
        1 - the list of open transactions
        2 - the hash of the previous block
        3 - a number 0 - n

        into bytes,  creates a hash from this, and validates the hash

        Args:
            transactions: list of open transactions
            last_hash: the hash of the previous block
            proof: a non negative whole number

        Returns:
            True if the validators hash first 2 characters are: '00'

        '''
        validator = (str([tx.to_ordered_dict() for tx in transactions]) + str(last_hash) + str(proof)).encode()
        validator_hash = hash_utils.hash_string(validator)
        return validator_hash[0:2] == '00'
    
    @staticmethod
    def validate_transaction(transaction, get_balance):
        '''
        Checks that the user has enough funds to complete the transaction

        Args:
            transaction: an object which contains the sender, receiver, and amount
            get_balance: a function which checks the users balance
        Returns:
            True if the user has enough funds
            False if the user does not have enough funds
        '''
        balance = get_balance()
        return balance >= transaction.amount

    @classmethod
    def is_valid_chain(cls, blockchain):
        '''
        Validates that the blockchain itself is pure.
        Done by comparing the hashes and proofs of each 
        block to ensure correctness.

        Args:  
            blockchain: the chain of blocks to validate

        Returns:
            True if the blockchain is indeed valid 
            False if it is not.

        '''
        for (i, block) in enumerate(blockchain):
            if i == 0:
                continue  # No need to verify the the genesis block
            if block.previous_hash != hash_utils.hash_block(blockchain[i - 1]):
                return False 
            if not cls.validate_proof(block.transactions[:-1], block.transactions, block.proof):
                return False
        return True

    @classmethod
    def validate_open_transactions(cls, open_transactions):
        '''
        Validates all open transactions

        Args:
            open_transactions: list of pending transactions

        Returns:
            True if all are valid
            False if not
        '''
        return all(list(map(cls.validate_transaction, open_transactions)))
    

