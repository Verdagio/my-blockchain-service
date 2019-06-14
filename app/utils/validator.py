'''Provides validation logic to ensure security for multiple elements in our blockchain'''

import utils.hash_utils as hash_utils

class Validator:

    @staticmethod
    def validate_proof(transactions, last_hash, proof):
        validator = (str([tx.to_ordered_dict() for tx in transactions]) + str(last_hash) + str(proof)).encode()
        validator_hash = hash_utils.hash_string(validator)
        return validator_hash[0:2] == '00'
    
    @staticmethod
    def validate_transaction(transaction, get_balance):
        balance = get_balance()
        return balance >= transaction.amount

    @classmethod
    def is_valid_chain(cls, blockchain):
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
        return all(list(map(cls.validate_transaction, open_transactions)))
    

