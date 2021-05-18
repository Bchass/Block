import blockchain
from flask import Blueprint, jsonify, request

#TODO: Figure out why regestring a node is throwing 405

blockchain_blueprint = Blueprint('blockchain_blueprint',__name__)

# Call the chain
@blockchain_blueprint.route('/chain',methods=['GET'])
def get_chain():
  respone = {
    'chain': blockchain.bc.chain,
    'length':len(blockchain.bc.chain)
  }
  return jsonify(respone), 200

# Mine a block
@blockchain_blueprint.route('/mine', methods=['GET'])
def mine_block():
  last_block = blockchain.bc.last_block
  proof = blockchain.Blockchain().PoW(last_block)

  blockchain.Blockchain().new_transactions(
    sender="0",
    recipient=blockchain.node_identifer,
    amount = 1
  )
  previous_hash = blockchain.block.hash(last_block)
  block = blockchain.bc.create_block(proof,previous_hash)

  response = {
    "message":"New Block Mined",
    "index":block['index'],
    "transactions":block['transactions'],
    "proof":block['proof'],
    "previous_hash":block['previous_hash'],
  }
  return jsonify(response), 200

# Retrieve all the transactions that have taken place
@blockchain_blueprint.route('/transactions/new', methods=['POST'])
def transacation():
  values = request.get_json(force=True)

  required = ['sender','recipient','amount']
  if not all(x in values for x in required):
    return 'Missing values',400

  index = blockchain.bc.new_transactions(values['sender'],values['recipient'],values['amount'])
  response = {'message': f'Transaction being added to Block {index}'}
  return jsonify(response),201


@blockchain_blueprint.route('/nodes/register',methods=['POST'])
def register_nodes():
  values = request.get_json(force=True)

  nodes = values.get('nodes')
  if nodes is None:
    return "Error: Need a valid list of nodes", 400

  for node in nodes:
    blockchain.register_nodes(node)

  response = {
    'message': 'Nodes have been added',
    'Total': list(blockchain.bc.nodes),
  }
  return jsonify(response), 201


# Resolve any conflicts with a chain
@blockchain_blueprint.route('/nodes/resolve', methods=['GET'])
def cs():
  replaced = blockchain.bc.conflicts()

  if replaced:
    respone = {
      'message': 'Chain replaced',
      'new_chain': blockchain.bc.chain
    }
  else:
      respone ={
        'message': 'Chain is authorized',
        'chain': blockchain.bc.chain
      }
      return jsonify(respone), 200
