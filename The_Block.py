import hashlib
import json
from time import time
from uuid import uuid4
from flask import Flask
from api import block_chain

#TODO: Add in mine and transaction functions and implement Consenus algo for a decentralized network
'''
Proof algorithm:
- find a number that is p, such that hash(pp) has 4 leading zeros and where p is the previous p
- p represents the previous proof, also p is considered the new proof
'''
# Help me get started: 
# https://hackernoon.com/learn-blockchains-by-building-one-117428612f46
# https://www.activestate.com/blog/how-to-build-a-blockchain-in-python/

app = Flask(__name__)
app.register_blueprint(block_chain)

node_identifer = str(uuid4()).replace('-','')

class Block:
    def __init__(self,index,transactions,timestamp,previous_hash):
        self.index = index
        self.transactions = transactions
        self.timestamp = timestamp
        #self.previous_hash = previous_hash
        self.nonce = 0

    def hash(self):
        block_string = json.dumps(self.__dict__,sort_keys=True)
        return hashlib.sha256(block_string.encode()).hexdigest()

class Blockchain:
    #How hard with PoW algo will be
    difficulty = 2

    def __init__(self):
        self.current_transactions = []
        self.chain = []
        self.genesis_block()

    #Make sure there aren't any predecessors before 0, genesis block starts at 0 and so does previous_hash which makes it a valid hash
    def genesis_block(self):
        genesis_block = Block(0, [], time(), "0")
        genesis_block.hash = genesis_block.hash()
        self.chain.append(genesis_block)

    #aka the last block
    def straggler(self):
        return self.chain[-1]

    def valid_proof(block, block_hash):
        return(block_hash.startswith('0' * Blockchain.difficulty) and
        block_hash == block.hash())

    #Check to make sure proof is valid
    def init_block(self,block,proof,previous_hash=None):
        '''
        self.previous_hash = self.straggler.hash
        if self.previous_hash != block.previous_hash:
            return False
        elif self.previous_hash != self.valid_proof(block,proof):
            return False
        block.hash = proof
        self.chain.append(block)
        return True
        '''
        self.init_block(previous_hash=1, proof=100)
        block = {
           'index': len(self.chain) + 1,
           'timestamp': time(),
           'transactions': self.current_transactions,
           'proof': proof,
           'previous_hash': previous_hash or self.hash(self.chain[-1]),
        }
        
        #Reset the transactions
        self.current_transactions = []
        self.chain.append(block)
        return block

    #Proof of hash
    def proof(block):
        block.nonce = 0
        hash = block.hash()
        while not hash.startswith('0' * Blockchain.difficulty):
            block.nonce += 1
            hash = block.hash()
        return hash
    
    #Create new transactions
    def new_transactions(self,sender,recipient,amount):
        self.current_transactions.append({
            'sender': sender,
            'recipient': recipient,
            'amount': amount,
        })

        return self.straggler['index'] + 1
    
    #Mine a Block
    def mine(self):
        if not self.current_transactions:
            return False
        straggler = self.straggler
        new_block = Block(index = straggler.index+1,
                          transactions=self.current_transactions,
                          timestamp=time(),
                          previous_hash=straggler.hash)
        proof = self.proof(new_block)
        self.init_block(new_block,proof)
        self.current_transactions = []
        return new_block.index

#Set variable so the class can be used in Flask file
blockchain = Blockchain()
