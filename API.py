import The_Block
import json
from flask import Blueprint, jsonify, request

block_chain = Blueprint('block_chain',__name__)

@block_chain.route('/chain',methods=['GET'])
def get_chain():
    chain_data = []
    for block in The_Block.blockchain.chain:
      chain_data.append(block.__dict__)
    return json.dumps({"length": len(chain_data),
                       "chain": chain_data})


@block_chain.route('/transactions/new', methods=['POST'])
def new_transactions():
    values = request.get_json()
    index = The_Block.blockchain.new_transactions(values['sender'],values['recipient'],values['amount'])

    response = {
        'message': f'Transaction be added to Block {index}'
    }
    return jsonify(response),201
