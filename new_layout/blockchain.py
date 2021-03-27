import json
import hashlib
import random
from time import time
from uuid import uuid4
from flask import Flask
from api import blockchain_blueprint
from passlib.hash import argon2

#TODO: implement Consenus algo for a decentralized network, figure out a new way to validate proof with Argon2
'''
Proof algorithm:
- find a number that is p, such that hash(pp) has 4 leading zeros and where p is the previous p
- p represents the previous proof, also p is considered the new proof
'''
# Help me get started: 
# https://hackernoon.com/learn-blockchains-by-building-one-117428612f46
# https://www.activestate.com/blog/how-to-build-a-blockchain-in-python/

app = Flask(__name__)
app.register_blueprint(blockchain_blueprint)

node_identifer = str(uuid4()).replace('-','')

class Block:

  @staticmethod
  def hash(block):
    block_string = json.dumps(block,sort_keys=True).encode()
    return argon2.hash(block_string)

  # Randomize number each time for genesis_block
  genesis_block = random.randint(0,99999)

class Blockchain:

     def __init__(self):
       self.chain = []
       self.current_transactions = []

       # This is how the proof is determined from calling create_block
       self.create_block(previous_hash=Block.genesis_block,proof=100)

     # Validate the proof
     @staticmethod
     def valid_proof(last_proof,proof,last_hash):
       guess = f'{last_proof}{proof}{last_hash}'.encode()
       guess_hash = hashlib.sha256(guess).hexdigest()
       return guess_hash[:4] == "0000"

     # Create a new block when mined  
     def create_block(self,proof,previous_hash):
        block = {
           'index':len(self.chain)+1,
           'timestamp':time(),
           'transactions':self.current_transactions,
           'proof':proof,
           'previous_hash':Block.hash(previous_hash) or self.hash(self.chain[-1]),
        }

        self.current_transactions = []
        self.chain.append(block)
        return block
     
     # Proof algo, explained at the top
     def PoW(self, last_block):
        last_proof = last_block['proof']
        last_hash = Block.hash(last_block)

        proof = 0
        while self.valid_proof(last_proof, proof, last_hash) is False:
            proof += 1

        return proof

     # Create new transactions, this still needs to be implemented   
     def new_transactions(self,sender,recipient,amount):
       self.current_transactions.append({
           'sender': sender,
           'recipient': recipient,
           'amount': amount,

       })

       return self.last_block['index']+1

     # Just call the last block mined
     @property
     def last_block(self):
          return self.chain[-1]
          
# Classes assigned to vars
bc = Blockchain()
block = Block()
