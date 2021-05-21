from flask import Flask, jsonify, request
from blockchain import Blockchain
from uuid import uuid4

app = Flask(__name__)
node_identifer = str(uuid4()).replace("-", "")

blockchain = Blockchain()

# Call the chain
@app.route("/chain", methods=["GET"])
def get_chain():
    respone = {"chain": blockchain.chain, "length": len(blockchain.chain)}
    return jsonify(respone), 200


# Mine a block
@app.route("/mine", methods=["GET"])
def mine_block():
    last_block = blockchain.last_block
    proof = blockchain.Blockchain().PoW(last_block)

    blockchain.Blockchain().new_transactions(
        sender="0", recipient=node_identifer, amount=1
    )
    previous_hash = blockchain.hash(last_block)
    block = blockchain.create_block(proof, previous_hash)

    response = {
        "message": "New Block Mined",
        "index": block["index"],
        "transactions": block["transactions"],
        "proof": block["proof"],
        "previous_hash": block["previous_hash"],
    }
    return jsonify(response), 200


# Retrieve all the transactions that have taken place
@app.route("/transactions/new", methods=["POST"])
def transacation():
    values = request.get_json(force=True)

    required = ["sender", "recipient", "amount"]
    if not all(x in values for x in required):
        return "Missing values", 400

    index = blockchain.new_transactions(
        values["sender"], values["recipient"], values["amount"]
    )
    response = {"message": f"Transaction being added to Block {index}"}
    return jsonify(response), 201


@app.route("/nodes/register", methods=["POST"])
def register_nodes():
    values = request.get_json(force=True)

    nodes = values.get("nodes")
    if nodes is None:
        return "Error: Need a valid list of nodes", 400

    for node in nodes:
        blockchain.register_nodes(node)

    response = {
        "message": "Nodes have been added",
        "Total": list(blockchain.nodes),
    }
    return jsonify(response), 201


# Resolve any conflicts with a chain
@app.route("/nodes/resolve", methods=["GET"])
def cs():
    replaced = blockchain.conflicts()

    if replaced:
        respone = {"message": "Chain replaced", "new_chain": blockchain.chain}
    else:
        respone = {"message": "Chain is authorized", "chain": blockchain.chain}
        return jsonify(respone), 200
