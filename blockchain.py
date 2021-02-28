import hashlib
import json
from time import time
from uuid import uuid4
from flask import Flask
from API import app_page

# TODO: Implement Scrypt after up and runnign with sha256
# https://hackernoon.com/learn-blockchains-by-building-one-117428612f46
# creates empty lists for constructor
'''
Proof algorithm:
- find a number that is p, such that hash(pp) has 4 leading zeros and where p is the previous p
- p represents the previous proof, also p is considered the new proof
https://en.wikipedia.org/wiki/Hashcash?ref=hackernoon.com
'''

app = Flask(__name__)
app.register_blueprint(app_page)
node_identifer = str(uuid4()).replace('-','')

class Blockchain(object):
    def __init__(self):
        self.chain = []
        self.current_transaction = []

        #genesis block, make sure there are no previous predecessors
        self.new_block(previous_hash = 1, proof = 100)

    #Validate the proof is correct
    def proof(self,last_proof):
        proof = 0
        while self.valid_proof(last_proof,proof) is False:
            proof += 1
            return proof

    def validate_proof(last_proof,proof):
        guess = f'{last_proof}{proof}'.encode()
        guess_hash = hashlib.sha256(guess).hexdigest()
        return guess_hash[:4] == "0000"

    #Params for each new block that is created    
    def new_block(self,proof,previous_hash):
        block = {
        'index': len(self.chain) + 1,
		'timestamp': time(),
		'transactions': self.current_transactions,
		'proof': proof,
		'previous_hash': previous_hash or self.hash(self.chain[-1]), 
        }

        #Reset the list of transactions
        self.current_transaction = []
        self.chain.append(block)
        return block
    
    #Add in information for current transactions
    def new_transaction(self,sender,recipient,amount):
        self.curremt_transactions.append({
            'sender': sender,
            'recipient': recipient,
            'amount': amount

            })
        return self.last_block['index']+1

    def hash(block):
        block_string = json.dumps(block,sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()

    def last_block(self):
        return self.chain[-1]