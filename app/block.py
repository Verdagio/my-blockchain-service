from time import time

class Block:
    
    def __init__(self, id, previous_hash, transaction_list, proof_of_work, creation_timestamp=None):
        self.id = id
        self.previous_hash = previous_hash
        self.transactions = transaction_list
        self.proof = proof_of_work
        self.timestamp = time() if creation_timestamp is None else creation_timestamp

    def __repr__(self):
        return str(self.__dict__)