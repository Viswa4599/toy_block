'''
Toy Block Chain
Author: Viswajit Vinod Nair
Inspired from : https://www.youtube.com/watch?v=pYasYyjByKI
'''
import hashlib

class vCoinBlock:
    def __init__(self,prev_hash,transaction_list):
        self.prev_hash = prev_hash
        self.transaction_list = transaction_list
        self.block_data = "-".join(transaction_list) + "-" + self.prev_hash
        self.block_hash = hashlib.sha256(self.block_data.encode()).hexdigest()

class vBlockChain:
    def __init__(self):
        self.prev_hash = "init_string"
        self.block_list = []

    def add_block(self,transaction_list):
        block = vCoinBlock(self.prev_hash,transaction_list)
        self.block_list.append(block)
        self.prev_hash = block.block_hash

    def get_chain(self):
        return self.block_list

if __name__ == '__main__':
    t1 = "Anna sends 2 vC to Mike"
    t2 = "Bob sends 4.1 vC to Mike" 
    t3 = "Mike sends 3.2 vC to Bob"
    t4 = "Daniel sends 0.3 vC to Anna"
    t5 = "Mike sends 1 vC to Charlie"
    t6 = "Mike sends 5.4 vC to Daniel"


    data = [[t1,t2],[t2,t4],[t5,t6]]

    block_chain = vBlockChain()

    for transaction_list in data:
        block_chain.add_block(transaction_list)

    chain = [block.block_data for block in block_chain.get_chain()]
    print(chain)
