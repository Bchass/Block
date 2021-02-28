from flask import Blueprint,jsonify,request
import blockchain as BC
from .blockchain import Blockchain as BC

# This will all be reworked

app_page = Blueprint('app_page',__name__)

@app_page.route('/mine',methods=['GET'])
def mine():
  last_block = BC.last_block
  last_proof = last_block['proof']
  prf = BC.proof(last_proof)

  BC.new_transaction(
    sender="0",
    recipient=BC.node_identifer,
    amount=1
  )

  previous_hash = BC.hash(last_block)
  BC.block = BC.new_block(prf,previous_hash)

  response = {
    'message': 'New Block',
    'index': BC.block['index'],
    'transactions': BC.block['transactions'],
    'proof': BC.block['proof'],
    'previous_hash': BC.block['previous_hash']
      }
  return jsonify(response), 200

@app_page.route('/transactions/new',methods=['POST'])
def transaction():
  values = request.get_json()
  
  #Make sure all params are met
  required = ['sender','recipient','amount']
  if not all(x in values for x in required):
    return 'Missing values', 400

  #Creating a new transaction
  index = BC.new_transaction(values['sender'],values['recipient'],values['amount'])
  response = {f'Transaction will be added to Block{index}'}
  return jsonify(response), 201


@app_page.route('/chain',methods=['GET'])
def chain():
    response = {
        'chain':BC.chain,
        'length':len(BC.chain)
        }
    return jsonify(response),200