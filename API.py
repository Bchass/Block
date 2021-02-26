from flask import Blueprint,jsonify,request

app_page = Blueprint('app_page',__name__)

@app_page.route('/mine',methods=['GET'])
def mine():
  return "Mining new block"

@app_page.route('/transactions/new',methods=['POST'])
def transaction():
  return "Adding new transaction"

@app_page.route('/chain',methods=['GET'])
def chain():
    response = {
        'chain':blockchain.chain,
        'length':len(blockchain.chain)
        }
    return jsonify(response),200
