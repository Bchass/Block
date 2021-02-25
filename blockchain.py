import hashlib
import json
from time import time
from uuid import uuid4

#https://hackernoon.com/learn-blockchains-by-building-one-117428612f46
#creates empty lists for constructor
class Blockchain(object):
  '''
  Proof algorithm:
  - find a number that is p, such that hash(pp) has 4 leading zeros and where p is the previous p
  - p represents the previous proof, also p is considered the new proof
  https://en.wikipedia.org/wiki/Hashcash?ref=hackernoon.com
  '''
def proof(self,last_proof):

      proof = 0
      while self.valid_proof(last_proof, proof) is False:
        proof += 1
      return proof

  #validate the proof is correct
def validate_proof(last_proof,proof):
      guess = f'{last_proof}{proof}'.encode()
      guess_hash = hashlib.sha256(guess).hexdigest()
      return guess_hash[:4] == "0000"

def __init__(self):
  self.chain = []		
  self.current_transactions = []
		
		#genesis block -> make sure there are no previous predecessors
  self.new_block(previous_hash = 1, proof = 100)
	
def new_block(self):
#parameters for each block that is created
  block = {
		'index': len(self.chain) + 1,
		'timestamp': time(),
		'transactions': self.current_transactions,
		'proof': proof,
		'previous_hash': previous_hash or self.hash(self.chain[-1]),
}
		#reset the list of transactions
  self.current_transactions=[]
  self.chain.append(block)
  return block
  
  #add in information for current transactions
def new_transaction(self):
  self.current_transactions.append({
			'sender': test,
			'recipient': test,
			'amount': test,
})

  return self.last_block['index']+1

  #TODO: implement scrypt instead of sha256 after up and running
@staticmethod
def hash(block):
  block_string = json.dumps(block,sort_keys=True).encode()
  return hashlib.sha256(block_string).hexdigest()
	
def last_block():
  return self.chain[-1]


	
