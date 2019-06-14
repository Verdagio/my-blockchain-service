import hashlib
import json

__all__ = ['hash_string', 'hash_block']

def hash_string(input):
    '''
    Takes an input of type string and returns its hashed value.
    Wraps hashlib.sha256().hexdigest()

    Args:
        input: The string to be hashed.
    
    Returns:
        A sha256 hashed string
    '''
    return hashlib.sha256(input).hexdigest()

def hash_block(block):
    '''
    Takes an input of type dict and returns its hashed value.
    Wraps hashlib.sha256().hexdigest()

    Args:
        block: The block object to be hashed.
    
    Returns:
        A sha256 hashed string
    '''
    copied_block = block.__dict__.copy()
    copied_block['transactions'] = [tx.to_ordered_dict() for tx in copied_block['transactions']]
   
    return hash_string(json.dumps(copied_block, sort_keys=True).encode())
