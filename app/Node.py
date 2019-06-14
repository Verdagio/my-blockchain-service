from uuid import uuid4
from blockchain import Blockchain
from utils.validator import Validator

class Node:
    def __init__(self):
        self.id = uuid4()
        self.blockchain = Blockchain(self.id) 

    def input_listener(self):
        session_active = True

        while session_active:   
            self.print_menu()
            user_choice = input('Please enter a choice: ')
            if user_choice == '1':
                tx_data = self.get_tx_info()
                receiver, amount = tx_data
                if self.blockchain.create_transaction(self.id, receiver ,amount):
                    print('Transaction added')
                else:
                    print('Transaction failed')
                print(self.blockchain.open_transactions)
            elif user_choice == '2':
                self.blockchain.mine_block(self.id)    
            elif user_choice == '3':
                self.print_blockchain()
            elif user_choice == '4':
                
                if Validator.validate_transaction(self.blockchain.open_transactions, self.blockchain.get_balance):
                    print('Transactions validated')
                else:
                    print('Could not validate all transactions')
            elif user_choice == 'q' or user_choice == 'Q':
                session_active = False
                break
            else:
                print('invalid input')
            if not Validator.is_valid_chain(self.blockchain.chain):
                self.print_blockchain()
                print('Corrupted Blockchain, exiting')
                break

    def print_menu(self):
        print(f'User: {self.id}\nBalance: {self.blockchain.get_balance()}\n')
        print('1 : Create Transaction')
        print('2 : Mine block')
        print('3 : Output all Blocks in blockchain')
        print('4 : Validate Transaction')
        print('q : Quit')
        print('---------------------')
    
    def get_tx_info(self):
        receiver = input('enter receiver')
        amount = float(input('enter amount'))
        return receiver, amount
    
    def print_blockchain(self):
        map(lambda b: print(f'{b}\n'), self.blockchain.chain)

if __name__ == '__main__':
    node = Node()
    node.input_listener()
