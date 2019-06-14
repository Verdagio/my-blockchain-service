from collections import OrderedDict
class Transaction:
    def __init__(self, sender, receiver, amount):
        self.sender = sender
        self.receiver = receiver
        self.amount = amount
    
    def __repr__(self):
        return str(self.__dict__)
    
    def to_ordered_dict(self):
        '''
            Converts a Transaction object to a collections.OrderedDict

            returns:

                OrderedDict([(sender),(receiver),(amount)]) 
        '''
        return OrderedDict([('sender', self.sender), ('receiver', self.receiver), ('amount', self.amount)])
