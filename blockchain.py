import json, hashlib, random, requests, binascii, string, argon2
from time import time
from uuid import uuid4
from flask import Flask
from api import blockchain_blueprint
'''
Proof algorithm:
- find a number that is p, such that hash(pp) has 4 leading zeros and where p is the previous p
- p represents the previous proof, also p is considered the new proof
'''
# Help me get started: 
# https://hackernoon.com/learn-blockchains-by-building-one-117428612f46 (Improving slowly upon this)
# https://www.activestate.com/blog/how-to-build-a-blockchain-in-python/

app = Flask(__name__)
app.register_blueprint(blockchain_blueprint)

node_identifer = str(uuid4()).replace('-','')

class Block:
  
  # Generate secured salts of 128 bits
  def salt_gen(size=128, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.SystemRandom().choice(chars) for _ in range(size))

  # hash
  @staticmethod
  def hash(block):
   block_string = json.dumps(block,sort_keys=True).encode()
   a2 = argon2.hash_password_raw(
        time_cost=12, memory_cost=64, parallelism=8, hash_len=16, type=argon2.low_level.Type.ID,
        password=block_string, salt=Block.salt_gen().encode()
   )
   return (binascii.hexlify(a2).decode("utf-8","ignore"))
   

  # Randomize number each time for genesis_block
  genesis_block = random.randint(0,99999)

class Blockchain:
  def __init__(self):
    self.chain = []
    self.current_transactions = []
    self.nodes = set()

    # This is how the proof is determined from calling create_block
    self.create_block(previous_hash=Block.genesis_block,proof=100)

# Check to make sure the current chain is accurate 
  def validate_chain(self, chain):
    last_block = chain[0]
    curr_index = 1

    while curr_index < len(chain):
      block = chain[curr_index]
      print('{}'.format(last_block))
      print('{}'.format(block))
      # Check hash of block
      if block['previous_hash'] != self.hash(last_block):
        return False
      # Check PoW
      if not self.valid_proof(last_block['proof'], block['proof'], block['previous_hash']):
        return False

      last_block = block
      curr_index += 1
      return True

  # Consenus algo
  def conflicts(self):
    neighbors = self.nodes
    new_chain = None
    max_len = len(self.chain)
    
    for node in neighbors:
      respone = requests.get('http://{0}/chain'.format(node))
      
      if respone.status_code == 200:
        length = respone.json()['length']
        chain = respone.json()['chain']
        
        if length > max_len and self.validate_chain(chain) and length == len(chain):
          max_len = length
          new_chain = chain

      if new_chain:
        self.chain = new_chain
        return True
      return False
  
  # Add new nodes
  def new_node(self, address):
    parsed_url = urlparse(address)
    if parsed_url.netloc:
      self.nodes.add(parsed_url.netloc)
    elif parsed_url.path:
      self.nodes.add(parsed_url.path)
    else:
      raise ValueError('Invalid url')
  
  # Validate the proof
  @staticmethod
  def valid_proof(last_proof,proof,last_hash):
    guess = '{0}{1}{2}'.format(last_proof,proof,last_hash).encode()
    guess_hash = hashlib.sha256(guess).hexdigest()
    return guess_hash[:4]=="0000"

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
